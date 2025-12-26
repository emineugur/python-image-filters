# Python Image Filters (Streamlit)

Bu proje, Python kullanılarak geliştirilen Streamlit tabanlı bir görüntü işleme uygulamasıdır.
Uygulama üzerinden kullanıcılar bilgisayarlarından bir görüntü yükleyerek,
görüntüyü gri (grayscale) formata dönüştürebilir ve farklı filtreleme işlemleri uygulayabilir.
Filtre yoğunluğu ayarlanabilir ve elde edilen sonuç indirilebilir.

Projede amaç, Python ile görüntü işleme mantığını uygulamalı olarak öğrenmek ve
basit bir web arayüzü üzerinden kullanıcı etkileşimi sağlamaktır.

Uygulama Python 3 ile geliştirilmiştir ve Streamlit kütüphanesi kullanılarak
web tabanlı bir arayüz oluşturulmuştur. Görüntü işleme işlemleri için OpenCV,
sayısal işlemler için NumPy ve görüntü dosyalarının okunup dönüştürülmesi için
Pillow (PIL) kütüphanesi kullanılmıştır.

Projeyi kendi bilgisayarında çalıştırmak isteyen kullanıcılar için bağımlılıkların
sistemi etkilememesi amacıyla sanal ortam (venv) kullanılması önerilmektedir.
Sanal ortam oluşturmak ve gerekli paketleri yüklemek için aşağıdaki adımlar izlenebilir:

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  

Kurulum tamamlandıktan sonra uygulama aşağıdaki komut ile çalıştırılır:

streamlit run app.py  

Uygulama çalıştırıldığında tarayıcı üzerinden açılır ve kullanıcıdan bir görüntü
yüklemesi istenir. Seçilen işleme göre görüntü gri formata dönüştürülür,
filtre uygulanır ve sonuç kullanıcıya gösterilir.

Proje dosya yapısı aşağıdaki gibidir:

python-image-filters/  
│── app.py  
│── requirements.txt  
│── .gitignore  
│── README.md  

Bu projede sanal ortam klasörü (venv) GitHub deposuna eklenmemiştir.
Bunun yerine gerekli tüm bağımlılıklar requirements.txt dosyasında belirtilmiştir.
Bu yaklaşım Python projelerinde standart ve önerilen bir yöntemdir.

Proje açık kaynak olarak paylaşılmıştır ve MIT lisansı ile lisanslanmıştır.
