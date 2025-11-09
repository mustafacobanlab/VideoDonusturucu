# 🎬 Modern Video Dönüştürücü Kullanım Talimatları

Bu program, elinizdeki videoları (MP4, MKV, MOV vb.) varsayılan olarak WhatsApp'ta sorunsuz paylaşılabilen standart bir formata (**H.264 + AAC**) dönüştürmenizi sağlar.  
Ayrıca, **özel FFmpeg parametreleri** girerek kendi gelişmiş dönüştürme ayarlarınızı uygulamanıza da olanak tanır.

---

## 🧩 1. Zorunlu Kurulum (Sadece 1 Kez Yapılacak)

Programın çalışabilmesi için `ffmpeg` adlı ücretsiz bir "motor" dosyasına ihtiyacınız var.

**✅ En Kolay Yöntem (Tavsiye Edilen):**

1.  Web tarayıcınızı açın ve şu adrese gidin:  
    👉 [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

2.  Sayfada biraz aşağı inin ve **"Release builds"** bölümünden  
    `ffmpeg-release-full.7z` (veya `.zip`) dosyasını indirin.

3.  İndirilen dosyayı bir klasöre çıkartın (WinRAR, 7-Zip veya Windows'un "Çıkart" özelliği ile).

4.  Oluşan `ffmpeg-...-full` klasörünün içine girin ve **`bin`** klasörünü açın.

5.  `bin` klasörünün içindeki **`ffmpeg.exe`** dosyasını kopyalayın.

6.  `VideoDonusturucu.exe` dosyasının bulunduğu klasöre geri dönün ve **ffmpeg.exe**'yi **yanına yapıştırın**.

---

📁 **Doğru klasör yapısı şöyle olmalıdır:**

- Video_Donusturucu_Klasoru/
  - \_\_VideoDonusturucu.exe <-- Programınız
  - \_\_ ffmpeg.exe <-- Motor dosyası
Artık programı kullanmaya hazırsınız 🎉

---

## ▶️ 2. Programın Kullanımı

1. **Programı Başlatın:**  
   `VideoDonusturucu.exe` dosyasına çift tıklayın.

2. **Adım 1: Dosyaları Seçin**
   - **Dosya Seçme:**
     - **Sürükle-Bırak:** Video dosyasını ilgili alana sürükleyin.
     - **Butonla:** "Gözat" butonuna tıklayarak dosya seçin.
   - **Kaydetme Yeri:**
     - Program otomatik bir çıktı yolu önerir (örn: `_whatsapp.mp4`).
     - Dilerseniz "Kaydet" butonuyla konum ve isim belirleyebilirsiniz.

3. **Adım 2: Ayarlar (Opsiyonel)**
   - Boş bırakırsanız, varsayılan (WhatsApp) ayarlar kullanılır.
   - Özel FFmpeg parametreleri girerseniz (örn: `-b:v 2M -vf scale=1280:-1`) çıktı adı `_converted.mp4` olarak değişir.

4. **Adım 3: Başlatma**
   - “**Dönüştürmeyi Başlat**” butonuna basın.

5. **Adım 4: İşlem Süresi**
   - Program, ilerleme çubuğu ve “İşlem sürüyor...” mesajı ile dönüşümü gösterir.
   - Boyut ve ayarlara göre işlem birkaç saniye veya dakika sürebilir.

6. **Adım 5: Tamamlanma**
   - “Başarılı: Dönüştürme tamamlandı!” mesajını göreceksiniz.

---

## ✨ Ek Özellikler

- **Koyu Mod:** Sağ üst köşedeki "Koyu Mod" anahtarı ile arayüz temasını değiştirebilirsiniz.

---

## ⚠️ Olası Sorunlar ve Çözümleri

### ❌ Hata: “Hata: FFmpeg bulunamadı.”
- `ffmpeg.exe` dosyasının `VideoDonusturucu.exe` ile **aynı klasörde** olduğundan emin olun.

### ⚙️ Hata: “FFmpeg Hatası: ...”
- Video dosyası bozuk olabilir veya özel FFmpeg parametresi hatalı olabilir.

---

## 📦 İndirme

👉 **[VideoDonusturucu.exe İndir](https://github.com/mustafacobanlab/VideoDonusturucu/raw/main/Download/VideoDonusturucu.exe)**

---
![Program Ana Ekranı](https://github.com/user-attachments/assets/49f13eb7-77be-4d60-a7f0-3aa55f7e3183)

---
**Hazırlayan:** Mustafa Çoban  
**Lisans:** Ücretsiz kullanım (non-commercial)
