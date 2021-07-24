import sqlite3

import models
from models import sepet

sepet = models.sepet.Sepet

class Musteri:
    db = sqlite3.connect('MyDb.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS musteri (musteriAdi TEXT, sifre TEXT)")

    musteriAdi = ""
    sifre = ""
    kontrol = 0
    kayitKontrol = 1


    def __init__(self, musteriAdi, sifre):
        self.sifre = sifre
        self.musteriAdi = musteriAdi


    def musteriKontrol(self, musteriAdi):  # database de, bu kullanıci adı varsa True yoksa False Dndürür
        #bunu satici giriş yaparken kullanacaz.
        db = sqlite3.connect('MyDb.db')
        cursor = db.cursor()
        command = f"select musteriAdi from musteri where saticiAdi='{str(musteriAdi)}'"
        cursor.execute(command)
        isUser = bool(len(cursor.fetchall()))  # 0=False, 1=True
        return isUser


    def musteriKayit(self, musteri):

        db = sqlite3.connect("MyDb.db")
        cursor = db.cursor()
        try:
            command = "insert into musteri(musteriAdi,sifre) values (?,?)"
            cursor.execute(command, (musteri.musteriAdi, musteri.sifre))
            db.commit()
            print("KAYIT BAŞARILI", "Kayıt tamamlanmıştır.")
            db.close()
        except:
            print("HATA", "Veritabanına kayıt sırasında hata oluştu.")
            musteri.kayitKontrol == 0
            db.close()


    def musteriGiris(self):
        kullaniciAdi = (input("Lütfen kullanıcı adınızı giriniz: "))
        uzunluk = len(kullaniciAdi)

        db = sqlite3.connect('MyDb.db')
        cursor = db.cursor()
        command = """SELECT musteriAdi FROM Musteri"""
        cursor.execute(command)
        i = cursor.fetchall()
        y = len(i)
        z = 0
        for x in i:
            z = z +1
            x = str(x)
            x = x[2:uzunluk+2]
            if(kullaniciAdi == x):
                sifre = (input("Lütfen sifrenizi giriniz: ")).ap
                uzunluk = len(sifre)
                command = """SELECT sifre FROM Musteri"""
                cursor.execute(command)
                i = cursor.fetchall()
                for x in i:
                    x = str(x)
                    x = x[2:uzunluk + 2]
                    if (sifre == x):
                        print("Giriş başarılı!!!!!!!")
                        from main import musteri
                        musteri.kontrol = 1
                        break
                break
            elif(y == z):
                print("Böyle bir kullanıcı adı bulunmamaktadır. Lütfen sisteme kayıt olun.")
                break



    def musteriEkrani(self):
        urun = models.urun.Urun
        print("Müşteri giriş ekranına hoşgeldiniz!!!!!!!!!!!!!!!!!")
        urun.getUrun(urun)
        urun.getSeciliUrun(urun)
        print()

        # burda hangi Id girildiyse o IDye ait ürün sepete kelnicek ama veritabanından.