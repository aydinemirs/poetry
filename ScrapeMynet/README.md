ScrapeMynet
- ScrapeMynet, Mynet finans sayfasından borsa verilerini çekmek için kullanılan bir Python uygulamasıdır.

Kurulum ve Başlatma
- Bu rehber, projeyi nasıl kuracağınızı ve çalıştıracağınızı adım adım anlatmaktadır.

Gereksinimler
- Python 3.8 veya üstü
- Poetry

### Adım1:(images1.png) Projeyi Klonla:
- Komut istemcisini açıp Github'daki projeyi önce kendi pc mize klonluyoruz.

git clone  https://github.com/aydinemirs/poetry.git ScrapeMynet

### Adım2:(images2.png) Poetry ile Bağımlılıkları Kur:
- Poetry'yi kullanarak gerekli bağımlılıkları yükleyin.

poetry install

### Adım3:(images3.png) Projeyi Çalıştır:
- cd ScrapeMynet
- dir C:\Users\ArdaAydin\ScrapeMynet\src\ScrapeMynet (Sizin dosyanız bilgisayarınızda nerdeyse kodu ona uyarlamanız gerek bu sadece bir örnek.)
- poetry run python src/ScrapeMynet/main.py