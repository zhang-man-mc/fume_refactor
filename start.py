
from src.fume_spider import FumeSpider
from src.url.url_parser import Url,Url_params
from src.login import *
from src.survey.extract import Extract
# def main():
#     login_fume_web()
#     shop_name = ['','']
#     u = Url()
#     # urls = u.concatenate_url_with_condition('杨记齐齐哈尔烤肉','2023-10-01','2023-10-31',1)
#
#     u1 = Url_params('食其家','2023-10-01','2023-10-31',5)
#     urls = u.concatenate_url_with_condition(u1)
#     f_s = FumeSpider()
#     fume_sum = []
#     for item in urls:
#         fume_sum += f_s.fetch(item)
#     print(f'爬取总数为：{fume_sum}')
#     #写入数据库
#     f_w = Fume_writer()
#     f_w.writer(fume_sum)


def main():
    login_fume_web()
    shop_name = ['','']
    u = Url()

    u1 = Url_params('食其家','2023-10-01','2023-10-31',5)
    urls = u.concatenate_url_with_condition(u1)
    f_s = FumeSpider()
    fume_sum = []

    for item in urls:
        html = f_s.fetch(item)
        fume_sum += Extract.extract_from_html(html)
    print(f'爬取总数为：{fume_sum}')
    #写入数据库

if __name__ == '__main__':
    main()