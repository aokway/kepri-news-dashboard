# 📰 Dashboard Berita Kepri

> Dashboard berita lokal Kepulauan Riau yang diperbarui otomatis setiap hari — dibangun dengan Python & GitHub Actions.

🌐 **Live demo:** [aokway.github.io/kepri-news-dashboard](https://aokway.github.io/kepri-news-dashboard)

---

## ✨ Fitur

- 🔄 Berita diperbarui otomatis setiap hari pukul 07:00 WIB via GitHub Actions
- 🗂️ Filter berita berdasarkan sumber media
- 🔍 Pencarian judul & isi berita secara real-time
- 📱 Tampilan responsif untuk mobile & desktop
- ⚡ Tanpa database — data disimpan sebagai JSON statis

---

## 📰 Sumber Berita

| Media | Kategori |
|---|---|
| [Antara Kepri](https://kepri.antaranews.com) | Berita umum Kepri |
| [Antara Kepri Top News](https://kepri.antaranews.com/rss/top-news.xml) | Berita pilihan Kepri |
| [Tribun Batam](https://batam.tribunnews.com) | Berita Batam & sekitarnya |
| [Antara Nasional](https://www.antaranews.com) | Berita nasional Indonesia |

---

## 🛠️ Teknologi

- **Python** + `feedparser` — untuk mengambil data RSS
- **HTML / CSS / JavaScript** — tampilan dashboard
- **GitHub Actions** — auto-update berita setiap hari
- **GitHub Pages** — hosting gratis

---

## 🚀 Cara Pakai Lokal

**1. Clone repo**
```bash
git clone https://github.com/aokway/kepri-news-dashboard.git
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
```bash
python -m http.server 8000
# Buka http://localhost:8000
```

---

## ⚙️ Cara Kerja