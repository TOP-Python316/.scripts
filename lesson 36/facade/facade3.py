import sqlite3


# Класс для работы с базой данных
class Database:
    def __init__(self, dbname):
        self._conn = sqlite3.connect(dbname)
        self._cursor = self._conn.cursor()

    def execute_query(self, query, params=()):
        self._cursor.execute(query, params)
        self._conn.commit()

    def execute_read_query(self, query, params=()):
        self._cursor.execute(query, params)
        return self._cursor.fetchall()


# Класс-фасад для работы с базой данных
class DataAccessObject:
    def __init__(self):
        self._db = Database("mydatabase.db")

    def create_user(self, username, password):
        self._db.execute_query("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

    def get_user(self, username):
        result = self._db.execute_read_query("SELECT * FROM users WHERE username=?", (username,))
        if len(result) == 0:
            return None
        else:
            return result[0]

# Пример использования
if __name__ == "__main__":
    dao = DataAccessObject()
    dao.create_user("user", "password")
    user = dao.get_user("user")
    print(user)