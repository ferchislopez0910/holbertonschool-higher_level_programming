#!/usr/bin/python3
"""Consult all cities'"""
from sys import argv
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

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
        """para buscar en dos tablas
        en una se necesita el estado
        en otra la cuidad.
        """
        result = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
        for city, state in result:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.close()

    else:
        print("Error - Introduce los argumentos correctamente")
