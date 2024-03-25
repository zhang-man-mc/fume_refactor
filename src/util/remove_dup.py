

from collections import namedtuple
from ..model.fume import Fume


class RemoveDup:
    @staticmethod
    def remove_duplicates_cls(fume_data: list[Fume]) -> list[Fume]:
        """数据为类实例"""
        if fume_data is None:
            return None
        list_fume_data = [tuple(fume.__dict__.values()) for fume in fume_data]
        has_removed_dup =  list(set(list_fume_data))
        unique_fume =  [Fume(*f) for f in has_removed_dup]
        return unique_fume

    @staticmethod
    def remove_duplicates_nametuple(fume_data: list[Fume]) -> list[Fume]:
        """数据为nametuple类型"""
        if fume_data is None:
            return None
        list_fume_data = [tuple(fume) for fume in fume_data]
        has_removed_dup =  list(set(list_fume_data))
        unique_fume =  [Fume(*f) for f in has_removed_dup]
        return unique_fume



# a = ('niha1o',1,)
# b = ('niha1o',1,)
# c = ('nihao',2,)
#
# d = [a,b,c]
# f = list(set(d))
# print(f)
#
# name_t = [Person(*f) for f in f]
# print(name_t)
