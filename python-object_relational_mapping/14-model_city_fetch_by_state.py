#!/usr/bin/python3
"""
Print all City objects from the database, grouped by state
Format: <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State.name, City.id, City.name)
        .join(City, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for state_name, city_id, city_name in results:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()


if __name__ == "__main__":
    main()
