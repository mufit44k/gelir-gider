# giriş yapıldıktan sonra yapılan işlemler 
# her iki veri tabanı içinde yapılan işlemler için fonksiyonlar ortak

import time
from datetime import datetime
import local_save
from bulut_save import blt_save

class user_islem:
    def __init__(self):
        self.zaman = datetime.now()
        self.yıl = str(datetime.now().year)
        self.ay = str(datetime.now().month)
        self.gönderilecek = []
        # veri tabanına veri ekleme
    def gelir_gider(self,user_id,miktar,tür,save_location,username):
        self.username = username
        self.gönderilecek = []
        self.tür = tür
        self.user_id = user_id
        self.miktar = miktar
        self.gönderilecek.append(self.user_id)
        self.gönderilecek.append(self.miktar)
        self.gönderilecek.append(self.zaman)
        self.gönderilecek.append(self.yıl + "-" + self.ay)
        self.gönderilecek.append(self.tür)
        if save_location == "local":
            local_save.local_save().ekle(tuple(self.gönderilecek))
        else:
            blt_save().insert_gelir_gider(self.gönderilecek,self.username)
        # veri tabanındaki verileri görüntüleme
    def dönem_durum(self,save_location,username):
        if save_location == "local":

            self.gelen_list = local_save.local_save().güncel_dönem()
        else:
            self.gelen_list = blt_save().döenem_durum(username)
        return self.gelen_list
        # veri tabnındaki tüm verileri alma
    def tüm_veriler(self,save_location,username):
        if save_location == "local":
    
            self.g_l = local_save.local_save().tüm_veri()
        else:
            self.g_l = blt_save().t_veri(username)
        return self.g_l
        # veri silme
    def delete_veri(self,save_location,username,index,liste):
        if save_location == "local":
            local_save.local_save().delete(index, liste)
            return "silindi"
        else:
            blt_save().delete(username,index)
            return "silindi"
