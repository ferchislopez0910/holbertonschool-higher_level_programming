#!/usr/bin/python3
"""Start link class to table in database """
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    """Consult with method Session of Alchemist"""
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        server = "localhost2"
        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, server, database), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
        session.close()

    else:
        print("Error - Introduce los argumentos correctamente")
