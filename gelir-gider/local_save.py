# yerel veritabanı işlemleri

import sqlite3 as s

class local_save:
    def __init__(self):
        self.user_id = 1
        self.connect = s.connect("local_database.db")
        self.im = self.connect.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS gelir_gider (user_id,miktar,zaman,dönem,tür)"
        self.im.execute(sorgu)
        self.ana_list = []

    def ekle(self,veri):
        sorgu = """INSERT INTO gelir_gider VALUES (?,?,?,?,?)"""
        self.im.execute(sorgu,veri)
        self.connect.commit()
        print("eklendi")
    def güncel_dönem(self):

        sorgu_all_dönem = """SELECT dönem FROM gelir_gider"""
        self.all_dönem = self.im.execute(sorgu_all_dönem).fetchall()
        if self.all_dönem == []:
            return []
        self.teklist = []
        self.count = []
        for i in self.all_dönem:
            self.teklist.append(list(i)[0])
        for i in self.teklist:
            count = self.teklist.count(i)
            if count == 1:
                self.count.append(i)
            elif count != 1:
                if i in self.count:
                    pass
                else:
                    self.count.append(i)
        sorgu = """SELECT zaman,miktar FROM gelir_gider WHERE dönem = ? AND tür = ? """
        # dönem gelir bilgisi
        self.gelir = []
        self.gider = []
        for i in self.count:
            self.gelir_dönem = self.im.execute(sorgu,(i,"gelir")).fetchall()
            self.gelir = self.gelir_dönem
            self.gider_dönem = self.im.execute(sorgu,(i,"gider")).fetchall()
            self.gider = self.gider_dönem
            self.liste_tüm = [i,self.gelir,self.gider]
            self.ana_list.append(self.liste_tüm)

        return self.ana_list
    def delete(self,index,liste):
        sorgu = "DELETE FROM gelir_gider WHERE miktar = ? AND zaman = ? AND dönem = ? AND tür = ?"
        self.im.execute(sorgu,(liste[index]))
        self.connect.commit()
    def tüm_veri(self):
        sorgu_all_dönem = """SELECT miktar,zaman,dönem,tür FROM gelir_gider"""
        self.alllist = self.im.execute(sorgu_all_dönem).fetchall()
        return self.alllist
# a = local_save()
# a.ekle((user_id,"miktar","zaman","2022-3","gelir"))