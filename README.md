# BlogApp Web Sitesi

BlogApp, kullanıcıların blogları görüntülemesine, eklemesine, düzenlemesine ve yorum yapmasına olanak tanıyan kapsamlı bir web sitesidir. Ayrıca, kategori seçimi, admin girişi, resim ekleme, profil resmi ekleme, şifre değiştirme, kayıt olma, blog arama ve daha birçok özelliği içermektedir.

## Başlangıç

Projeyi yerel bir ortamda başlatmak için aşağıdaki adımları izleyin:

### Gereksinimler

Projeyi başlatmak için aşağıdaki gereksinimlere ihtiyacınız vardır:

- Python 3.x
- Django
- Diğer bağımlılıklar (requirements.txt)

Gereksinimleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install -r requirements.txt
```
## Kurulum
Projeyi klonlayın:

```bash
git clone https://github.com/korayyalcin1903/django-blogapp
```

### Proje dizinine gidin:

```bash
cd blogapp
```

### Virtual environment (sanal ortam) oluşturun ve etkinleştirin:

```bash
python -m venv venv
source venv/bin/activate
```

### Gereksinimleri yükleyin:

```bash
pip install -r requirements.txt
```

### Veritabanı oluşturun:
```bash
python manage.py migrate
```

### Admin kullanıcısı oluşturun:
```bash
python manage.py createsuperuser
```

### Projeyi başlatın
```bash
python manage.py runserver
```

## Kullanım
- Blogları görüntülemek için ana sayfayı ziyaret edin.
- Blog eklemek ve düzenlemek için giriş yapın ve profilinizin altında settings linkine tıklayın.
- Yorum yapmak için bir blog gönderisini görüntüleyin ve yorum bölümünü kullanın.
- Kategori seçimi, profil resmi ekleme, şifre değiştirme ve kayıt olma gibi işlemleri profil sayfanızdan gerçekleştirebilirsiniz.
- Admin girişi ile blogları ekleyebilir, düzenleyebilir ve silebilirsiniz.
- Blog arama işlevini kullanarak belirli bir blog gönderisini bulabilirsiniz.
## Katkıda Bulunma
Eğer projeye katkıda bulunmak istiyorsanız, lütfen bir pull request göndermeden önce iletişime geçin ve geliştirme süreci hakkında bilgi alın.

## Lisans
Bu proje [Lisans Adı] altında lisanslanmıştır. Lisans detayları için [Lisans Dosyası] dosyasını inceleyebilirsiniz.

## İletişim
Proje ile ilgili sorularınız veya geri bildirimleriniz için aşağıdaki iletişim bilgilerini kullanabilirsiniz:

- E-posta: korayyalcin1903@gmail.com

## Görseller
### Index
![127 0 0 1_8000_ (1) (Orta)](https://github.com/korayyalcin1903/django-blogapp/assets/92126235/fbe90472-d288-4028-b320-6387a1ea5e86)
### Blogs
![127 0 0 1_8000_blogs (Orta)](https://github.com/korayyalcin1903/django-blogapp/assets/92126235/29c470cd-b53b-489c-8e70-36515a93b34e)
### Blog Details and Comment
![127 0 0 1_8000_blogs_abd-ordusu-ve-microsoft-arasndaki-anlasma-buyuyor (Orta)](https://github.com/korayyalcin1903/django-blogapp/assets/92126235/98101872-5d70-4921-8346-c27d2c962af1)
### Account/Profile
![127 0 0 1_8000_account_profile (Orta)](https://github.com/korayyalcin1903/django-blogapp/assets/92126235/dc6f7d19-0ad2-4527-8f50-bdc21dede6b0)

