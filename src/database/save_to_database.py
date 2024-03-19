# 保存到数据库
import pandas as pd
from ..model.fume import Fume
from .db_connect import datebase_single_obj

class Fume_writer:
    # def __init__(self):
    #     # 传递数据库连接
    #     self._con = datebase_single_obj.con_write()

    @staticmethod
    def writer(fume: list[Fume]) -> None:
        if len(fume) == 0:
            print('无数据写入！')
            return None
        data = pd.DataFrame([vars(x) for x in fume], columns=['MV_Stat_Code', 'MV_Create_Time', 'MV_Data_Time', 'MV_Fan_Electricity',
                                           'MV_Purifier_Electricity', 'MV_Fume_Concentration',
                                           'MV_Fume_Concentration2'])
        # test3 要写入的数据表，这样写的话要提前在数据库建好表
        data.to_sql(name="fd_t_minutevalue", con=datebase_single_obj.connect_remote_database_write(), if_exists="append",index=False,index_label=False)
        print("分钟数据表写入完成!")


