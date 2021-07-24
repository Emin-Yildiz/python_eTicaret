import sqlite3

import models


class Satici:

    kontrol = 0
    db = sqlite3.connect('MyDb.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS satici (saticiAdi TEXT, sifre TEXT, urunTuru TEXT)")

    saticiAdi = ""
    sifre = ""
    urunTuru = ""

    def __init__(self, saticiAdi, sifre, urunTuru):
        self.sifre = sifre
        self.saticiAdi = saticiAdi
        self.urunTuru = urunTuru



    def saticiKontrol(self, saticiAdi):
        db = sqlite3.connect('MyDb.db')
        cursor = db.cursor()
        command = f"select saticiAdi from satici where saticiAdi='{str(saticiAdi)}'"
        cursor.execute(command)
        isUser = bool(len(cursor.fetchall()))  # 0=False, 1=True
        return isUser

    def saticiKayit(self, satici):

        db = sqlite3.connect("MyDb.db")
        cursor = db.cursor()
        try:
            command = "insert into satici(saticiAdi,sifre,urunTuru) values (?,?,?)"
            cursor.execute(command, (satici.saticiAdi, satici.sifre, satici.urunTuru))
            db.commit()
            print("KAYIT BAŞARILI", "Kayıt tamamlanmıştır.")
            db.close()
        except:
            print("HATA", "Veritabanına kayıt sırasında hata oluştu.")
            db.close()

    def getSatici(self):
        print("Aşağıda satıcılar ve satıcıların hangi türde ürün sattıkları listelenmektedir.")
        db = sqlite3.connect('MyDb.db')
        cursor = db.cursor()
        command = """SELECT saticiAdi, urunTuru FROM Satici"""
        cursor.execute(command)
        i = cursor.fetchall()
        for x in i:
            print(x)

    def saticiGiris(self):
        satici = models.satici.Satici
        kullaniciAdi = (input("Lütfen kullanıcı adınızı giriniz: "))
        uzunluk = len(kullaniciAdi)

        db = sqlite3.connect('MyDb.db')
        cursor = db.cursor()
        command = """SELECT SaticiAdi FROM Satici"""
        cursor.execute(command)
        i = cursor.fetchall()
        for x in i:
            x = str(x)
            x = x[2:uzunluk + 2]
            if (kullaniciAdi == x):
                sifre = (input("Lütfen sifrenizi giriniz: "))
                uzunluk = len(sifre)
                command = """SELECT sifre FROM Satici"""
                cursor.execute(command)
                i = cursor.fetchall()
                for x in i:
                    x = str(x)
                    x = x[2:uzunluk + 2]
                    if (sifre == x):
                        print("Giriş başarılı!!!!!!!")
                        satici.kontrol = 1
                        break
                break
        if(satici.kontrol == 0):
            print("Böyle bir kullanıcı adı bulunmamaktadır. Lütfen sisteme kayıt olun.")



    def saticiEkrani(self):
        print("Satici giriş ekranına hoşgeldiniz!!!!!!!!!!")
        basilanTus = (input("Ürün eklemek için e’ye basınız. Ürün güncellemek için g’ye basınız. Herhangi bir ürünü kaldırmak için d’ye basınız"))
        if(basilanTus == "e"):
            from main import urun
            urunAdi = (input("Lütfen ürün adını giriniz: "))

            urunFiyati = (input("Lütfen ürün fiyatını giriniz: "))

            urunTuru = (input("Lütfen ürün türünüzü giriniz: "))

            urunID = (input("Lütfen ürün ID'nizi giriniz: "))

            urun1 = urun(urunAdi, urunFiyati, urunTuru,urunID)

            urun.urunKayit(urun,urun1)

        elif(basilanTus == "g"):

            urunID = (input("Fiyatını güncellemek istediğiniz ürünün ID'sini giriniz: "))

            yFiyat = (input("Lütfen ürünün yeni fiyatını giriniz: "))

            db = sqlite3.connect('MyDb.db')
            cursor = db.cursor()
            try:
                command = """UPDATE urun SET urunFiyat = ? WHERE urunID = ?"""
                cursor.execute(command, (yFiyat,urunID))
                db.commit()
                print("GÜNCELLEME İŞLEMİ BAŞARILI")
                db.close()
            except:
                print("HATA", "Veritabanında güncelleme sırasında hata oluştu.")
                db.close()

        elif(basilanTus == "d"):

            urunID = (input("Silmek istediğiniz ürünün ID'sini giriniz: "))

            db = sqlite3.connect('MyDb.db')
            cursor = db.cursor()
            try:
                command = """DELETE FROM urun WHERE urunID = ?"""
                cursor.execute(command,(urunID,))
                db.commit()
                print("SİLME İŞLEMİ BAŞARILI")
                db.close()
            except:
                print("HATA", "Veritabanında silme sırasında hata oluştu.")
                db.close()