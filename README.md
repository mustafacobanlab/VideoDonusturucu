# 🎬 Video Dönüştürücü Kullanım Talimatları

Bu program, elinizdeki videoları (MP4, MKV, MOV vb.) WhatsApp'ta sorunsuz paylaşılabilen standart bir formata (**H.264 + AAC**) dönüştürmenizi sağlar.

---

## 🧩 1. Zorunlu Kurulum (Sadece 1 Kez Yapılacak)

Programınızın video dönüştürme işlemini yapabilmesi için `ffmpeg` adında ücretsiz bir "motor" dosyasına ihtiyacı vardır. Kurulumu çok basittir.

**✅ En Kolay Yöntem (Tavsiye Edilen):**

1. Web tarayıcınızı açın ve şu adrese gidin:  
   👉 [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

2. Sayfada biraz aşağı inin ve **"Release builds"** bölümünü bulun.  
   `ffmpeg-release-full.7z` (veya `.zip`) yazan linke tıklayarak dosyayı indirin.

3. İndirdiğiniz `.7z` (veya `.zip`) dosyasını bir klasöre çıkartın.  
   (WinRAR, 7-Zip veya Windows'un kendi "Çıkart" özelliğini kullanabilirsiniz.)

4. Oluşan `ffmpeg-...-full` klasörünün içine girin.

5. Orada bir **`bin`** klasörü göreceksiniz, onun da içine girin.

6. `bin` klasörünün içinde bir sürü dosya göreceksiniz.  
   Bize sadece **`ffmpeg.exe`** dosyası lazım.

7. Bu **`ffmpeg.exe`** dosyasını kopyalayın.

8. Size gönderilen `VideoDonusturucu.exe` (bu program) dosyasının bulunduğu klasöre geri dönün ve  
   `ffmpeg.exe` dosyasını **tam yanına** yapıştırın.

---

📁 **Klasör yapısı doğruysa şu şekilde görünmelidir:**


Artık programı kullanmaya hazırsınız 🎉  
`ffmpeg.exe` o klasörde olduğu sürece programınız çalışacaktır.

---

## ▶️ 2. Programın Kullanımı

1. **`VideoDonusturucu.exe`** dosyasına çift tıklayarak programı çalıştırın.

2. **Dosya Seçme:**
   - **Yöntem A (Sürükle-Bırak):** Dönüştürmek istediğiniz video dosyasını programın üstündeki  
     “Video Dosyasını Buraya Sürükle Bırak” alanına sürükleyin.
   - **Yöntem B (Butonla):** “Gözat” butonuna tıklayarak video dosyanızı seçin.

3. **Kaydetme Yeri:**
   - Program otomatik olarak videonun orijinal adının sonuna `_whatsapp.mp4` ekleyerek bir çıktı yolu önerir.
   - İsterseniz "Kaydet" butonuna tıklayarak dönüştürülen videonun nereye, hangi isimle kaydedileceğini kendiniz seçebilirsiniz.

4. **Başlatma:**
   - “**Dönüştür (H.264 + AAC)**” butonuna basın.

5. **Bekleme:**
   - Dönüştürme işlemi başlar. Bu sırada program arayüzü "İşlem sürüyor..." diyecek ve bir ilerleme çubuğu gösterecektir.
   - Lütfen videonun boyutuna göre birkaç saniye veya dakika bekleyin.

6. **Tamamlanma:**
   - İşlem bittiğinde “✅ Dönüştürme tamamlandı!” mesajını göreceksiniz.

---

## ⚠️ Olası Sorunlar ve Çözümleri

### ❌ Hata: “FFmpeg bulunamadı”
**Çözüm:** 1. Adım’ı eksik yaptınız.  
`ffmpeg.exe` dosyasının `VideoDonusturucu.exe` ile **birebir aynı klasörde** olduğundan emin olun.

---

### ⚙️ Hata: “FFmpeg Hatası: ...”
**Çözüm:** Bu, `ffmpeg`'in videoyu işleyemediği anlamına gelir.  
Dönüştürmeye çalıştığınız video dosyası bozuk veya hasarlı olabilir.

---

### 💤 Program “Dönüştür” deyince donuyor veya yanıt vermiyor
**Çözüm:** Program donmuş gibi görünse de aslında arka planda çalışıyordur.  
Lütfen işlemin bitmesini bekleyin.

---

## 📦 İndirme

Programın en son sürümünü aşağıdaki bağlantıdan indirebilirsiniz:

👉 **[VideoDonusturucu.exe İndir](https://github.com/user/VideoDonusturucu/Download)**

---

**Hazırlayan:** `Mustafa Çoban`  
**Lisans:** Ücretsiz kullanım (non-commercial)
