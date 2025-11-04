from mysql import connector

class MySQLConnectionSingleton:
    """Create multiple instances, but pointing to same object under the hood."""
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print('Class object is loaded into memory and instance is created!')
            # we are assigning class variable _instance to creating a new instance
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
            cls._instance.host = kwargs.get("host", None) 
            cls._instance.user = kwargs.get("user", None) 
            cls._instance.password = kwargs.get("password", None)
            cls._instance.database = kwargs.get("database", None)
        return cls._instance

    def __init__(self, host, user, password, database):
        print('Class instance is initialized!')
        # self._connection = None
        # self.host = host
        # self.user = user
        # self.password = password
        # self.database = database
        
    def get_connection(self):
        if not self._connection:
            self._connection = connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        return self._connection

    def execute_query(self, query):
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
    
    


class MySQLConnection:
    """Create multiple instances, and pointing to different objects under the hood."""
    _instance = None
    pass

if __name__ == "__main__":
    config = {
        "host": "asdf",
        "user": "qwer",
        "password": "zxcv",
        "database": "poiu",
    }
    instance_one = MySQLConnectionSingleton(**config)
    instance_two = MySQLConnectionSingleton(**config)
    
    print(instance_one.host is  instance_two.host)
