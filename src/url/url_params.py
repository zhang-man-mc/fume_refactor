
from collections import namedtuple


# 形成url的参数
"""
Args:
    shop_name:店铺名称
    date_begin:开始时期
    date_end:结束日期
    page_num:需要爬取的页数
"""
Url_params = namedtuple('Url_params','shop_name,date_begin,date_end,page_num',defaults=[None,'2023-10-01','2023-10-31',1])