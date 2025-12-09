# PersonaVision API - Video Yüz Tanıma Sistemi

PersonaVision, video dosyalarında otomatik yüz tanıma için tasarlanmış güçlü bir RESTful API'dir. FastAPI ve Python ile geliştirilmiş olup, yüklenen videoları işleyerek güçlü bilgisayarlı görü kütüphaneleri kullanarak yüzleri tespit eder ve tanır.
   
## 🚀 Özellikler

*   **Video İşleme**: Video yüklemelerini ve kare çıkarmayı verimli bir şekilde gerçekleştirir.
*   **Yüz Tanıma**: Video karelerindeki yüzleri tespit etmek ve tanımlamak için `face_recognition` ve `OpenCV` kullanır.
*   **RESTful API**: Kolay entegrasyon için temiz ve dokümante edilmiş API uç noktası sağlar.
*   **Docker Desteği**: Kolay dağıtım için Docker ve Docker Compose ile tamamen konteynerleştirilmiş uygulama.
*   **Veritabanı Entegrasyonu**: Tanıma verilerini depolamak için PostgreSQL entegrasyonu içerir.

## 🛠️ Teknoloji Yığını

*   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
*   **Programlama Dili**: Python 3.9+
*   **Bilgisayarlı Görü**: `face_recognition`, `opencv-python-headless`
*   **Veritabanı**: PostgreSQL (`psycopg2-binary`)
*   **Konteynerleştirme**: Docker, Docker Compose

## 📂 Proje Yapısı

```
.
├── src/
│   ├── controller/       # API rota işleyicileri
│   ├── service/          # İş mantığı (Tanıma, Veritabanı)
│   └── utils/            # Yardımcı fonksiyonlar
├── main.py               # Uygulama giriş noktası
├── Dockerfile            # Docker derleme talimatları
├── docker-compose.yml    # Docker servis yapılandırması
├── init.sql              # Veritabanı başlatma betiği
└── requirements.txt      # Python bağımlılıkları
```

## ⚡ Kurulum ve Yapılandırma

### Seçenek 1: Docker Kullanarak (Önerilen)

1.  **Depoyu klonlayın:**
    ```bash
    git clone <repo-url>
    cd videoarchive-facerecognation-main
    ```

2.  **Konteynerleri derleyin ve çalıştırın:**
    ```bash
    docker-compose up --build
    ```

3.  API `http://localhost:8000` adresinden erişilebilir olacaktır.

### Seçenek 2: Yerel Kurulum

1.  **Ön Gereksinimler:**
    *   Python 3.8+
    *   CMake (`face_recognition` kütüphanesi için gerekli)

2.  **Sanal ortam oluşturun:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows için: venv\Scripts\activate
    ```

3.  **Bağımlılıkları yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Uygulamayı çalıştırın:**
    ```bash
    uvicorn main:app --reload
    ```

## 📖 API Dokümantasyonu

Uygulama çalıştıktan sonra, interaktif API dokümantasyonuna (Swagger UI) şu adresten erişebilirsiniz:

*   **URL**: `http://localhost:8000/docs`

### Uç Noktalar

*   `POST /api/v1/recognition/`: Yüz tanıma işlemi gerçekleştirmek için bir video dosyası yükleyin.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen Pull Request göndermekten çekinmeyin.

## 📄 Lisans

[MIT Lisansı](LICENSE)
