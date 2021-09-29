from django.core.management.base import BaseCommand

from shop.spiders import OmaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Crawl oma.by"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()
        