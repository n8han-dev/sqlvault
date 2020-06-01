from cryptography.fernet import Fernet
import os


class Password:

    def get_password(self, vault):
        key_file = "key%s.bin" % vault
        vault_file = "vault%s.bin" % vault
        key = self.get_key(key_file)
        if not key:
            return 0
        flag = self.check_password(vault_file, key)
        return flag

    @staticmethod
    def create_key(key_name):
        key = Fernet.generate_key()
        with open(key_name, "wb") as k:
            k.write(key)

    def add_password(self, vault):
        new_pass = input("Enter new password: ")
        pass_file = "vault%s.bin" % vault
        key_name = "key%s.bin" % vault
        self.create_key(key_name)
        with open(key_name, "rb") as k:
            for line in k:
                key = line
        encrypts = Fernet(key)
        enc_password = encrypts.encrypt(bytes(new_pass, "utf-8"))
        with open(pass_file, "wb") as pas:
            pas.write(enc_password)
        print("Created key and password for vault%s" % vault)

    @staticmethod
    def get_key(file):
        if not os.path.exists(file) or os.stat(file).st_size == 0:
            print("Error: no key found")
            return False
        with open(file, "rb") as k:
            for line in k:
                key = line
        return key

    @staticmethod
    def check_password(pass_file, key):
        with open(pass_file, "rb") as ps:
            for line in ps:
                enc_pass = line
        decrypter = Fernet(key)
        dec_pass = decrypter.decrypt(enc_pass).decode("utf-8")
        inp_pass = input("Input your password: ")
        print(dec_pass, inp_pass)
        if dec_pass == inp_pass:
            print("success")
            return True
        else:
            print("incorrect password")
            return False
