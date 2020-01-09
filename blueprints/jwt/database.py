import os

import sqlalchemy as db

connection_str = os.getenv("DB_CONNECTION_STRING")
schema_name = os.getenv("DB_SCHEMA")


def username_lookup(input_username):
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData(schema=schema_name)
    users = db.Table('users', metadata, autoload=True, autoload_with=engine)
    query_username = db.select([db.func.count(users.columns.email)]).where(users.columns.email == input_username)
    ResultProxy = connection.execute(query_username)
    ResultSet = ResultProxy.fetchall()
    if ResultSet[0][0] == 1:
        return True
    else:
        return False


def password_lookup(input_username):
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData(schema=schema_name)
    users = db.Table('users', metadata, autoload=True, autoload_with=engine)
    query_username = db.select([users.columns.password]).where(users.columns.email == input_username)
    ResultProxy = connection.execute(query_username)
    ResultSet = ResultProxy.fetchall()
    return str(ResultSet[0][0])


def access_lookup(input_username):
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData(schema=schema_name)
    users = db.Table('users', metadata, autoload=True, autoload_with=engine)
    query_username = db.select([users.columns.access]).where(users.columns.email == input_username)
    ResultProxy = connection.execute(query_username)
    ResultSet = ResultProxy.fetchall()
    return str(ResultSet[0][0])
