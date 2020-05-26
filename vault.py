from passwd import PassHandler as Paswd
import connect_sql
import os


class Vault:

    @staticmethod
    def enter_vault(vault):
        print("Enter Vault")
        key = Paswd.get_password(vault)
        print(key)

    @staticmethod
    def create_vault(vault):
        print("create Vault")
        if os.path.exists("vault%s.bin" % vault):
            print("Err: vault exists")
            return 0
        pas = "vault%s.bin" % vault
        Paswd.add_password(pas)

    @staticmethod
    def delete_vault(vault):
        print("delete Vault")

    @staticmethod
    def err_handler(vault):
        print("Error", vault)

    def start(self):
        pr = "Enter 1 to reach your vault\nEnter 2 to create new vault\n- "
        options = {"1": "enter_vault", "2": "create_vault", "3": "delete_vault"}
        option = input(pr)
        try:
            int(option)
        except ValueError:
            print("Error: input should be int")
            return 0
        action = options.get(option, "err_handler")
        vault = input("Enter vault name: ")
        getattr(self, action)(vault)


v1 = Vault()
v1.start()
