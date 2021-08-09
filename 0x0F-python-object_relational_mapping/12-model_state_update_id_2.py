#!/usr/bin/python3
"""Write a script that lists all State objects that contain the letter 'a'"""
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine)


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
        """Se busca un registro con el id 2
        y se cambia por uno nuevo, este metodo
        solo es para cambiar un regitro.
        """
        i = session.query(State).get(2)
        i.name = "New Mexico"
        session.add(i)
        session.commit()
        session.close()

    else:
        print("Error - Introduce los argumentos correctamente")
