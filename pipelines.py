from db_controller import insert_article


class DatabasePipeline:
    def process_item(self, item, spider):
        insert_article(item['title'], item['authors'], item['content'], item['url'])
        return item
