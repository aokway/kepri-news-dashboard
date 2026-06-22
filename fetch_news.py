import feedparser
import json
import os
from datetime import datetime, timezone

# Daftar RSS feed berita Kepri
RSS_FEEDS = [
    {
        "name": "Antara Kepri",
        "url": "https://kepri.antaranews.com/rss/",
        "color": "#e63946"
    },
    {
        "name": "Batamnews",
        "url": "https://batamnews.co.id/feed",
        "color": "#2a9d8f"
    },
    {
        "name": "Tribun Batam",
        "url": "https://batam.tribunnews.com/rss",
        "color": "#e76f51"
    },
    {
        "name": "Antara Batam (English)",
        "url": "https://en.antaranews.com/rss/nusantara-batam.xml",
        "color": "#457b9d"
    },
]

def parse_date(entry):
    """Ambil tanggal dari entry RSS, fallback ke sekarang jika gagal."""
    for attr in ("published_parsed", "updated_parsed"):
        t = getattr(entry, attr, None)
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc).isoformat()
            except Exception:
                pass
    return datetime.now(timezone.utc).isoformat()

def fetch_all():
    articles = []

    for feed_info in RSS_FEEDS:
        print(f"Mengambil dari {feed_info['name']}...")
        try:
            feed = feedparser.parse(feed_info["url"])
            for entry in feed.entries[:15]:  # Ambil 15 artikel per sumber
                articles.append({
                    "title": entry.get("title", "").strip(),
                    "link": entry.get("link", ""),
                    "summary": entry.get("summary", "")[:300].strip(),
                    "published": parse_date(entry),
                    "source": feed_info["name"],
                    "color": feed_info["color"],
                })
            print(f"  ✓ {len(feed.entries[:15])} artikel")
        except Exception as e:
            print(f"  ✗ Gagal: {e}")

    # Urutkan dari terbaru
    articles.sort(key=lambda x: x["published"], reverse=True)

    output = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total": len(articles),
        "articles": articles
    }

    os.makedirs("data", exist_ok=True)
    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nSelesai! {len(articles)} artikel disimpan ke data/news.json")

if __name__ == "__main__":
    fetch_all()
