# buluta giriş

from bulut_save import blt_save
from ui_gelir_gider import ui_gelir_giderr


class Giris:
    def __init__(self):
        self.islem()

    def islem(self):
        while True:
            username = input("kullanıcı adı:")
            sifre = input("şifre:")
            if blt_save().login(username,sifre) == True:
                print("hatalı kullanıcı adı ve şifre")
                continue
            else:
                print(f"giriş işlemi başarılı hoşgeldin {username}")
                ui_gelir_giderr("blt",username)
                break
                