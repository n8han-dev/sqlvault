from cryptography.fernet import Fernet
import os


class PassHandler:

    def get_password(self, vault):
        key = self.get_key()
        flag = self.check_password(vault, key)
        return flag

    @staticmethod
    def create_key():
        key = Fernet.generate_key()
        with open("key.bin", "wb") as k:
            k.write(key)

    def add_password(self, filename):
        new_pass = input("Enter new password: ")
        with open(filename, "wb") as pas:
            pas.write(bytes(new_pass))

    @staticmethod
    def encrypt_password():
        pass

    def get_key(self):
        if not os.path.exists("key.bin") or os.stat("key.bin").st_size == 0:
            self.create_key()
            print("key created")
        with open("key.bin", "rb") as k:
            for line in k:
                key = line
        return key

    @staticmethod
    def check_password(vault, key):
        pass_file = "pass%s.bin" % vault
        with open(pass_file, "rb") as ps:
            for line in ps:
                enc_pass = line
        decrypter = Fernet(key)
        dec_pass = decrypter.decrypt(enc_pass)
        inp_pass = input("Input your password: ")
        if dec_pass == inp_pass:
            print("success")
            return 1
        else:
            print("incorrect password")
            return 0
