# 📰 Dashboard Berita Kepri

Dashboard sederhana yang mengumpulkan berita terbaru dari Kepulauan Riau secara otomatis setiap hari.

## Sumber Berita
- [Antara Kepri](https://kepri.antaranews.com)
- [Batamnews](https://batamnews.co.id)
- [Tribun Batam](https://batam.tribunnews.com)
- [Antara Batam (English)](https://en.antaranews.com)

## Fitur
- Berita diperbarui otomatis setiap hari pukul 07:00 WIB via GitHub Actions
- Filter berdasarkan sumber berita
- Pencarian judul & isi berita
- Tampilan responsif untuk mobile

## Cara Pakai Lokal

**1. Clone repo**
```bash
git clone https://github.com/USERNAME/kepri-news-dashboard.git
cd kepri-news-dashboard
```

**2. Install dependency**
```bash
pip install -r requirements.txt
```

**3. Ambil berita**
```bash
python fetch_news.py
```

**4. Buka dashboard**
Buka file `index.html` di browser, atau jalankan server lokal:
```bash
python -m http.server 8000
# Buka http://localhost:8000
```

## Deploy ke GitHub Pages

1. Push repo ke GitHub
2. Pergi ke **Settings → Pages**
3. Pilih source: **Deploy from branch → main → / (root)**
4. Dashboard bisa diakses di `https://USERNAME.github.io/kepri-news-dashboard`

## Struktur Project
```
kepri-news-dashboard/
├── index.html          # Dashboard utama
├── fetch_news.py       # Script ambil berita dari RSS
├── requirements.txt    # Python dependencies
├── data/
│   └── news.json       # Data berita (auto-generated)
└── .github/
    └── workflows/
        └── update-news.yml  # GitHub Actions scheduler
```

## Kontribusi
Mau tambah sumber berita Kepri lainnya? Edit bagian `RSS_FEEDS` di `fetch_news.py`!
