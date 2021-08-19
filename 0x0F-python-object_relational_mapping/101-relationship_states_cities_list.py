#!/usr/bin/python3
"""Consult all cities'"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    """Consult with method Session of Alchemist"""
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        server = "localhost"
        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, server, database), pool_pre_ping=True)
        """Verifica que la tabla este creada en la bd"""
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(State).all()
        for state in result:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("    {}: {}".format(city.id, city.name))
        session.close()

    else:
        print("Error - Introduce los argumentos correctamente")
