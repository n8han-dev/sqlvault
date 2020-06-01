from passwd import Password
import os


class Vault:

    password_instance = Password()

    def create_vault(self, vault):
        print("create Vault")
        if os.path.exists("vault%s.bin" % vault):
            print("Err: vault%s exists" % vault)
            return False
        self.password_instance.add_password(vault)
        return True

    def enter_vault(self, vault):
        print("Enter Vault")
        result = self.password_instance.get_password(vault)
        if not result:
            return False

    @staticmethod
    def delete_vault(vault):
        print("delete Vault")

    def start(self):
        pr = "Enter 1 to reach your vault\nEnter 2 to create a new vault\nEnter 3 to delete a vault\n- "
        options = {"1": "enter_vault", "2": "create_vault", "3": "delete_vault"}
        option = input(pr)
        try:
            int(option)
        except ValueError:
            print("Error: input should be int")
            return 0
        action = options.get(option, "err_handler")
        vault = input("Enter vault name: ")
        res = getattr(self, action)(vault)
        if not res:
            return 0


v1 = Vault()
v1.start()
