# 📘 LearnMate – Günlük Planlama Asistanı

---

## 👥 Takım Üyeleri

| İsim | Rolü |
|------|------|
| Mehmet Bozkurt | Product Manager |
| Simay Şahiner | Scrum Master |

---

## 🎯 Proje Açıklaması

**LearnMate**, yapay zeka destekli bir günlük planlama defteri uygulamasıdır. Kullanıcıların günlük hedeflerini, görevlerini ve his durumlarını kaydetmesini sağlar. Uygulama, eksik tamamlanan görevlere göre öneriler sunarak planlı ve verimli çalışma alışkanlığı kazandırmayı hedefler.

Örnek öneri:  
> “Son 2 gündür kitap okuma hedefini tamamlamadın. Yarın sabah 10:00'da 25 dakikalık bir okuma oturumu planlamanı öneririm.”

Yapay zeka sistemi, kullanıcı geçmiş verilerini analiz ederek yapılmayan görevleri tespit eder ve **Gemini generative AI** altyapısıyla kişiye özel öneriler oluşturur.

---

## 🧠 Uygulama Özellikleri

- 📅 Günlük görev ekleme ve takibi
- 📈 Görev tamamlama durumuna göre AI öneri üretimi
- 🤖 Gemini AI ile kişisel planlama desteği
- 🧠 His durumu kaydı
- 🔒 Oturum tabanlı kullanıcı yönetimi (SessionMiddleware)
- 🗂️ MSSQL veritabanı ile kullanıcıya özel veri yönetimi

---

## 🎯 Hedef Kitle

- Öğrenciler (sınav/ödev planlaması)
- Profesyoneller (günlük iş takibi)
- Freelance çalışanlar (hedef yönetimi)
- Kişisel gelişim odaklı bireyler

---

## 🖼️ Uygulama Görselleri

> Figma prototipi henüz oluşturulmadı. Tasarım tamamlandığında buraya eklenecektir.

---

## 📆 Daily Scrum

- Toplantılar her gün Google Meet üzerinden yapıldı.
- WhatsApp üzerinden günlük yazılı scrum mesajları gönderildi.

📸 Scrum SS’leri:
> <img width="1876" height="994" alt="Screenshot 2025-07-15 220102" src="https://github.com/user-attachments/assets/a2f49afe-e3ac-4598-a12e-ab6866667dae" />

---

## 🔄 Sprint Süreci

<details>
<summary><h3>Sprint 1</h3></summary>

### 🎯 Hedefler
- [x] Proje fikrinin belirlenmesi  
- [x] Yapay zeka mekanizması için ihtiyaç analizi  
- [x] Rol ve görev dağılımı  
- [ ] Arayüz ilk taslağı

---

### 📌 Backlog
- Kullanıcı analizi ve persona oluşturuldu
- Rakip uygulama analizi yapıldı
- AI öneri sistemi için kural tabanlı mantık geliştirilmeye başlandı

---

### 🔍 Review
- Proje fikri netleşti  
- Yapay zekaya dayalı öneri sisteminin temel yapısı planlandı

---

### 🔁 Retrospective
- ✅ Takım içi iletişim güçlüydü  
- ⚠️ Tasarım süreci biraz yavaş ilerledi  
- 🛠️ UI/UX için haftalık Figma çalışmaları planlandı

---

### 🧮 Puanlama

| Kategori | Puan (0-10) |
|----------|-------------|
| Fikir Geliştirme | **[10]** |
| Araştırma Derinliği | **[8]** |
| Süreç Takibi | **[7]** |
| Takım Uyumu | **[8]** |
| Teknik Çıktılar | **[8]** |

🧠 **Puanlama Mantığı:**  
Sprint içeriğine göre 50 puan üzerinden değerlendirme yapılmıştır.

</details>

<details>
<summary><h3>Sprint 2</h3></summary>

### 🎯 Hedefler
- [x] Ana sayfa HTML ve TailwindCSS ile oluşturulacak  
- [x] Görev ekleme/silme işlevleri geliştirilecek  
- [x] Günlük his ve değerlendirme alanları eklenecek  
- [x] Yapay zeka öneri kutusu hazırlanacak  
- [x] FastAPI ile backend başlangıcı yapılacak

---

### 📌 Backlog
- Görev yönetimi kutucukları tamamlandı  
- His durumu alanları eklendi  
- Yapay zeka öneri kutusu hazırlandı (statik olarak)  
- FastAPI altyapısı kuruldu  
- TailwindCSS ile frontend yapı tamamlandı

---

### 🔍 Review
- Ana sayfa tasarımı tamamlandı  
- Görevler checkbox ve silme butonlarıyla işlevsel hale getirildi  
- Yapay zeka öneri kutusu görsel olarak eklendi  
- FastAPI backend hazırlandı  
- MSSQL entegrasyonu planlandı  

---

### 🔁 Retrospective
- ✅ Görev yönetimi başarıyla geliştirildi  
- ✅ UI tasarımı beklentiyi karşıladı  
- ⚠️ Dark tema entegrasyonu sprint içinde yapılamadı  
- ⚠️ AI önerileri şimdilik manuel olarak girildi  
- 🛠️ 3. sprint’te AI sistemi generative hale getirilecek

---

### 🧮 Puanlama

| Kategori | Puan (0-10) |
|----------|-------------|
| UI Uygulama | **[9]** |
| Görev Yönetimi | **[9]** |
| Teknik Derinlik | **[8]** |
| Takım Uyumu | **[9]** |
| Süreç Yönetimi | **[8]** |

🧠 **Puanlama Mantığı:**  
Sprint 2 içeriği 50 puan üzerinden değerlendirilmiştir.  
Görev ve his takibi başarıyla entegre edildi. AI tarafı ise bir sonraki sprint'e bırakıldı.

</details>

<details>
<summary><h3>Sprint 3</h3></summary>

### 🎯 Hedefler
- [x] Kullanıcı girişi ekranı geliştirilecek  
- [x] Görevler, kullanıcı ve his verileri MSSQL'e aktarılacak  
- [x] SessionMiddleware ile kullanıcı oturumu yönetilecek  
- [x] Gemini AI ile dinamik öneri sistemi kurulacak  
- [x] Uygulama tam fonksiyonel hale getirilecek ve proje sonlandırılacak

---

### 📌 Backlog
- MSSQL veritabanı bağlantısı başarıyla kuruldu  
- Kullanıcılar, görevler ve his verileri veritabanına aktarıldı  
- FastAPI üzerinden `SessionMiddleware` ile kullanıcı oturumu oluşturuldu  
- Yapay zeka öneri sistemi Gemini AI ile entegre edildi  
- Kullanıcının tamamlamadığı görevlere göre öneriler üretilmeye başlandı  
- Proje son sprintte tamamlandı ✅

---

### 🔍 Review
- Kullanıcı girişi, görev kaydı ve öneri sistemi tam entegre edildi  
- Gemini AI başarılı şekilde görev analizine göre öneriler üretiyor  
- Session bazlı oturum kontrolü sorunsuz çalışıyor  
- Proje tüm hedefleriyle birlikte tamamlandı

---

### 🔁 Retrospective
- ✅ MSSQL entegrasyonu başarıyla çalıştı  
- ✅ Gemini AI öneri sistemi beklentiyi karşıladı  
- 🛠️ İleride dil seçeneği ve tema geçişi gibi kullanıcı deneyimi arttırıcı özellikler eklenebilir

---

### 🧮 Puanlama

| Kategori | Puan (0-10) |
|----------|-------------|
| Backend İşlevsellik | **[10]** |
| Kalıcı Veri Yapısı | **[10]** |
| AI Entegrasyonu | **[10]** |
| Kullanıcı Yönetimi | **[10]** |
| Proje Teslim Durumu | **[10]** |

🧠 **Puanlama Mantığı:**  
Projenin son sprintinde tüm sistemler birleştirildi. Kullanıcı verileri kalıcı hale getirildi, yapay zeka önerileri gerçek zamanlı üretildi ve proje başarıyla tamamlandı.

🎯 **Toplam Puan: 50 / 50**

</details>

---

## 🔗 Bağlantılar

- [Figma Tasarımı](EKLENECEK_LINK) _(hazırlanma aşamasında)_
