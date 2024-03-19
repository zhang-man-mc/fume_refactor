import urllib.parse 
from .url_params import Url_params
class Url:
    
    # def concatenate_url_with_condition(self,shop_name,date_begin,date_end,page_num)->list:
    #     """形成完整的url"""
    #     # 名字编码
    #     base_url = self.encoding_shop_name(shop_name)
    #     # 加上日期条件
    #     url_with_date = self.url_add_date(base_url,date_begin,date_end)
    #     # 加上页数条件
    #     sub_urls_wait_for_request = self.list_add_page(url_with_date,page_num)
    #     return sub_urls_wait_for_request
    
    def concatenate_url_with_condition(self,obj_params:Url_params)->list:
        """形成完整的url"""
        # 名字编码
        base_url = self.encoding_shop_name(obj_params.shop_name)
        # 加上日期条件
        url_with_date = self.url_add_date(base_url,obj_params.date_begin,obj_params.date_end)
        # 加上页数条件
        sub_urls_wait_for_request = self.list_add_page(url_with_date,obj_params.page_num)
        return sub_urls_wait_for_request



    def url_add_date(self,url,date_begin,date_end):     #url,年-月-日 2023-05-03
        url_date=url+'&key5='+date_begin+'&key6='+date_end
        return url_date
    
    def list_add_page(self,url,page_num):  # url中的i是页 ,apge_num表示爬取的页数  。url后面加上页的参数
        urls = [url+'&page'+'={}'.format(str(i)) for i in range(1,page_num+1)]
        return urls 
    
    def encoding_shop_name(self,shop_name):
        encoded_shop_name = urllib.parse.quote(urllib.parse.quote(shop_name))
       
        return 'http://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp?key1=&shop='+encoded_shop_name+'&pagesize=100'
    


if __name__ == '__main__':
    u = Url()
    u1 = Url_params('食其家','2023-10-01','2023-10-31',5)
    # urls = u.concatenate_url_with_condition('食其家','2023-10-01','2023-10-31',5)
    urls = u.concatenate_url_with_condition(u1)
    for item in urls:
        print(item)