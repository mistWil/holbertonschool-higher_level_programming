#!/usr/bin/python3

from model_state import State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sys

# Assurez-vous de définir Base et State ici si ils ne sont pas définis dans model_state

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer le premier état
    state = session.query(State).order_by(State.id).first()

    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")