#!/usr/bin/python3
"""Consult all cities'"""
from sys import argv
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """Consult with method Session of Alchemist"""
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        server = "localhost2"
        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, server, database), pool_pre_ping=True)
        """Verifica que la tabla este creada en la bd"""
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        new_city = State(name="California")
        new_city.cities = [City(name="San Francisco")]
        session.add(new_city)
        session.commit()
        session.close()

    else:
        print("Error - Introduce los argumentos correctamente")
