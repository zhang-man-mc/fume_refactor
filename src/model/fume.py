
class Fume():
    """网页表格上的条目"""
    def __init__(self,MV_Stat_Code: str,MV_Create_Time: str,MV_Data_Time: str,MV_Fan_Electricity: str,MV_Purifier_Electricity: str,MV_Fume_Concentration: str,MV_Fume_Concentration2: str) -> None:
        """_summary_

        Args:
            MV_Stat_Code (str): 设备编号
            MV_Create_Time (str): 创建时间
            MV_Data_Time (str): 数据时间
            MV_Fan_Electricity (str): 风机电
            MV_Purifier_Electricity (str): 净化器电流
            MV_Fume_Concentration (str): 进烟浓度
            MV_Fume_Concentration2 (str): 排烟浓度
        """
        self.MV_Stat_Code = MV_Stat_Code
        self.MV_Create_Time = MV_Create_Time
        self.MV_Data_Time = MV_Data_Time
        self.MV_Fan_Electricity  = MV_Fan_Electricity
        self.MV_Purifier_Electricity = MV_Purifier_Electricity
        self.MV_Fume_Concentration  = MV_Fume_Concentration
        self.MV_Fume_Concentration2 = MV_Fume_Concentration2


    def __repr__(self):
        return f'{self.__class__.__name__}(MV_Stat_Code={self.MV_Stat_Code!r},MV_Create_Time={self.MV_Create_Time!r},MV_Data_Time={self.MV_Data_Time!r},MV_Fan_Electricity={self.MV_Fan_Electricity!r},MV_Purifier_Electricity={self.MV_Purifier_Electricity!r},MV_Fume_Concentration={self.MV_Fume_Concentration!r},MV_Fume_Concentration2={self.MV_Fume_Concentration2!r})'

    # def __str__(self):
    #     print('调用了__str__')
    #     return f'{self.__class__.__name__}(MV_Stat_Code={self.MV_Stat_Code!r},MV_Create_Time={self.MV_Create_Time!r},MV_Data_Time={self.MV_Data_Time!r},MV_Fan_Electricity={self.MV_Fan_Electricity!r},MV_Purifier_Electricity={self.MV_Purifier_Electricity!r},MV_Fume_Concentration={self.MV_Fume_Concentration!r},MV_Fume_Concentration2={self.MV_Fume_Concentration2!r})'


if __name__ == '__main__':
    f1 = Fume(MV_Stat_Code='zhuoquan_31011020175002',MV_Create_Time='2023-10-31 07:22',MV_Data_Time='2023-10-31 07:20',MV_Fan_Electricity='0',MV_Purifier_Electricity='0',MV_Fume_Concentration='0',MV_Fume_Concentration2='0.012')
    f2 = Fume(MV_Stat_Code='zhuoquan_31011020175002',MV_Create_Time='2023-10-31 07:22',MV_Data_Time='2023-10-31 07:20',MV_Fan_Electricity='0',MV_Purifier_Electricity='0',MV_Fume_Concentration='0',MV_Fume_Concentration2='0.012')
    f3 = Fume(MV_Stat_Code='zhuoquan_31011020175002',MV_Create_Time='2023-10-31 07:22',MV_Data_Time='2023-10-31 07:20',MV_Fan_Electricity='0',MV_Purifier_Electricity='0',MV_Fume_Concentration='0',MV_Fume_Concentration2='0.012')
    f = [f1,f2,f3]
    # print(f)
    # print(f.__dict__)
    # v = vars(f)
    # print(v)
    # print(tuple(f.__dict__.values()))

    # a = ('zhuoquan_31011020175002', '2023-10-31 07:22', '2023-10-31 07:20', '0', '0', '0', '0.012')
    # print(Fume(*a))
    a = [i.__dict__ for i in f]
    print(a)

