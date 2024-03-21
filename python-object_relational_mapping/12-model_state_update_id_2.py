#!/usr/bin/python3


"""Write a script that changes the name of a
State object from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer l'état avec id = 2
    state = session.query(State).get(2)

    if state is not None:
        # Changer le nom de l'état
        state.name = "New Mexico"
        session.commit()
        session.close()
