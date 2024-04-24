from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()


def insert_article(text, authors, content, url):

    db.insert({'Text': text, 'Author(s)': authors, 'Content': content, 'URL': url})
    print("Article inserted into the database.")


def fetch_article_by_url(url):
    result = db.search(Query().URL.test(lambda value: url in value))
    if result:
        return result[0]
    else:
        return None


def top_five_authors():
    results = db.all()
    author_counts = {}
    for result in results:
        authors = result.get('Author(s)')
        if authors:
            for author in authors.split(','):
                author = author.strip()
                author_counts[author] = author_counts.get(author, 0) + 1

    sorted_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_authors[:5]


def all_articles():
    return db.all()


def fetch_new_articles():
    from news_crawler import FoxnewsSpider
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings={'LittleBigCodeProject.DatabasePipeline': 300})

    # Run the spider
    process.crawl(FoxnewsSpider)
    process.start()
