
from .url.url_parser import Url
from .login import *
from requests import HTTPError,Timeout,ConnectionError,RequestException
from .get_web_page import FumeWebPage
from .decorator.loop_get_data import loop_get_data_by_shop


class FumeSpider:
    @loop_get_data_by_shop(shops=['吉刻联盟'])
    def fetch(self, url: str, page: FumeWebPage):
        try:
            r = page.get_page(url)
        except ConnectionError as e:
            print('网络连接异常: ', e)
        except Timeout as e:
            print('连接超时: ', e)
        except HTTPError as e:
            print(f'HTTP错误, 状态码: {e.response.status_code}, {e}')
        except RequestException as e:
            print('请求异常: ', e)
        except ValueError as e:
            print('响应解析异常: ', e)
        return r

# class FumeSpider:
#
#
#     # def fetch(self,url)->List[Fume]:
#     #     """爬取网页表格数据"""
#     #
#     #     r = request_get(url).text
#     #     soup = bs(r,'html.parser')
#     #
#     #     # 找到所有的tr标签
#     #     rows = soup.find_all('tr')
#     #
#     #     # 提取表格中的数据
#     #     result = []
#     #     for row in rows[1:]:
#     #         data = []
#     #         cols = row.find_all('td')
#     #         for col in cols:
#     #             if col.find('div'):
#     #                 # 如果td中包含div，则单独提取其内容
#     #                 div_content = col.find('div').text.strip()
#     #                 # 返回元素的文本内容 搜索tag的直接子节点
#     #                 td_content = ''.join(col.find_all(text=True, recursive=False)).strip()
#     #                 data.append(td_content)
#     #                 data.append(div_content)
#     #             else:
#     #                 # 如果td中不包含div，则直接提取td的内容
#     #                 td_content = col.text.strip()
#     #                 data.append(td_content)
#     #         del (data[-2:])
#     #         del (data[2])
#     #
#     #         # 给映射对象类
#     #         result.append(Fume(MV_Stat_Code=data[2],MV_Create_Time=data[-1],MV_Data_Time=data[-2],MV_Fan_Electricity=data[6],MV_Purifier_Electricity=data[7],MV_Fume_Concentration=data[4],MV_Fume_Concentration2=data[5]))
#     #
#     #     # 打印提取的数据
#     #     for i in result:
#     #         print(i)
#     #     print(f'数量为:{len(result)}')
#     #
#     #     return result
#
#     def fetch(self, url: str) -> str:
#         """爬取网页表格数据"""
#         try:
#             r = request_get_test(url)
#         except ConnectionError as e:
#             print('网络连接异常: ', e)
#         except Timeout as e:
#             print('连接超时: ', e)
#         except HTTPError as e:
#             print(f'HTTP错误, 状态码: {e.response.status_code}, {e}')
#         except RequestException as e:
#             print('请求异常: ', e)
#         except ValueError as e:
#             print('响应解析异常: ', e)
#         return r


if __name__ == '__main__':
    # 登录
    login_fume_web()
    u = Url()
    urls = u.concatenate_url_with_condition('杨记齐齐哈尔烤肉','2023-10-01','2023-10-31',1)
    f_s = FumeSpider()
    for item in urls:
        f_s.fetch(item)