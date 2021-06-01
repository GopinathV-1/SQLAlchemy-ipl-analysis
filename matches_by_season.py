from sqlalchemy import Column, Integer, String, func, create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv
import json

engine = create_engine('postgresql://test:test@localhost:5432/test')
session = sessionmaker(bind=engine)()


def abbreviate_team_name(name):
    '''making abbreviation names'''
    split_name = name.split(' ')
    short_name = [each[0] for each in split_name]
    return ''.join(short_name)


def create_table_from_csv():
    ''' creating table and storing csv file values
        in the table'''

    Base = declarative_base()

    class Matches(Base):
        __tablename__ = 'matches'

        id = Column(Integer, primary_key=True)
        season = Column(Integer)
        team = Column(String)

    Base.metadata.create_all(engine)

    # storing csv file data in table
    try:
        with open('matches.csv', 'r') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                row_value = Matches(
                    id=index*2,
                    season=row['season'],
                    team=abbreviate_team_name(row['team1'])
                )
                session.add(row_value)
                row_value_next = Matches(
                    id=index*2 + 1,
                    season=row['season'],
                    team=abbreviate_team_name(row['team2'])
                )
                session.add(row_value_next)
            session.commit()
    except exc.IntegrityError:
        session.rollback()
    return Matches


def create_json(Matches):
    ''' creating json file from the data
        in the table'''

    # Query to count number of matches palyed by each team in each season
    season = (session.query(
             Matches.team, Matches.season,
             func.count(Matches.team),
             func.dense_rank().over(order_by=Matches.team))
             .group_by(Matches.team, Matches.season)
             .order_by(Matches.team, Matches.season).all())

    # provinding default value 0 for teams that not played in specific season
    data, rank, season_year = dict(), 0, set()
    for row in season:
        if rank < row[3]:
            data[row[0]] = [0] * (row[1] - 2008)
            rank = row[3]
        data[row[0]].append(row[2])
        season_year.add(row[1])

    data['season'] = sorted(list(season_year))
    for row in data.items():
        data[row[0]] += [0] * (len(data['season']) - len(row[1]))

    with open('matches_by_season.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":

    data = create_table_from_csv()
    create_json(data)
