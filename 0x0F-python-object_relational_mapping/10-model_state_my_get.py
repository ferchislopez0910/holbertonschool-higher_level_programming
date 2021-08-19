#!/usr/bin/python3
"""Write a script that lists all State objects that contain the letter 'a'"""
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    """Consult with method Session of Alchemist"""
    if len(argv) == 5:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        search = argv[4]
        server = "localhost"
        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, server, database), pool_pre_ping=True)
        """Verifica que la tabla este creada en la bd"""
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        """Se asigna una variable para hacer la consulta
        Se busca los metodos de alchemis para hallar first
        """
        result = session.query(State).filter_by(
            name=search).first()
        if result is not None:
            print("{}".format(result.id))
        else:
            print("Not found")
        """Cuando se hace delete, insert, update, deben confimar la accion"""
        session.commit()
        session.close()

    else:
        print("Error - Introduce los argumentos correctamente")
