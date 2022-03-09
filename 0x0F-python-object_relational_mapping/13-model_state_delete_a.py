#!/usr/bin/python3
"""
python script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://argv[1]:argv[2]@localhost/argv[3]')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    part = '%a%'
    states = session.query(State).filter(State.name like(part))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
