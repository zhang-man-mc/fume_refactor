from collections import namedtuple

Shop = namedtuple('Shop',['name','url'],defaults=(None,None))

if __name__ == '__main__':
    s = Shop('食其家','www')
    print(s.name)
    pass
