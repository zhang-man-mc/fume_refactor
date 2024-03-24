import functools
import wrapt
from .util.generate_url import GenerateUrl


class LoopGetDataByShop:
    def __init__(self,fun,*,shops: list):
        # 根据店铺名称生成url
        self.shop_url = GenerateUrl.generate_url(shops)
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print(f'传入的参数为：{self.shop_url}')
        print(f'生成的url个数为：{len(self.shop_url)}')
        return self._loop(*args,**kwargs)

    def _loop(self,*args, **kwargs):
        """根据url爬取油烟页面"""
        for url in self.shop_url:
            self.fun(url,*args,**kwargs)


def loop_get_data_by_shop(**kwargs):
    return functools.partial(LoopGetDataByShop,**kwargs)

# @LoopByShop(shops=[1,2,3,4])
# def add(a,b):
#     print("加法函数被调用了")
#     return a + b


if __name__ == '__main__':
    pass
    # print(add)
