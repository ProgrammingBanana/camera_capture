import sqlite3


class Database():
    def __init__(self):
        """ Initializes the object by connecting to the database and creating the table if it didnt exist """
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
        """Creates table if it doesnt exist """

        CREATE_TABLE_SIGNS = """CREATE TABLE IF NOT EXISTS signs(
                                    name_pk TEXT NOT NULL PRIMARY KEY,
                                    count INTEGER NOT NULL,
                                    path TEXT NOT NULL
                                )WITHOUT ROWID;"""

        self.cursor.execute(CREATE_TABLE_SIGNS)


    def insert_sign(self, name, path):
        """ Inserts a sign entry into the signs table
        Args:
            name (String): Primary Key, name of the sign
            path (String): String representation of folder path
        """

        INSERT_TABLE_SIGNS = """INSERT INTO signs (name_pk, count, path ) VALUES (?,?,?);"""

        count = self.cursor.execute(INSERT_TABLE_SIGNS, (name, 0, path))
        self.conn.commit()


    def update_sign(self, name, amount_recorded):
        """ Updates a sign entry in the signs table by incrementing the amount of recordings done in count
        Args:
            name (String): Primary Key, name of the sign
            amount_recorded (Integer): Amount of new videos recorded
        """
        
        count = self.get_count(name)
        new_count = count + amount_recorded

        UPDATE_TABLE_SIGNS = """UPDATE signs
                                    SET count  = (?)
                                WHERE name_pk = (?);"""
        
        self.cursor.execute(UPDATE_TABLE_SIGNS, (new_count, name))
        self.conn.commit()

    def get_count(self, name):
        """ Gets the amounts of videos recorded for a given sign

        Args:
            name (String): Primary Key, name of the sign
        Returns:
            Integer: amount of videos recorded for a given sign
        """

        GET_COUNT = """SELECT count FROM signs
                       WHERE name_pk = (?);"""

        count =  self.cursor.execute(GET_COUNT, (name,)).fetchall()[0][0]

        return count


    def get_signs(self):
        """ Gets a list of all signs and their data

        Returns:
            List: List of sign tuples that contain the name, count and file path for a given sign
        """

        GET_SIGNS = """ SELECT * FROM signs"""

        return self.cursor.execute(GET_SIGNS).fetchall()