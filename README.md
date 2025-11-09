# 🎬 Modern Video Dönüştürücü Kullanım Talimatları

Bu program, elinizdeki videoları (MP4, MKV, MOV vb.) varsayılan olarak WhatsApp'ta sorunsuz paylaşılabilen standart bir formata (**H.264 + AAC**) dönüştürmenizi sağlar.

Ayrıca, **özel FFmpeg parametreleri** girerek kendi gelişmiş dönüştürme ayarlarınızı uygulamanıza da olanak tanır.

---

## 🧩 1. Zorunlu Kurulum (Sadece 1 Kez Yapılacak)

Programınızın video dönüştürme işlemini yapabilmesi için `ffmpeg` adında ücretsiz bir "motor" dosyasına ihtiyacı vardır. Kurulumu çok basittir.

**✅ En Kolay Yöntem (Tavsiye Edilen):**

1.  Web tarayıcınızı açın ve şu adrese gidin:
    👉 [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

2.  Sayfada biraz aşağı inin ve **"Release builds"** bölümünü bulun.
    `ffmpeg-release-full.7z` (veya `.zip`) yazan linke tıklayarak dosyayı indirin.

3.  İndirdiğiniz `.7z` (veya `.zip`) dosyasını bir klasöre çıkartın.
    (WinRAR, 7-Zip veya Windows'un kendi "Çıkart" özelliğini kullanabilirsiniz.)

4.  Oluşan `ffmpeg-...-full` klasörünün içine girin.

5.  Orada bir **`bin`** klasörü göreceksiniz, onun da içine girin.

6.  `bin` klasörünün içinde bir sürü dosya göreceksiniz.
    Bize sadece **`ffmpeg.exe`** dosyası lazım.

7.  Bu **`ffmpeg.exe`** dosyasını kopyalayın.

8.  Size gönderilen `VideoDonusturucu.exe` (bu program) dosyasının bulunduğu klasöre geri dönün ve
    `ffmpeg.exe` dosyasını **tam yanına** yapıştırın.

---
Elbette, GitHub ile tam uyumlu Markdown (.md) formatındaki dosya içeriği aşağıdadır. Bunu kopyalayıp doğrudan `README.md` dosyanıza yapıştırabilirsiniz.

```markdown
# 🎬 Modern Video Dönüştürücü Kullanım Talimatları

Bu program, elinizdeki videoları (MP4, MKV, MOV vb.) varsayılan olarak WhatsApp'ta sorunsuz paylaşılabilen standart bir formata (**H.264 + AAC**) dönüştürmenizi sağlar.

Ayrıca, **özel FFmpeg parametreleri** girerek kendi gelişmiş dönüştürme ayarlarınızı uygulamanıza da olanak tanır.

---

## 🧩 1. Zorunlu Kurulum (Sadece 1 Kez Yapılacak)

Programınızın video dönüştürme işlemini yapabilmesi için `ffmpeg` adında ücretsiz bir "motor" dosyasına ihtiyacı vardır. Kurulumu çok basittir.

**✅ En Kolay Yöntem (Tavsiye Edilen):**

1.  Web tarayıcınızı açın ve şu adrese gidin:
    👉 [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

2.  Sayfada biraz aşağı inin ve **"Release builds"** bölümünü bulun.
    `ffmpeg-release-full.7z` (veya `.zip`) yazan linke tıklayarak dosyayı indirin.

3.  İndirdiğiniz `.7z` (veya `.zip`) dosyasını bir klasöre çıkartın.
    (WinRAR, 7-Zip veya Windows'un kendi "Çıkart" özelliğini kullanabilirsiniz.)

4.  Oluşan `ffmpeg-...-full` klasörünün içine girin.

5.  Orada bir **`bin`** klasörü göreceksiniz, onun da içine girin.

6.  `bin` klasörünün içinde bir sürü dosya göreceksiniz.
    Bize sadece **`ffmpeg.exe`** dosyası lazım.

7.  Bu **`ffmpeg.exe`** dosyasını kopyalayın.

8.  Size gönderilen `VideoDonusturucu.exe` (bu program) dosyasının bulunduğu klasöre geri dönün ve
    `ffmpeg.exe` dosyasını **tam yanına** yapıştırın.

---
📁 **Klasör yapısı doğruysa şu şekilde görünmelidir:**

```

Video\_Donusturucu\_Klasoru/
│
├── VideoDonusturucu.exe   \<-- Sizin programınız
│
└── ffmpeg.exe             \<-- Yanına kopyaladığınız motor dosyası

```

Artık programı kullanmaya hazırsınız 🎉
`ffmpeg.exe` o klasörde olduğu sürece programınız çalışacaktır.

---

## ▶️ 2. Programın Kullanımı

1.  **`VideoDonusturucu.exe`** dosyasına çift tıklayarak programı çalıştırın.

2.  **Adım 1: Dosyaları Seçin**
    * **Dosya Seçme:**
        * **Yöntem A (Sürükle-Bırak):** Dönüştürmek istediğiniz video dosyasını programın üstündeki “Video Dosyasını Buraya Sürükleyin veya Tıklayın” alanına sürükleyin.
        * **Yöntem B (Butonla):** “Gözat” butonuna tıklayarak video dosyanızı seçin.
    * **Kaydetme Yeri:**
        * Program, seçtiğiniz videoya göre otomatik bir çıktı yolu önerir (örn: `_whatsapp.mp4`).
        * İsterseniz "Kaydet" butonuna tıklayarak dönüştürülen videonun nereye, hangi isimle kaydedileceğini kendiniz seçebilirsiniz.

3.  **Adım 2: Ayarlar (Opsiyonel)**
    * Bu bölümü **boş bırakırsanız**, program videonuzu varsayılan (WhatsApp) ayarlarla dönüştürür.
    * Eğer kendi özel FFmpeg ayarlarınızı girmek isterseniz (örneğin: `-b:v 2M -vf scale=1280:-1`, `-ss 00:00:10 -t 00:00:05` vb.), bu kutucuğu kullanabilirsiniz.
    * **Not:** Özel ayar girdiğinizde, önerilen çıktı adı otomatik olarak `_converted.mp4` olarak değişecektir.

4.  **Adım 3: Başlatma**
    * “**Dönüştürmeyi Başlat**” butonuna basın.

5.  **Adım 4: Bekleme**
    * Dönüştürme işlemi başlar. Bu sırada program arayüzü "İşlem sürüyor..." diyecek ve bir ilerleme çubuğu gösterecektir.
    * Lütfen videonun boyutuna ve ayarlara göre birkaç saniye veya dakika bekleyin.

6.  **Adım 5: Tamamlanma**
    * İşlem bittiğinde “Başarılı: Dönüştürme tamamlandı!” mesajını göreceksiniz.

---

## ✨ Ek Özellikler

* **Koyu Mod:** Programın sağ üst köşesindeki **"Koyu Mod"** anahtarı ile arayüz temasını anında değiştirebilirsiniz.

---

## ⚠️ Olası Sorunlar ve Çözümleri

### ❌ Hata: “Hata: FFmpeg bulunamadı.”
**Çözüm:** 1. Adım’ı eksik yaptınız.
`ffmpeg.exe` dosyasının `VideoDonusturucu.exe` ile **birebir aynı klasörde** olduğundan emin olun.

---

### ⚙️ Hata: “FFmpeg Hatası: ...”
**Çözüm:** Bu, `ffmpeg`'in videoyu işleyemediği anlamına gelir.
* Dönüştürmeye çalıştığınız video dosyası bozuk veya hasarlı olabilir.
* "Özel FFmpeg Parametreleri" bölümüne girdiğiniz komut hatalı olabilir.

---

## 📦 İndirme

Programın en son sürümünü aşağıdaki bağlantıdan indirebilirsiniz:

👉 **[VideoDonusturucu.exe İndir](https://github.com/mustafacobanlab/VideoDonusturucu/raw/main/Download/VideoDonusturucu.exe)**

---

**Hazırlayan:** `Mustafa Çoban`
**Lisans:** Ücretsiz kullanım (non-commercial)
```