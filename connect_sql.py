import mysql.connector


class Sql:

    def connect(self):
        print("connect")

    def conflict(self):
        print("conflict line 1")
        print("conflict line 2")

    def no_conflict(self):
        pass  # i don't conflict
