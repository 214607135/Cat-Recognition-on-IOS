from icrawler.builtin import GoogleImageCrawler
from datetime import date
from icrawler.builtin import FlickrImageCrawler
from icrawler.builtin import UrlListCrawler

urllist_crawler = UrlListCrawler(downloader_threads=4,
                                 storage={'root_dir': 'D:/2019 Summer Term/Project/siamese cat'})
urllist_crawler.crawl('D:/2019 Summer Term/Project/Crawling/urllist/siamese cat.txt')

"""
google_storage = {'root_dir': 'D:/2019 Summer Term/Project/dog'}
google_crawler = GoogleImageCrawler(parser_threads=4,
                                   downloader_threads=4,
                                   storage=google_storage)
google_crawler.crawl(keyword='dog', max_num=100)


flickr_crawler = FlickrImageCrawler('your_apikey', # haven't gotten yet
                                    storage={'root_dir': 'D:/2019 Summer Term/Project/cat-flickr'})
flickr_crawler.crawl(max_num=1000, tags='cat',
                     group_id='68012010@N00', min_upload_date=date(2015, 5, 1))"""