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
    3-Conda(environment.yaml) !Conda hem sanal ortam yöneticisi hem de bir paket yöneticisi 
"""