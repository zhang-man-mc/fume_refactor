from typing import List
from .model.fume import Fume
from .database.db_connect import datebase_single_obj
import pandas as pd

class Fume_writer:

    # 写入分钟时间表
    def writer(self,list:List[Fume]):
        """写入数据库"""

        # 将包含实例的列表转为DataFrame格式
        fume_list = []
        for fume_instance in list:
            fume_dict = vars(fume_instance)
            fume_list.append(fume_dict)
        data = pd.DataFrame(fume_list,columns=['MV_Stat_Code','MV_Create_Time','MV_Data_Time','MV_Fan_Electricity','MV_Purifier_Electricity','MV_Fume_Concentration','MV_Fume_Concentration2'])
        print(data)

        data.to_sql(name="fd_t_minutevalue", con=datebase_single_obj.connect_remote_database_write(), if_exists="append",index=False,index_label=False)
        print("分钟数据表写入完成!")


if __name__ == '__main__':
    f1 = Fume(MV_Stat_Code='zhuoquan_31011020175001',MV_Create_Time='2023-10-30 07:22',MV_Data_Time='2023-10-31 07:20',MV_Fan_Electricity='0',MV_Purifier_Electricity='0',MV_Fume_Concentration='0',MV_Fume_Concentration2='0.012')
    f2 = Fume(MV_Stat_Code='zhuoquan_31011020175002',MV_Create_Time='2023-10-31 07:22',MV_Data_Time='2023-10-31 07:20',MV_Fan_Electricity='0',MV_Purifier_Electricity='0',MV_Fume_Concentration='0',MV_Fume_Concentration2='0.012')
    a = [f1,f2]
    f_w = Fume_writer()
    f_w.writer(a)