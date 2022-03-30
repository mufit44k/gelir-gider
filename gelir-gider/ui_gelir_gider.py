# giriş yapınca yapılacak işlemler menü
from user_islem import user_islem
from bulut_save import blt_save

class ui_gelir_giderr:
    def __init__(self,save_location,username):
        self.username = username
        self.location = save_location
        self.id = 1
        if self.location == "local":
            self.id = 1
            self.username = ""
        else:
            self.id = blt_save().user_id(self.username)
        self.islem()
    def islem(self):
        while True:
            print("""
                1-Gelir ekle
                2-Gider ekle
                3-Dönemsel olarak gelir ve gider görüntüle
                4-Veri sil
                5-Çıkış
            """)
            result = input("seçim:")
            if result == 1 or result == "1":
                while True:
                    try:
                        miktar = int(input("eklenecek miktar:"))
                        user_islem().gelir_gider(self.id, miktar, "gelir", self.location,self.username)
                        break
                    except:
                        print("hatalı girdi...")
                        continue
                
            elif result == 2 or result =="2":
                while True:
                    try:
                        miktar = int(input("harcanan miktar:"))
                        user_islem().gelir_gider(self.id, miktar, "gider", self.location,self.username)
                        break
                    except:
                        print("hatalı girdi...")
                        continue
            
            elif result == 3 or result =="3":
                print("bilgiler getiriliyor...")

                gelen = user_islem().dönem_durum(self.location, self.username)
                if gelen == []:
                    print("kayıtlı bilgi yok")
                else:
                    say = 1
                    gelir = 0
                    gider = 0
                    for i in gelen:
                        print("dönem:",i[0])
                        for x in i[1]:
                            if len(x) == 0:
                                print("döneme ait gelir yok")
                            else:
                                print("""
                                {}.gelir
                                {} tarihinde {} tl eklenmiştir.
                                """.format(say,x[0],x[1]))
                                gelir += x[1]
                                say += 1
                        say = 1
                        for a in i[2]:
                            if len(a) == 0:
                                print("döneme ait gider yok")
                            else: 

                                print("""
                                {}.gider
                                {} tarihinde {} tl harcanmıştır.
                                """.format(say,a[0],a[1]))
                                gider += a[1]
                                say += 1
                        print("""Döneme ait toplam gelir {} tl\nDöneme ait toplam gider {} tl\nDöneme ait net bakiye {} tldir.""".format(gelir,gider,gelir-gider))
                        if gelir-gider > 2500:
                            print("bu harika yatırım yapabilirsin")
                        elif gelir-gider < 2500 and gelir-gider > 1000:
                            print("yatırım yapmak için biraz daha çalışman lazım")
                        elif gelir-gider < 1000 and gelir-gider > 0:
                            print("ne eksik ne fazla buda iyi")
                        elif gelir-gider < 0 :
                            print("böyle giderse batacaksın")
            
                        gelir = 0
                        gider = 0
                        say = 1
            elif result == 4 or result =="4":
                gelen = user_islem().tüm_veriler(self.location, self.username)
                if gelen == []:
                    print("kayıtlı bilgi yok")
                else:
                    say = 1
                    for i in gelen:
                        i = list(i)
                        print(f"""{say}.verinin
                        miktar:{i[0]}
                        zaman:{i[1]}
                        dönem:{i[2]}
                        tür:{i[3]}
                        """)
                        say += 1
                    while True:
                        try:
                            inp = input("lütfen silmek istediğniz veri numarasını yazın:")
                            inp = int(inp)
                            if inp > 0 and inp <= say:
                                index = inp - 1
                                print(user_islem().delete_veri(self.location, self.username, index, gelen))
                                break
                            else:
                                print("hatalı değer girdiniz tekrar deneyin arada değil")
                        except:
                            print("hatalı değer girdiniz tekrar deneyin")
                

            elif result == 5 or result =="5":
                print("Ana menüye dönülüyor...")
                break
                
            else:
                print("Yanlış seçim tekrar deneyiniz...")

    


