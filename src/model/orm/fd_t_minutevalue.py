from sqlalchemy import Column, Integer, Double, String,Boolean, DateTime
from .base import Base


class FdTMinutevalue(Base):
    __tablename__ = 'fd_t_minutevalue'

    MV_ID = Column(Integer, primary_key=True)
    MV_Stat_Code = Column(String(50))
    MV_Create_Time = Column(DateTime())
    MV_Data_Time = Column(DateTime())
    MV_Power_On_Time = Column(DateTime())
    MV_Recent_Down_Time = Column(DateTime())
    MV_signal = Column(Double())
    MV_Fan_Status = Column(Boolean)
    MV_Purifier_Status = Column(Boolean())
    MV_Fan_Electricity = Column(Double())
    MV_Purifier_Electricity = Column(Double())
    MV_Fume_Concentration = Column(Double())
    MV_Fume_Concentration2 = Column(Double())
    MV_PM = Column(Double())
    MV_NMHC = Column(Double())
    MV_Upload = Column(Double())

    # addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(MV_ID={self.MV_ID!r}, MV_Stat_Code={self.MV_Stat_Code!r}, MV_Create_Time={self.MV_Create_Time!r})"


