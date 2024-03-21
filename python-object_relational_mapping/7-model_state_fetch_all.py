#!/usr/bin/python3


"""Write a python file that contains the class definition of
a State and an instance Base = declarative_base()
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    """including the guard clause"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    """creating a SQLAlchemy engine that will connect to the MySQL database"""

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query the database by selecting all rows from the
    State table, ordered by the id column
    """
    for states in session.query(State).order_by(State.id):
        print(f"{states.id}: {states.name}")
