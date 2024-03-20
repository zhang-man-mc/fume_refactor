
from abc import ABC,abstractmethod


class FumeWebPage(ABC):
    """油烟页面"""
    @abstractmethod
    def get_page(self,url: str) -> str:
        raise NotImplementedError()