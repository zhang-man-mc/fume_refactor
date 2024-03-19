
from sqlalchemy import create_engine
class DataBase:

    """ 本机 """
    con_read = None
    con_write = None
    ip = 'localhost'
    user = 'root'
    password = '1234'
    port = 3306
    data_base_name = 're_conganize_fume'

   
    def connect_remote_database_read(self):
        """连接数据库"""
        if self.con_read == None or self.con_read.closed:
            engine = create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.ip}:{self.port}/{self.data_base_name}?charset=utf8",pool_recycle=3600, pool_size=3, max_overflow=0)
            self.con_read = engine.connect()
        return self.con_read

    def connect_remote_database_write(self):
        """ 写"""
        if self.con_write == None or self.con_write.closed:
            engine = create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.ip}:{self.port}/{self.data_base_name}?charset=utf8",pool_recycle=3600, pool_size=3, max_overflow=0)
            self.con_write = engine.connect()
        return self.con_write

# 其他文件导入此对象即可 
datebase_single_obj = DataBase()

if __name__ == '__main__':
    pass