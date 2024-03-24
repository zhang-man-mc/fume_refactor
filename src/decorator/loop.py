

import wrapt
from ..util.generate_url import GenerateUrl
from ..survey.extract import Extract
def loop_get_data_by_shop(shops: list):
    fume_data = []
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        nonlocal fume_data
        print('装饰器调用了')
        shop_url = GenerateUrl.generate_url(shops)
        print(f'url长度为:{len(shop_url)}')
        # 依次爬取url
        for url in shop_url:
            # 爬取
            html = wrapped(url, *args, **kwargs)
            # 提取
            fume_sum = Extract.extract_from_html(html)
            fume_data += fume_sum
        return fume_data
    return wrapper


if __name__ == '__main__':
    # function()
    pass
