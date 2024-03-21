#!/usr/bin/python3


"""Write a script that adds the State object
Louisiana to the database hbtn_0e_6_usa
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

    # Créer un nouvel état
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()
