import time
import functools
import wrapt

class DelayedStart:
    """延迟执行"""
    def __init__(self,seconds=3):
        self.seconds = seconds

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs):
        print('延时装饰器执行了')
        time.sleep(self.seconds)
        print(f'睡眠了{self.seconds}秒')
        return wrapped(*args, **kwargs)




# class Add:
#     @DelayedStart(seconds=4)
#     def add(self):
#         print('add执行了')


if __name__ == '__main__':
    # Add().add()
    pass
