# 📄 Belge Soruları Asistanı

Kullanıcıların **PDF** yükleyip belge hakkında **soru sorabildiği** bir Streamlit uygulaması. PDF'den metin çıkarır, soruları **LangChain + OpenAI** ile yanıtlar ve **sohbet geçmişini** tutar.

## 🚀 Özellikler
- **PDF Yükleme** (sadece .pdf, 10 MB sınır)
- **PDF İşleme**: `pdfplumber` ile metin çıkarma, tam metni görüntüleme
- **Soru-Cevap**: LangChain `LLMChain` + `ConversationBufferMemory`
- **Chat Arayüzü**: `st.chat_message` ile mesajlar
- **Sayfa Sayısı**: Toplam sayıyı ve okunan sayfaları gösterme
- **Model Seçimi**: Sidebar'dan farklı modeller (ör. `gpt-4o-mini`, `gpt-4o`, `o4-mini`, özel ad)
- **Sohbet İndirme**: TXT ve JSON formatında indirme
- **PDF Önizleme**: İlk sayfanın metinsel önizlemesi
- **Sohbet Temizleme**: Tek tıkla geçmişi sıfırlama
- **Karakter/Kelime Sayısı**: Çıkarılan metin istatistikleri

> Not: Büyük PDF'ler için metin parçalara ayrılır ve **basit anahtar kelime eşleşmesi** ile ilgili parçalar seçilerek modele verilir.

---

## 🧰 Kurulum (VS Code ile Adım Adım)

1. **Projeyi indirin / klonlayın**
   ```bash
   git clone <repo-url>
   cd belge-asistani
   ```

2. **Python sürümü**: 3.10+ önerilir. (Kontrol: `python --version`)

3. **Sanal ortam oluşturun ve etkinleştirin**
   ```bash
   python -m venv .venv
   
   source .venv/bin/activate
   ```

4. **Gerekli paketler**
   ```bash
   pip install -r requirements.txt
   ```

5. **API anahtarı**
   - `.env.example` dosyasını `.env` olarak kopyalayın ve kendi **OPENAI_API_KEY** değerinizle doldurun.
   - **.env dosyasını asla GitHub'a yüklemeyin.** `.gitignore` buna göre ayarlı.

6. **Uygulamayı çalıştırın**
   ```bash
   streamlit run app.py
   ```
   Tarayıcıda açılan sayfadan PDF yükleyin ve soru sorun.

---

## 📁 Proje Yapısı
```
belge-asistani/
├── app.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

## 🧪 Test İpuçları
- Metin içeren basit bir PDF ile başlayın.
- Görsel ağırlıklı (metinsiz) PDF'lerde metin çıkarılamayabilir — uygulama uyarır.
- Uzun PDF'lerde soru sorduğunuzda önce anahtar kelimeleri net yazın (konu, kişi, başlık).

---

## 🔐 Güvenlik
- API anahtarınızı **.env** dosyasında tutun; **koda gömmeyin**.
- Paylaşıma açık repolara **.env** yüklemeyin.

---

## 📸 Ekran Görüntüleri
Aşağıdaki bölümleri açıp ekran görüntüsü alabilirsiniz:
- **PDF Önizleme (1. sayfa)** expander
- **Sohbet arayüzü** (soru-cevap)
- **Sohbeti indir (TXT/JSON)** tuşları

---

## ℹ️ Notlar
- `langchain_openai.ChatOpenAI` modeli için `OPENAI_API_KEY` ortam değişkeni gerekir.
- Varsayılan yanıt stili kısa ve doğrudandır; bağlam yoksa “Bu bilgi belgede yok” denir.
