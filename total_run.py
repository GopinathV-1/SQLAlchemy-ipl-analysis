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

    class Deliveries(Base):
        __tablename__ = 'deliveries'

        id = Column(Integer, primary_key=True)
        batting_team = Column(String)
        batsman = Column(String)
        total_runs = Column(Integer)

    Base.metadata.create_all(engine)

    # storing csv file data in table
    try:
        with open('deliveries.csv', 'r') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                row_value = Deliveries(
                    id=index,
                    batting_team=abbreviate_team_name(row['batting_team']),
                    batsman=row['batsman'],
                    total_runs=row['total_runs']
                )
                session.add(row_value)
            session.commit()
    except exc.IntegrityError:
        session.rollback()
    return Deliveries


def create_json(Deliveries):
    ''' creating json file from the data
        in the table'''

    # Query to compute total runs scored each team
    total_runs = session.query(Deliveries.batting_team, func.sum(
                        Deliveries.total_runs)).group_by(
                        Deliveries.batting_team).all()
    total_runs = [list(row) for row in total_runs]

    data = {'total_run': []}
    data['total_run'] = total_runs

    with open('total_run.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":

    data = create_table_from_csv()
    create_json(data)
