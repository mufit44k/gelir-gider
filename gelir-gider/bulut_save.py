# buluta kayıt işlemleri

import pymongo
from pymongo import MongoClient
import certifi
ca = certifi.where()
from bson.objectid import ObjectId


class blt_save:
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://Mufit44k:Mufit2015@cluster0.fevhf.mongodb.net/gelir-gider-depo?retryWrites=true&w=majority",tlsCAFile=ca)
        self.db = self.cluster["gelir-gider-depo"]
        self.collection0 = self.db["gelir-gideruser"]
        self.collection = self.db["gelir-giderr"]
        # veritabnındaki kullanıcıya ait verileri alma
    def ortak(self,username):
        result = self.collection.find({"username":username})
        result = list(result)
        if result == []:
            return []
        eklenen = result[0]["eklenen"]
        return eklenen
        # gelir gider bilgisi ekleme
    def insert_gelir_gider(self,gelen,username):
        result = self.collection.find({"username":username})
        print(result)
        result = list(result)
        print(result)
        if result == []:
            self.collection.insert_one({"userid":gelen[0],"username":username,"eklenen":[{"miktar":gelen[1],"zaman":gelen[2],"dönem":gelen[3],"tür":gelen[4]}]})
            print("eklendi")
        else:
            eklenen_list = result[0]["eklenen"]
            print(type(eklenen_list))
            print(eklenen_list)
            eklenecek = {"miktar":gelen[1],"zaman":gelen[2],"dönem":gelen[3],"tür":gelen[4]}
            eklenen_list.append(eklenecek)
            print(eklenen_list)
            self.collection.update_one({"username":username},{"$set":{"userid":gelen[0],"username":username,"eklenen":eklenen_list}})

            print("eklendi")
        # kullnıcı kaydı
    def insert_user(self,gelen):
        self.collection0.insert_one({"username":gelen[0],"sifre":gelen[1],"eposta":gelen[2]})
        # sisteme kayıt yaparken aynı e posta adresi varmı diye kontrol
    def epostakontrol(self,gelen):
        result = self.collection0.find({"eposta":gelen})
        result = list(result)
        if result == []:
            return True
        else:
            return False
        # sisteme kayıt yaparken aynı kullanıcı  ado varmı diye kontrol
    def usernamekontrol(self,gelen):
        result = self.collection0.find({"username":gelen})
        result = list(result)
        if result == []:
            return True
        else:
            return False
        # giriş işlemi
    def login(self,user,sifre):
        result = self.collection0.find({"username":user,"sifre":sifre})
        if len(list(result)) == 0:
            return True
        else:
            return False
        # gerektiği yerlerde kullanabilmek için kullanıcı id bilgisiini alma
    def user_id(self,username):
        result = self.collection0.find({"username":username})
        result = list(result)
        id = result[0]["_id"]
        return id
        # her döneme ait gelir gider bilgilerini alma
    def döenem_durum(self,username):
        eklenen = self.ortak(username)
        if eklenen == []:
            return eklenen
        dönemler = []
        anali = []
        dönemler1 = [] # kullanılacak dönem bilgileri
        for i in eklenen:
            dönem = i["dönem"]
            dönemler.append(dönem)
        for i in dönemler:
            count = dönemler.count(i)
            if count == 1:
                dönemler1.append(i)
            else:
                if count != 1:
                    if i in dönemler1:
                        pass
                    else:
                        dönemler1.append(i)
        self.gelir = []
        self.gider = []
        for i in dönemler1:
            for a in eklenen:
                if a["dönem"] == i and a["tür"] == "gelir":
                    li = [a["zaman"],a["miktar"]]
                    self.gelir.append(li)
                elif a["dönem"] == i and a["tür"] == "gider":
                    li = [a["zaman"],a["miktar"]]
                    self.gider.append(li)
            gelirli = [i,self.gelir,self.gider]
            anali.append(gelirli)
            self.gelir = []
            self.gider = []
        
        return anali
    # veri silme
    def delete(self,username,index):
        eklenen = self.ortak(username)
        eklenen.remove(eklenen[index])
        eklenen_list = eklenen
        gelen = self.user_id(username)
        self.collection.update_one({"username":username},{"$set":{"userid":gelen,"username":username,"eklenen":eklenen_list}})
    # var olan tüm verileri kullanılacak formatta gönderme
    def t_veri(self,username):
        solist = []
        eklenen = self.ortak(username)
        if eklenen == []:
            return []
        for i in eklenen:
            liste = [i["miktar"],i["zaman"],i["dönem"],i["tür"]]
            solist.append(liste)
        return solist
