# buluta kayıt

from bulut_save import blt_save

class Kayıt:
    def __init__(self):
        self.islem()
    def islem(self):
        while True:
            
            while True:
    
                username = input("kullanıcı adı:")
                if blt_save().usernamekontrol(username) == True:
                    break
                else:
                    print("username zaten kayıtlı tekrar dene")
                    continue
            while True:

                eposta = input("e- mail adresi:")
                if blt_save().epostakontrol(eposta) == True:
                    break
                else:
                    print("eposta zaten kayıtlı tekrar dene")
                    continue
            while True:
                sifre = input("şifre oluştur:")
                sifre2 = input("şifreyi tekrar gir:")
                if sifre == sifre2:
                    break
                else:
                    continue
            break
        self.liste = [username,sifre,eposta]
        blt_save()
        blt_save().insert_user(self.liste)
            