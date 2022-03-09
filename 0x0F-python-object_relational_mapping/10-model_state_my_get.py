#!/usr/bin/python3
"""
python script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

"""
import sqlalchemy
from state_model import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql_mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Sessionmaker(bind=engine)
    session = Session()
    state = session.query(state).filter_by(name=argv[4]).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
