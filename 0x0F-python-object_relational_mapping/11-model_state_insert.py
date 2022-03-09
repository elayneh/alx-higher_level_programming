#!/usr/python3
"""
python script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
list the first State object from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from mode_state import Base, State


if __name__ = "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(state).order_by(State_id).first()
    if first_state is not None:
        print("{}".format(first_state.id, first_State.name))
    else:
        print("Nothing")
    session.close()
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create('mysql+myqldb://argv[1]:argv[2]@localhost/argv[3]')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    state = session.query(State).filter(name='Louisiana').first()
    print(state.id)
    session.commit()
    session.close()
