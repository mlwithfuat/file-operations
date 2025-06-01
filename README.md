# PDF Araçları Koleksiyonu

Bu proje, PDF dosyalarıyla çalışmak için iki temel araç içerir:
- **PDF Birleştirme Aracı**: Birden fazla PDF dosyasını tek dosyada birleştirir
- **PDF to Word Dönüştürücü**: PDF dosyalarını Word formatına dönüştürür

## 🚀 Özellikler

### PDF Birleştirme Aracı
- ✅ Manuel dosya seçimi ile birleştirme
- ✅ Klasördeki tüm PDF'leri otomatik birleştirme
- ✅ Komut satırı ve interaktif mod desteği
- ✅ Hata kontrolü ve dosya doğrulama
- ✅ Kullanıcı dostu arayüz

### PDF to Word Dönüştürücü
- ✅ İki farklı çıkarma motoru (PyPDF2 & pdfplumber)
- ✅ Tablo çıkarma ve Word'e aktarma
- ✅ Toplu dönüştürme desteği
- ✅ Format ve sayfa yapısı koruması
- ✅ Komut satırı ve interaktif mod

## 📋 Gereksinimler

### Sistem Gereksinimleri
- Python 3.7 veya üzeri
- Windows, macOS veya Linux

### Python Kütüphaneleri
```bash
pip install PyPDF2 pdfplumber python-docx
```

Veya requirements.txt dosyası ile:
```bash
pip install -r requirements.txt
```

## 📦 Kurulum

1. **Projeyi klonlayın:**
```bash
git clone https://github.com/username/pdf-tools.git
cd pdf-tools
```

2. **Gerekli kütüphaneleri yükleyin:**
```bash
pip install -r requirements.txt
```

3. **Araçları kullanmaya başlayın!**

## 🛠️ Kullanım

### PDF Birleştirme Aracı

#### Komut Satırı Kullanımı
```bash
# Belirli dosyaları birleştir
python pdf_merger.py --files dosya1.pdf dosya2.pdf dosya3.pdf --output sonuc.pdf

# Klasördeki tüm PDF'leri birleştir
python pdf_merger.py --folder ./pdf_klasoru --output birlestirilmis.pdf
```

#### İnteraktif Mod
```bash
python pdf_merger.py
```
Program size seçenekler sunacak ve adım adım yönlendirecek.

### PDF to Word Dönüştürücü

#### Komut Satırı Kullanımı
```bash
# Basit dönüştürme
python pdf_to_word.py --input belge.pdf --output sonuc.docx

# Tablolarla birlikte dönüştürme
python pdf_to_word.py --input belge.pdf --output sonuc.docx --method pdfplumber --tables

# Toplu dönüştürme
python pdf_to_word.py --folder ./pdf_klasoru
```

#### İnteraktif Mod
```bash
python pdf_to_word.py
```

## 📚 Detaylı Kullanım Örnekleri

### PDF Birleştirme Örnekleri

```bash
# Örnek 1: İki dosyayı birleştir
python pdf_merger.py --files rapor1.pdf rapor2.pdf --output final_rapor.pdf

# Örnek 2: Proje klasöründeki tüm PDF'leri birleştir
python pdf_merger.py --folder ./proje_dosyalari --output proje_tam.pdf

# Örnek 3: İnteraktif modda manuel seçim
python pdf_merger.py
# 1. Dosya listesi girerek birleştir -> seçin
# Dosyalar: belge1.pdf, belge2.pdf, belge3.pdf
# Çıktı: birlestirilmis_belge.pdf
```

### PDF to Word Dönüştürme Örnekleri

```bash
# Örnek 1: Temel dönüştürme
python pdf_to_word.py --input akademik_makale.pdf --output makale.docx

# Örnek 2: Tablolarla birlikte (önerilen)
python pdf_to_word.py --input finansal_rapor.pdf --output rapor.docx --method pdfplumber --tables

# Örnek 3: Toplu dönüştürme
python pdf_to_word.py --folder ./tum_makaleler
# Sonuç: ./tum_makaleler/converted_word_files/ klasöründe
```

## ⚙️ Konfigürasyon Seçenekleri

### PDF Birleştirme Parametreleri
| Parametre | Açıklama | Varsayılan |
|-----------|----------|------------|
| `--files` | Birleştirilecek PDF dosya listesi | - |
| `--folder` | PDF dosyalarının bulunduğu klasör | - |
| `--output` | Çıktı dosyası adı | `birlestirilmis.pdf` |

### PDF to Word Parametreleri
| Parametre | Açıklama | Varsayılan |
|-----------|----------|------------|
| `--input` | Kaynak PDF dosyası | - |
| `--output` | Hedef Word dosyası | `{dosya_adı}_converted.docx` |
| `--folder` | Toplu dönüştürme klasörü | - |
| `--method` | Çıkarma motoru (`pypdf2`/`pdfplumber`) | `pdfplumber` |
| `--tables` | Tabloları dahil et | `False` |

## 🎯 Çıkarma Motorları Karşılaştırması

| Özellik | PyPDF2 | pdfplumber |
|---------|--------|------------|
| **Hız** | Çok Hızlı ⚡ | Normal 🚀 |
| **Metin Kalitesi** | Temel 📝 | Yüksek 📄 |
| **Tablo Desteği** | Yok ❌ | Var ✅ |
| **Format Koruması** | Düşük | Yüksek |
| **Önerilen Kullanım** | Hızlı çıkarma | Kaliteli dönüştürme |

## 📁 Proje Yapısı

```
pdf-tools/
├── pdf_merger.py           # PDF birleştirme aracı
├── pdf_to_word.py          # PDF to Word dönüştürücü
├── requirements.txt        # Python bağımlılıkları
├── README.md              # Bu dosya
├── examples/              # Örnek dosyalar
│   ├── sample1.pdf
│   ├── sample2.pdf
│   └── sample3.pdf
└── output/               # Çıktı dosyaları
    ├── merged/
    └── converted/
```

## 🔧 Sorun Giderme

### Yaygın Hatalar ve Çözümleri

#### "Modül bulunamadı" Hatası
```bash
# Çözüm: Kütüphaneleri yeniden yükleyin
pip install --upgrade PyPDF2 pdfplumber python-docx
```

#### "Dosya bulunamadı" Hatası
- Dosya yollarının doğru olduğundan emin olun
- Dosya adlarında Türkçe karakter varsa İngilizce karakterlerle deneyin
- Mutlak yol kullanmayı deneyin: `/tam/yol/dosya.pdf`

#### PDF Dönüştürme Kalitesi Düşük
```bash
# pdfplumber metodunu ve tablo desteğini kullanın
python pdf_to_word.py --input dosya.pdf --method pdfplumber --tables
```

#### Büyük Dosyalar için Performans
- PyPDF2 metodunu tercih edin (hızlı ancak basit)
- Dosyaları küçük parçalara bölün
- Sistem belleğini kontrol edin

### Desteklenmeyen PDF Türleri
- **Taranmış PDF'ler**: OCR (Optical Character Recognition) gerektirir
- **Şifrelenmiş PDF'ler**: Şifre çözme özelliği eklenmeli
- **Çok karmaşık layout'lar**: Format tam korunamayabilir

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin yeni-ozellik`)
5. Pull Request oluşturun

### Geliştirme Önerileri
- [ ] OCR desteği eklenmesi
- [ ] GUI arayüzü geliştirme
- [ ] PDF şifre çözme özelliği
- [ ] Batch processing için progress bar
- [ ] Daha fazla çıktı formatı (Excel, TXT, vb.)

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.


