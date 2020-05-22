import passwd
import connect_sql


class Vault:

    @staticmethod
    def enter_vault():
        print("Enter Vault")

    @staticmethod
    def create_vault():
        print("create Vault")

    @staticmethod
    def delete_vault():
        print("delete Vault")

    def start(self):
        pr = "Enter 1 to reach your vault\nEnter 2 to create new vault\n- "
        options = {"1": "enter_vault", "2": "create_vault", "3": "delete_vault"}
        option = input(pr)
        try:
            int(option)
        except ValueError:
            print("Error: input should be int")
        action = options.get(option, lambda: "No such option")
        action()


v1 = Vault()
v1.start()
