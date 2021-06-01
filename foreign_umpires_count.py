from sqlalchemy import Column, Integer, String, func, create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv
import json

engine = create_engine('postgresql://test:test@localhost:5432/test')
session = sessionmaker(bind=engine)()


def create_table_from_csv():
    ''' creating table and storing csv file values
        in the table'''

    Base = declarative_base()

    class Umpires(Base):
        __tablename__ = 'umpires'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        country = Column(String)
    Base.metadata.create_all(engine)

    # storing csv file data in table
    try:
        with open('umpires.csv', 'r') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                row_value = Umpires(id=index, name=row['umpire'],
                                    country=row[' country'])
                session.add(row_value)
            session.commit()
    except exc.IntegrityError:
        session.rollback()
    return Umpires


def create_json(Umpires):
    ''' creating json file from the data
        in the table'''

    # Query to count numuber of foreign umpire's from same country
    umpires_count = session.query(Umpires.country, func.count(
                        Umpires.name)).filter(
                        Umpires.country != ' India').group_by(
                        Umpires.country).all()

    umpires_count = [[row[0].strip(), row[1]] for row in umpires_count]
    data = {'foreign_umpires_count': []}
    data['foreign_umpires_count'] = umpires_count

    with open('foreign_umpires_count.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":

    data = create_table_from_csv()
    create_json(data)
