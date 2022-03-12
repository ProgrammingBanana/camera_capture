import sqlite3


class Database():
    def __init__(self):
        """ Initializes the object by connecting to the database and creating all tables if they didnt exist """
        self.conn =  sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = 1") #This is needed in order to force sqlite to enforce foreign keys
        self.create_tables()

    def close(self):
        """ Ensures that the database connection is closed """
        self.cursor.close()
        self.conn.close()

    def drop_tables(self):
        """ Drops all tables in the database"""
        self.cursor.execute("DROP TABLE signs;")

        print("The table have been dropped")


    def create_tables(self):
        """Creates all tables if they dont exist """

        CREATE_TABLE_SIGNS = """CREATE TABLE IF NOT EXISTS signs(
                                    name_pk TEXT NOT NULL PRIMARY KEY,
                                    count INTEGER NOT NULL,
                                    path TEXT NOT NULL
                                )WITHOUT ROWID;"""

        self.cursor.execute(CREATE_TABLE_SIGNS)


    def insert_sign(self, name, path):
        """ Inserts a robot into the database
        Args:
            name (String): Robot string representation (Since these are unique, they are used as primary keys)
            path (String): String representation of folder path
        """

        INSERT_TABLE_SIGNS = """INSERT INTO signs (name_pk, count, folder ) VALUES (?,?,?);"""

        count = self.cursor.execute(INSERT_TABLE_SIGNS, (name, 1, path))
        self.conn.commit()


    def update_sign(self, name, amount_recorded):
        """ Updates a robot in the database, by setting obj to the current version of the robot obj 
        Args:
            name (String): Robot string representation (Since these are unique, they are used as primary keys)
            amount_recorded (Integer): Amount of new videos recorded
        """
        
        count = self.get_count()
        new_count = count + amount_recorded

        UPDATE_TABLE_SIGNS = """UPDATE signs
                                    SET count  = (?)
                                WHERE name_pk = (?);"""
        
        self.cursor.execute(UPDATE_TABLE_SIGNS, (new_count, name))
        self.conn.commit()

    def get_count(self, name):
        GET_COUNT = """SELECT count FROM signs
                       WHERE name_pk = (?);"""

        return self.cursor.execute(GET_COUNT, (name,)).fetchall()