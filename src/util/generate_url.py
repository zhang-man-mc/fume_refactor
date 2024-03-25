import urllib.parse
from ..config import config


class GenerateUrl:
    base_url = 'http://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp?key1=&shop='

    # 对中文店铺名进行二次加密
    @staticmethod
    def _parse_shop_name(shop_name):
        return urllib.parse.quote(urllib.parse.quote(shop_name))

    @staticmethod
    def _url_add_date(url, begin_date, end_date, page_size: int = 100):
        return url + '&key5=' + begin_date + '&key6=' + end_date


    @staticmethod
    def _list_url(url, page_num: int = 100):
        """
            url中的i是页
            page_num表示爬取的页数
        """
        urls = [url + '&page' + '={}'.format(str(i)) for i in range(1, page_num + 1)]
        return urls

    @staticmethod
    def generate_url(shops: list = None) -> dict:
        """
        url =
        {'吉刻联盟': ['http://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp, 'http://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp?=5']}

        """
        if shops is None:
            return
        urls = {}
        for shop in shops:
            parse_shop = GenerateUrl._parse_shop_name(shop)
            url_shop = GenerateUrl.base_url + parse_shop +'&pagesize=' + str(config['development'].page_size)
            url_date = GenerateUrl._url_add_date(url_shop, config['development'].begin_date, config['development'].end_date)
            urls.update({shop: [url_date + f'&page={i}' for i in range(1, config['development'].page_num+1)]})
        return urls

    # @staticmethod
    # def generate_url(shops: list = None) -> list:
    #     if shops is None:
    #         return
    #     urls = []
    #     for shop in shops:
    #         parse_shop = GenerateUrl._parse_shop_name(shop)
    #         url_shop = GenerateUrl.base_url + parse_shop + '&pagesize=' + str(config['development'].page_size)
    #         url_date = GenerateUrl._url_add_date(url_shop, config['development'].begin_date,
    #                                              config['development'].end_date)
    #         urls += [url_date + f'&page={i}' for i in range(1, config['development'].page_num + 1)]
    #     return urls


if __name__ == '__main__':
    print(GenerateUrl.generate_url(config['development'].shop_name))
