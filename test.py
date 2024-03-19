
from src.fume_spider import Fume_spider
from src.database.save_to_database import Fume_writer
from src.url.url_parser import Url,Url_params
from src.login import *
from src.survey.extract import Extract



def main():
    f_s = Fume_spider()
    html = f_s.fetch('https://111')
    fume_sum = Extract.extract_from_html(html)
    print(f'爬取总数为：{fume_sum}')
    #写入数据库
    Fume_writer.writer(fume_sum)

if __name__ == '__main__':
    main()