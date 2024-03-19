from ..model.fume import Fume
from bs4 import BeautifulSoup as bs

class Extract:
    # 从HTML中提取需要的数据

    @staticmethod
    def extract_from_html(html: str) -> list[Fume]:
        soup = bs(html, 'html.parser')
        # 找到所有的tr标签
        rows = soup.find_all('tr')

        # 提取表格中的数据
        result = []
        for row in rows[1:]:
            data = []
            cols = row.find_all('td')
            for col in cols:
                if col.find('div'):
                    # 如果td中包含div，则单独提取其内容
                    div_content = col.find('div').text.strip()
                    # 返回元素的文本内容 搜索tag的直接子节点
                    td_content = ''.join(col.find_all(text=True, recursive=False)).strip()
                    data.append(td_content)
                    data.append(div_content)
                else:
                    # 如果td中不包含div，则直接提取td的内容
                    td_content = col.text.strip()
                    data.append(td_content)
            del (data[-2:])
            del (data[2])

            # 给映射对象类
            result.append(
                Fume(MV_Stat_Code=data[2], MV_Create_Time=data[-1], MV_Data_Time=data[-2], MV_Fan_Electricity=data[6],
                     MV_Purifier_Electricity=data[7], MV_Fume_Concentration=data[4], MV_Fume_Concentration2=data[5]))

        # 打印提取的数据
        # for i in result:
        #     print(i)
        print(f'数量为:{len(result)}')
        return result