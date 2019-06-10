"""
    Author:Yiwen Gao

"""
from icrawler.builtin import GoogleImageCrawler
from datetime import date
from icrawler.builtin import FlickrImageCrawler
from icrawler.builtin import UrlListCrawler
import base64

from icrawler import ImageDownloader
from six.moves.urllib.parse import urlparse

# #####################################
# URLlist Crawling
# urllist_crawler = UrlListCrawler(downloader_threads=4,
#                                  storage={'root_dir': 'D:/2019 Summer Term/Project/siamese cat'})
# urllist_crawler.crawl('D:/2019 Summer Term/Project/Crawling/urllist/siamese cat.txt')
# 



# #####################################
# flicker Crawling
# flickr_crawler = FlickrImageCrawler('923381f3ba63f6e57a9f559b0946bf50',
#                                     storage={'root_dir': 'D:/2019 Summer Term/Project/cat-flickr'})
# flickr_crawler.crawl(max_num=100, tags='cat',
#                      min_upload_date=date(2015, 5, 1))
# ######################################

# Google Crawling
# downloader filename
#####################################################################
# class PrefixNameDownloader(ImageDownloader):

#     def get_filename(self, task, default_ext):
#         filename = super(PrefixNameDownloader, self).get_filename(
#             task, default_ext)
#         return 'cat' + filename


# class Base64NameDownloader(ImageDownloader):

#     def get_filename(self, task, default_ext):
#         url_path = urlparse(task['file_url'])[2]
#         if '.' in url_path:
#             extension = url_path.split('.')[-1]
#             if extension.lower() not in [
#                     'jpg', 'jpeg', 'png', 'bmp'
#             ]:
#                 extension = default_ext
#         else:
#             extension = default_ext
#         file_idx = self.fetched_num + self.file_idx_offset
#         return '{:06d}.{}'.format(file_idx, extension)
###################################################################

###########         cralwer         #############

google_storage = {'root_dir': 'D:/2019 Summer Term/Project/test1'}
i=0
while i <= 100:
    i+=1
    for keyword in ['Siamese cat', 'Scottish Fold cat','Abyssinian cat',
                'Bengal cat','Bombay cat','Birman cat','British Shorthair cat',
                'Maine Coon cat','Persian cat','Egyptian Mau cat',
                'Sphynx cat','Ragdoll cat','Russian Blue cat','American Shorthair cat',
                'Exotic cat','Siberian cat','American Bobtail cat'
    ]:
        google_crawler = GoogleImageCrawler(
            parser_threads=10,
            downloader_threads=20,
            storage={'root_dir': 'D:/2019 Summer Term/Project/test2/{}'.format(keyword)}
        )
        google_crawler.session.verify = False
        google_crawler.crawl(
            keyword=keyword, max_num=180, min_size=(300, 300),
            filters={'date':((2016, 1, 1),None)})
        google_crawler.crawl(
            keyword=keyword, max_num=180, min_size=(300, 300),
            filters={'date':((2012, 1, 1), (2015, 12, 31))}
            , file_idx_offset='auto')
        
    if i ==2:
        break

# google_crawler = GoogleImageCrawler(parser_threads=4,
#                                    downloader_threads=4,
#                                    storage=google_storage)
# google_crawler.crawl(keyword='dog', max_num=100)