#!/usr/bin/python3


"""Write a script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa
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

    # Récupérer les états dont le nom contient la lettre 'a'
    states = session.query(State).filter(State.name.like('%a%'))

    # Supprimer ces états
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
