
import models.satici

from models.musteri import Musteri
from models.urun import Urun

basilanTus = ""
musteri = models.musteri.Musteri
satici = models.satici.Satici
urun = models.urun.Urun

def saticiSistemKayit():
    saticiAdi = (input(
        "Lütfen kullanıcı adınızı giriniz: "))  # bundan sonra veritabanında kullanici adını kontrolü yapıcak sonra şifre.

    sifre = (input(
        "Lütfen sifre giriniz: "))  # bundan sonra veritabanında kullanici adını kontrolü yapıcak sonra şifre.

    urunTuru = (input(
        "Lütfen urun turu giriniz: "))  # bundan sonra veritabanında kullanici adını kontrolü yapıcak sonra şifre.

    satici1 = satici(saticiAdi, sifre, urunTuru)
    satici.saticiKayit(satici, satici1)
    satici.saticiEkrani(satici)


def musteriSistemKayit():
    musteriAdi = (input(
        "Lütfen kullanıcı adınızı giriniz: "))  # bundan sonra veritabanında kullanici adını kontrolü yapıcak sonra şifre.

    sifre = (input(
        "Lütfen sifre giriniz: "))  # bundan sonra veritabanında kullanici adını kontrolü yapıcak sonra şifre.


    musteri1 = musteri(musteriAdi, sifre)
    musteri.musteriKayit(musteri, musteri1)
    if(musteri.kayitKontrol == 1):
        musteri.musteriEkrani(musteri)

def kullaniciGiris():
    basilanTus = (input("Müşteri misiniz, Satıcı mısınız? (Müşteri iseniz 'y' , Satıcı iseniz 'n')"))

    if(basilanTus == "y"):

        musteri.musteriGiris(musteri)
        if(musteri.kontrol == 1):
            musteri.musteriEkrani(musteri)

    else:

        satici.saticiGiris(satici)
        if(satici.kontrol == 1):
            satici.saticiEkrani(satici)

def urunEkleme():
    urunAdi = (input("Lütfen ürün adını giriniz: "))

    urunFiyat = (input("Lütfen ürün fiyatını giriniz: "))

    urunTuru = (input("Lütfen ürün türünüzü giriniz: "))

    urunID = (input("Lütfen ürün ID'nizi giriniz: "))

    urun1 = urun(urunAdi, urunFiyat, urunTuru, urunID)

    urun.urunKayit(urun, urun1)


if __name__ == '__main__':

    basilanTus = (input("E-ticaret uygulamasına hoşgeldiniz!!!!!!! \nSisteme kayıtlı mısınız?(Evet ise 'y', hayır ise 'n' tuşuna basınız)"))
    if(basilanTus == "y"):
        kullaniciGiris()
    else:
        basilanTus = (input("Müşterimi yoksa satıcı mısınız?(Satıcı ise 'y' müşteri ise 'n'ye basınız"))
        if(basilanTus == "y"):
            saticiSistemKayit()
        elif(basilanTus == "n"):
            musteriSistemKayit()