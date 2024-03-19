
from src.fume_spider import Fume_spider
from src.fume_writer import Fume_writer
from src.url.url_parser import Url
from src.url.url_params import Url_params
from src.login import *

def main():
    u = Url()
    u1 = Url_params('食其家','2023-10-01','2023-10-31',5)
    urls = u.concatenate_url_with_condition(u1)
    for item in urls:
        print(item)    

if __name__ == '__main__':
    main()