#!/usr/bin/python3
""" Creates and inserts a State objects"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


"""  adds the State object “Louisiana” to the database hbtn_0e_6_usa """
if __name__ == '__main__':
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="Louisiana"))
    print(session.query(State).filter_by(name="Louisiana").first().id)
    session.commit()
    session.close()
