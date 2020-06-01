import mysql.connector


class Sql:

    def connect(self):
        print("connect")

    def conflict(self):
        print("i want conflict with line 1")
        print("i want conflict with line 2")

    def no_conflict(self):
        pass  # i don't conflict
