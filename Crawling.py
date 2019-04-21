from icrawler.builtin import GoogleImageCrawler

google_storage = {'root_dir': 'D:/2019 Summer Term/Project/dog'}
google_crawler = GoogleImageCrawler(parser_threads=4,
                                   downloader_threads=4,
                                   storage=google_storage)
google_crawler.crawl(keyword='dog', max_num=100)
