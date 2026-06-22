import feedparser
import json
import os
from datetime import datetime, timezone

RSS_FEEDS = [
    # Antara Kepri - berbagai kategori (cover seluruh wilayah Kepri)
    {
        "name": "Antara Kepri",
        "url": "https://kepri.antaranews.com/rss/terkini.xml",
        "color": "#e63946"
    },
    {
        "name": "Antara Kepri Top News",
        "url": "https://kepri.antaranews.com/rss/top-news.xml",
        "color": "#c1121f"
    },
    {
        "name": "Antara Kepri Ekonomi & FTZ",
        "url": "https://kepri.antaranews.com/rss/ekonomi-ftz.xml",
        "color": "#e85d04"
    },
    {
        "name": "Antara Kepri Hukum",
        "url": "https://kepri.antaranews.com/rss/hukum.xml",
        "color": "#6a0572"
    },
    {
        "name": "Antara Kepri Politik",
        "url": "https://kepri.antaranews.com/rss/politik.xml",
        "color": "#023e8a"
    },
    {
        "name": "Antara Kepri Kesra",
        "url": "https://kepri.antaranews.com/rss/kesra.xml",
        "color": "#2d6a4f"
    },
    {
        "name": "Antara Kepri Olahraga",
        "url": "https://kepri.antaranews.com/rss/olahraga.xml",
        "color": "#f77f00"
    },
    {
        "name": "Antara Kepri Wisata",
        "url": "https://kepri.antaranews.com/rss/wisata.xml",
        "color": "#0096c7"
    },
    # Tribun Batam
    {
        "name": "Tribun Batam",
        "url": "https://batam.tribunnews.com/feed",
        "color": "#e76f51"
    },
    # Antara Nasional
    {
        "name": "Antara Nasional",
        "url": "https://www.antaranews.com/rss/terkini.xml",
        "color": "#457b9d"
    },
]

def parse_date(entry):
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
            count = 0
            for entry in feed.entries[:15]:
                articles.append({
                    "title": entry.get("title", "").strip(),
                    "link": entry.get("link", ""),
                    "summary": entry.get("summary", "")[:300].strip(),
                    "published": parse_date(entry),
                    "source": feed_info["name"],
                    "color": feed_info["color"],
                })
                count += 1
            print(f"  ✓ {count} artikel")
        except Exception as e:
            print(f"  ✗ Gagal: {e}")

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