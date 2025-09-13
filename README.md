# 🎬 Film Öneri Sistemi

Bu proje, **içerik tabanlı bir film öneri sistemi** sunar.  
Kullanıcı bir film adı girer ve sistem, benzer filmleri önerir.

## 🚀 Özellikler
- İçerik tabanlı filtreleme (overview üzerinden TF-IDF + cosine similarity)
- Basit kullanım
- Geliştirilebilir yapı (işbirlikçi filtreleme, hibrit modeller eklenebilir)

## 📂 Proje Yapısı
```
film-recommender/
│── data/movies.csv
│── src/recommender.py
│── requirements.txt
│── README.md
```

## 🔧 Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/film-recommender.git
   cd film-recommender
   ```

2. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Çalıştırın:
   ```bash
   python src/recommender.py
   ```

## 📊 Veri Seti
Bu projede `movies.csv` dosyası kullanılmaktadır.  
Kaggle'dan [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) indirilebilir.
## 📊 Google Colab Üzerinde Çalıştır

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/talatylmzdr/film-recommender/blob/main/film_recommender_colab.ipynb)

