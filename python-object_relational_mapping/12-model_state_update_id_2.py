#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer l'état avec id = 2
    state = session.query(State).get(2)

    if state is not None:
        # Changer le nom de l'état
        state.name = "New Mexico"
        session.commit()
