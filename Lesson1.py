print("Hello World")

a = 5
b = 3
c = a * b

"""Veri Bilimi için Python Programlama eğitimine hoş geldiniz!
Eğitim tamamlanınca aşağıdaki konularda bilgi edineceğim.
-Çalışma Ortamı Ayarları
-Veri Yapıları
-Fonksiyonlar 
-Koşullar 
-Döngüler 
-Comprehension
-Python ile Veri Analizi

*Anaconda Nedir: Python kullanmak istediğimizde tercih edebileceğimiz bazı arayüzleri bize bir arada sunan bir araçtır.
*Pycharm nedir: Büyük ölçekli projeler geliştirebilmek için pro düzeyde bir Python geliştirme ortamıdır. Jupiter notebook, spyder, jupyterlab, vs code gibi diğer bir çok araç ile de geliştirilebilir.
*Virtual Environment Nedir: Projelerin birbirinden izole bir şekilde çalıştırılabilmesiniçin kullanılan bir araçtır.
*Anaconda’nın sağlamış olduğu base environment adı verilen sanal ortamı seçerek içinde sık kullanılan veri bilimi, makine öğrenmesi kütüphaneleri modülleri yüklü olduğu için kolayca işlemlere başlayabiliriz.
*Aşağı taraftaki terminal bölümü işletim sistemiyle olacak olan konuşmalarda yazılan kodların komutların gönderildiği bölümdür. Buradan kolayca işletim sistemine ilişkin kodlar yazılabilir.

	print("Hello World") >> RUN

**Sayılar(Numbers) ve Karakter Dizileri(Strings)**
Sayı 9 gibi rakamlardan oluşur. Python’da kullanılan 3 tip sayı vardır:
	1-Integer: 9, 111, 100000 gibi
	print(9) >> RUN
	9
	2-Float: Ondalıklı sayısal bir ifadedir.
	print
	3-Kompleks sayılar: Çok yaygın kullanılmaz.
String ise “” arasında gösterilen ifadelerde kullanılır.
"""
"""---------------------------------------------------------------------"""
"""Sanal Ortam(Virtual Environment)
*İzole çalışma ortamları oluşturmak için kullanılan araçlardır.
*Farklı çalışmalar için oluşabilecek farklı kütüphane ve versiyon ihtiyaçlarını 
çalışmalar birbirini etkilemeyecek şekilde oluşturma imkanı sağlar.

Örn: Proje 1: Python 3.7; Numpy 1.16; Pandas 1.1
     Proje 2: Python 2.7; Numpy 1.14; Pandas 0.14
Bu iki projeyi aynı anda sanal ortam aracılığı ile gerçekleştirebiliriz.

-----------------------------------------------------------------------
***Paket Yönetimi(Package Management)***
Paket=Modül=Kütüphane Yönetimi şeklinde bilinir.

Paket Yönetim Araçları:
    1-pip(requirements.txt)
    2-pipenv(Pipfile)
    3-Conda(environment.yaml) !Conda hem sanal ortam yöneticisi hem de bir paket yöneticisidir.
    
-Bu araçlar python dışındaki paketleri indirme, kurma, güncelleme gibi işlevleri yerine getirir.
Bağımlılık yönetimi dependency management yaparlar.

-Sanal ortamlar ile paket yönetim araçlarının ilişkisi nedir?

*pip ile conda arasında ne fark vardır?
conda: package management ve virtual environment yönetimi için kullanılabilir.
pip: paket yönetimi için kullanılabilir.

---------------------------------------------------------------------------
UYGULAMA: SANAL ORTAM VE PAKET YÖNETİMİ

-Pycharm bize hem pythonla çalışmak hem de işletim sistemimiz ile çalışmak için alanlar sağlamıştır.
-Terminal komut satırı bölümünde yazılan komutlar işletim sistemini ilgilendirir.
-Bilgisayardaki sanal ortamların listelenmesi için:
    conda env list >> Komtutu kullanılır.
    
**Sanal Ortam Oluşturma:
    conda create -n myenv >> RUN şeklinde oluşturulur. Bu şekilde istenilen isim ile bir sanal ortam oluşturulur.
-Bu ortamı aktif edebilmek için 
    conda activate myenv >> kodunu kullanmamız gerekiyor.

-conda list >> dersek sanal ortamda hangi kütüphaneler var onu görürüz.

-base olan sanal ortamamızda bir sürü küyüphane var ama kendi oluşturduğumuz myenv sanal ortamımızda hiçbir kütüphane yok.

-Bir sanal ortama paket yüklemek istediğimizde ya da ya da çalışılan ortama
ekstra paket yükletilmek istenirse 
    conda install (istenilen kütüphane)>> RUN ifadesi kullanılır.
    conda install numpy
Burada sadece numpy değil diğer gerekli kütüphaneleri de bağımlı olarak indiriyor örneğin python veya pip gibi.

-Aynı anda 1'den fazla paket yüklemek istiyorsak ne yapabiliriz?
Aralarında sadece 1 boşluk bırakarak 3 veya daha fazla kütüphaneyi yükleyebiliriz.
    conda install scipy pandas 

-Belirli bir proje için özel bir numpy versiyonu kullanmak istersek:
Önce var olan paketi silelim bunun için:
    conda remove (paketin ismi)
    conda remove numpy
Burada silinirken nasıl yüklenirken beraberinde başka paketleri de yüklediyse
silerken de onları da siliyor. Silinirken versiyon numarasını görebiliriz.
numpy-1.26.4 bu silinen versiyondu. Bir önceki sürüm olan numpy-1.26.3
indirelim. Bunun için 
    conda install numpy=1.26.3 >> Run 
    
!!!Conda da tek eşittir kullanılır; pip'te 2 tane eşittir kullanılır!!!

Kütüphanemize 1.26.3 versiyonu eklendi mi diye kontrol edelim.
    conda list
Eklenmiş :)

-Yeni versiyona(1.26.4) tekrar nasıl geçeriz? 2 seçenek var:
    1-Baştan kurulum yapmak
    2-Upgrade ifadesi kullanılır.
    conda upgrade numpy >> RUN ile son versiyona geçiş yapılır.

-Çalışma kitabımızdaki bütün kütüphaneleri güncellemek istersek:
    conda upgrade -all >> RUN kullanabiliriz bir de pip(python package index) kullanabiliriz.
    pip install paket_adı
    pip install pandas

-pip ile versiyona göre paket yükleme:
    pip install pandas==2.2.1  
!!!Pip'te 2 eşittir kullanılıyordu!!!
!!!Paket yönetim aracı Pip, biz bir önceki versiyonu istediğimiz için onu
indirip diğer versiyonu otomatik olarak sildi. Conda'da bunu manuel olarak yapıyorduk.

-Çalışılan kütüphaneleri başka kişilere aktarmak için
    requirements.txt dosyası (pip dünyasında yaygındır) ya da
    yaml file(conda tarafında yaygındır) oluşturma ile gerçekleşir.
    conda env export > environment.yaml >> RUN

Dosyaları listelemek için dir(Windowsta dir, Mac'te ls) komutu kullanılır.
Daha sonra
    Project >> MiuuIPython >> altına environment.yaml dosyasının gelmiş olduğunu görüyoru<.

Bu dosyaya çift tıklanırsa sanal ortamdaki tüm kütüphaneleri gösterir.

-Var olan sanal ortamı tamamen silmek için:
    conda env remove -n myenv >> RUN

-Paketlerin versiyonlarını barındıran bir dosyayı kullanarak sıfırdan
aynı sanal ortamı oluşturmak için:
    conda env create -f environment.yaml >> RUN
Daha sonra sanal ortamı aktifleştir:
    conda activate myenv >> RUN

--------------------------------------------------

QUIZ:
1-İzole çalışma ortamları için kullanılan ortam = Virtual Environment
2-Paket yükseltmesi için kullanılan=conda upgrade
3-Hangi komut bilgisayarınızdaki sanal ortamı oluşturmak için kullanılır?=conda create
4-Hem sanal ortam oluşturabileceğimiz hem de paket indirme paket güncelleme paket silme gibi paketleri de(Paket yönetimi yani) ilgilendiren işlemleri yapabilmemizi sağlayan nedir?=conda
5-Sanal ortam araçlarından biri değildir=pip

"""