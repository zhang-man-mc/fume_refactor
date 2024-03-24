

import wrapt

"""装饰器测试"""
def with_arguments(myarg1, myarg2):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print('装饰器调用了')
        print(f'参数为：{myarg1},{myarg2}')
        # url_1 = 'http://baidu.com'
        # url_2 = 'http://baidu1.com'
        url_1 = 1
        url_2 = 4

        return wrapped(url_1,url_2,*args, **kwargs)
    return wrapper

@with_arguments(1, 2)
def function(url,url_1):
    print('原函数调用了')
    print(f'url:{url},{url_1}')

class Add:

    @with_arguments(myarg1=5,myarg2=3)
    def add(self,a,b):
        print('类函数被调用了')
        print(f'加法结果为：{a+b}')



if __name__ == '__main__':
    # function()
    a = Add()
    a.add()