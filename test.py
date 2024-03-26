
from src.fume_spider import FumeSpider
from src.database.save_to_database import Fume_writer
from src.url.url_parser import Url,Url_params
from src.login import *
from src.survey.extract import Extract
from src.request_.request_test_data import LocalFumePage
from src.request_.request import RemoteFumePage
from src.util.generate_url import GenerateUrl
from src.config import config
from src.decrator import loop_get_data_by_shop
from src.decorator.loop import loop_get_data_by_shop
from src.util.remove_dup import RemoveDup
from src.model.orm.fd_t_minutevalue import FdTMinutevalue
from src.model.fume import Fume
# 测试获取本地和远程数据
# def main():
#     local_fume_page = LocalFumePage()
#     remote_fume_page = RemoteFumePage()
#     f_s = FumeSpider()
#
#     # 请求本地网页
#     html = f_s.fetch('https://111',local_fume_page)
#
#     # 请求远程网页
#     # html = f_s.fetch('https://111',remote_fume_page)
#
#
#     fume_sum = Extract.extract_from_html(html)
#     print(f'爬取总数为：{fume_sum}')
#     # 写入数据库
#     # Fume_writer.writer_orm(fume_sum)


# 测试装饰器获取本地数据
def main():
    local_fume_page = LocalFumePage()
    f_s = FumeSpider()

    # 装饰器请求本地网页
    fume_data = f_s.fetch(local_fume_page)

    print(f'遍历完毕：结果为：fume_data:{fume_data}')
    print(f'遍历完毕：长度为：{len(fume_data)}')

    # 去重
    removed_dup = RemoveDup.remove_duplicates_cls(fume_data)
    print(f'去重后,结果为：removed_dup：{removed_dup}')
    print(f'去重后：长度为：{len(removed_dup)}')

    # Fume_writer.writer_orm(removed_dup)

# 测试类装饰器
# @loop_get_data_by_shop(shops=['吉刻联盟','大成海鲜'])
# def add(url,page,*args,**kwargs):
#     print("加法函数被调用了")
#     print(url)
#     print(f"page:{page}")
#     return url

# 测试方法装饰器
# @loop_get_data_by_shop(shops=['吉刻联盟','大成海鲜'])
# def add(url):
#     print("加法函数被调用了")
#     print(url)
#     return 1


if __name__ == '__main__':
    main()

    # 测试生成url
    # url = GenerateUrl.generate_url(config['development'].shop_name)
    # print(url)

    # 测试装饰器
    # add()


    # 测试ORM写入数据库
    # Fume_writer.select()
    # f1 = Fume(MV_Stat_Code='1', MV_Create_Time='2023-10-31 07:22',
    #           MV_Data_Time='2023-10-31 07:20', MV_Fan_Electricity='0', MV_Purifier_Electricity='0',
    #           MV_Fume_Concentration='0', MV_Fume_Concentration2='0.012')
    # f2 = Fume(MV_Stat_Code='2', MV_Create_Time='2023-10-31 07:22',
    #           MV_Data_Time='2023-10-31 07:20', MV_Fan_Electricity='0', MV_Purifier_Electricity='0',
    #           MV_Fume_Concentration='0', MV_Fume_Concentration2='0.012')
    # f3 = Fume(MV_Stat_Code='3', MV_Create_Time='2023-10-31 07:22',
    #           MV_Data_Time='2023-10-31 07:20', MV_Fan_Electricity='0', MV_Purifier_Electricity='0',
    #           MV_Fume_Concentration='0', MV_Fume_Concentration2='0.012')
    # f = [f1, f2, f3]
    #
    # Fume_writer.writer_orm(f)

