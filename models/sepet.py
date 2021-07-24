import sqlite3

import models

class Sepet:

    sepetList = []
    sepetFiyat = 0
    kontrol = 1

    def __init__(self):
        self

    def sepeteEkle(self):#urunID geliyor
        sepet = models.sepet.Sepet
        urun = models.urun.Urun

        while(sepet.kontrol):
            urun.getSeciliUrunList(urun)
            basilanTus = input("Sepete daha fazla ürün eklemek istiyor musunuz?(Evet ise 'y', hayır ise 'n' ye tıklayın.)")
            if(basilanTus == 'n'):
                sepet.sepetOnay(sepet)
                sepet.kontrol = 0

    def sepetOnay(self):
        sepet = models.sepet.Sepet

        print()
        print("Ürün ismi   Ürün Fiyatı")
        print("---------   -----------")
        for x in sepet.sepetList:
            print("  ",x.urunAdi,",    ", x.urunFiyat)
        print()
        print("Sepetinizin tutarı: ", sepet.sepetFiyat)
        print()
        basilanTus = input("Sepetinizi onaylamak istiyor musunuz? Evet ise 'y', hayır ise 'n' ye tıklayın.)")
        if(basilanTus == 'y'):
            print("Sepetiniz onaylanmıştır bizi tercih ettiğiniz için teşekkür ederiz.!!!!!!!!!")
        else:
            print("Sistemden çıkış yapılıyor!!!!!!!!!!!!!!!!!!!!")
