from psycopg2 import pool

class Database:
    __connection_pool =None

    @classmethod
    def initialize(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1,
                                                          10,
                                                          **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls,connection):
        cls.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        cls.__connection_pool.closeall()

class CursorFromConnectionPool:

    def __init__(self):
        self.connection=None
        self.cursor=None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):  # Deal with errors coming from with statement
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)

# class ConnectionFromPool:
#
#     def __init__(self):
#         self.connection = None
#
#     def __enter__(self):
#         self.connection = connection_pool.getconn()
#         return self.connection
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection.commit()
#         connection_pool.putconn(self.connection)
