# burası anasayfa
# kullanıcı giriş yapacakmı yapmayacakmı kontrol edilecek 
print("""
MFT---------------MFT------------------------MFT
MFT---------------MFT------------------------MFT
MFT---------------MFT------------------------MFT
""")
from ui_gelir_gider import ui_gelir_giderr
from kayıt import Kayıt
from giris import Giris
class ana_menu:
    def __init__(self):
        self.islem()
    def islem(self):
        while True:
            print("""
                    1-Giriş Yap
                    2-Kayıt Ol
                    3-Giriş yapmadan devam et
                    4-Çıkış
            """)
            result = input("seçim:")
            if result == 1 or result == "1":
                Giris()
            elif result == 2 or result =="2":
                Kayıt()
            elif result == 3 or result =="3":
                print("Giriş yapmmadan ilerliyorsunuz...")
                ui_gelir_giderr("local","")
                break
            elif result == 4 or result =="4":
                print("kapandı...")
                break
            else:
                print("Yanlış seçim tekrar deneyiniz...")


if __name__ == "__main__":
    ana_menu()
