print("Giriş için 3 deneme hakkınız bulunmaktadır.Lütfen dikkatlice isminizi giriniz.")
count=1
while count < 4:
    ad = input("Ad:")
    soyad = input("Soyad:")
    if ad =='Buse Melek' and soyad=='OLGAÇ':
        print("Hoşgeldiniz {} {}" .format(ad, soyad))
    break

else:

    print('Hatalı bilgi tekrar deneyin.')
    print("{}. denemeniz" .format(count))
    count += 1
    if count == 4:
        print('3 denemeniz de başarısız oldu! Bye!')

dersler={"1:matematik","2:biyoloji","3:fizik","4:kimya","5:teknik çizim","6:yazılım"}
derssayısı=len(dersler)
bilinendersler=[]
print("Listeden en az 3 en fazla 5 ders seçmelisiniz.")
print(dersler)
count=0
while count<5:
    dersseçimi=int(input("Ders seçiminizi yapın 1-6:"))
    if dersseçimi==1:
        if("1:matematik" in bilinendersler):
            print("\n *matematik dersini zaten seçmiştiniz!!!")
            count -= 1
        else:
            bilinendersler.append[dersler(1)]
            print("\n=> {} dersi listeye eklendi!\n".format(dersler[1]))
            print(bilinendersler)
            if dersseçimi==2:
                if("2:biyoloji" in bilinendersler):
                    print("\n *biyoloji dersini zaten seçmiştiniz!!!")
                    count -=1
                else:
                    bilinendersler.append[dersler(2)]
                    print("\n=> {} dersi listeye eklendi!\n".format(dersler[2]))
                    print(bilinendersler)
                    if dersseçimi==3:
                        if("3:fizik"in bilinendersler):
                            print("\n *fizik dersini zaten seçmiştiniz!!!"),
                            count-=1
                        else:
                            bilinendersler.append[dersler(3)]
                            print("\n=> {} dersi listeye eklendi! \n".format(dersler[3]))
                            print(bilinendersler)
                            if dersseçimi==4:
                                if("4:kimya" in bilinendersler):
                                    print("\n *Kimya dersini zaten seçmiştiniz!!!")
                                    count -= 1
                                else:
                                    bilinendersler.append[dersler(4)]
                                    print("\n=> {} dersi listeye eklendi \n".format(dersler[4]))
                                    print(bilinendersler)
                                    if dersseçimi==5:
                                        if("5:teknik çizim"in bilinendersler):
                                            print("\n *teknik çizim dersini zaten seçmiştiniz!!!")
                                            count-=1
                                        else:
                                            bilinendersler.append[dersler(5)]
                                            print("\n=> {} dersi listeye eklendi \n".format(dersler[5]))
                                            print(bilinendersler)
                                            if dersseçimi==6:
                                                if("6:yazılım"in bilinendersler):
                                                    print("\n *yazılım dersini zaten seçmiştiniz!!!")
                                                    count-=1
                                                else:
                                                    bilinendersler.append[dersler(6)]
                                                    print("\n=> {} dersi listeye eklendi \n".format(dersler[6]))
                                                    print(bilinendersler)
vize=input('Vize notunuzu giriniz:')
final=input('Final notunuzu giriniz:')
proje=input("proje notunuzu giriniz:")
ortalamaNot=(0.3*vize)+(0.5*final)+(0.2*proje)
print("Not ortalamanız:",ortalamaNot)
if ortalamaNot>90 :
      print("Harf Notunuz AA")
      if ortalamaNot >70 and ortalamaNot <90 :
          print("Harf notunuz BB")
          if ortalamaNot >50 and ortalamaNot <70 :
              print("Harf notunuz CC")
              if ortalamaNot >30 and ortalamaNot <50 :
                  print("Harf notunuz DD")
                  if ortalamaNot<30:
                      print("Harf notunuz FF.Kaldınız.")










