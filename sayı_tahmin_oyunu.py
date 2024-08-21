# -*- coding: utf-8 -*-
"""Sayı_Tahmin_Oyunu.py

Ödev: Basit Bir Oyun Simülasyonu

Görev:
Küçük bir sayı tahmin oyunu yapacaksın.
Bilgisayar rastgele bir sayı üretecek ve kullanıcı bu sayıyı tahmin etmeye çalışacak.
Kullanıcı doğru tahmini yapana kadar döngü devam edecek.

Adımlar:

1. Rastgele Sayı Üret:  
   - 1 ile 100 arasında rastgele bir sayı üretmek için `random` kütüphanesini kullan.
  
2. Kullanıcıdan Girdi Al:  
   - Kullanıcıdan 1 ile 100 arasında bir sayı tahmin etmesini iste.
  
3. Koşulları Kullan:  
   - Eğer kullanıcı tahmini doğruysa, oyunu bitir ve kullanıcıyı tebrik et.
   - Eğer kullanıcı tahmini düşükse, "Daha büyük bir sayı deneyin." mesajı ver.
   - Eğer kullanıcı tahmini yüksekse, "Daha küçük bir sayı deneyin." mesajı ver.
  
4. Döngü:  
   - Kullanıcı doğru tahmini yapana kadar oyunu tekrarla.

5. Oyunu Geliştir:  
   - Kullanıcıya kaç deneme yaptığını söyle.
   - Oyunu birden fazla oynanabilir yap ve her oyunun sonunda kullanıcıya tekrar oynamak isteyip istemediğini sor.
"""

import random


def tahmin_oyunu():
    print("Tahmin oyununa hoş geldiniz!")
    print("Bu oyunda bilgisayar 1-100 arasında bir sayı tahmininde bulunur.")
    print("Oyuncu doğru tahmini yapana kadar oyun devam eder.")
    print("Bilgisayar oyuncunun tahminleri için ipucu verir.")
    print("Tahmin küçükse, daha büyük bir sayı tahmin edilmelidir.")
    print("Tahmin büyükse, daha küçük bir sayı tahmin edilmelidir.")

    bilgisayar = random.randint(1, 100)
    tahmin_sayisi = 0

    while True:
        oyunkurucu = int(input("\nTahmin için 1-100 arasında bir sayı girin: "))
        tahmin_sayisi += 1

        if oyunkurucu < 1 or oyunkurucu > 100:
          print("\nGeçersiz sayı girildi. Lütfen aralıktaki sayılar ile tekrar deneyin.")
        elif bilgisayar == oyunkurucu:
          print(f"\nDoğru tahmin ettiniz! {tahmin_sayisi} denemede bulup oyunu kazandınız!")
          tekrar = input("\nTekrar oynamak ister misin? Evet/Hayır: ")
          if tekrar == "Evet":
              print("\nYeni oyun başlatılıyor...\n")
              tahmin_sayisi = 0
              bilgisayar = random.randint(1, 100)
          else:
              print("\nOyun sonlandırılıyor...")
              return
        elif bilgisayar < oyunkurucu:
          print("\nDaha küçük bir sayı denemelisiniz!")
        elif bilgisayar > oyunkurucu:
          print("\nDaha büyük bir sayı denemelisiniz!")


tahmin_oyunu()
