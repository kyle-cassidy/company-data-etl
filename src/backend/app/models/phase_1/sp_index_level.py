from sqlalchemy.orm import relationship, backref
from app import db
class SPIndexLevel:
    __table__ = 'sp_500_index_levels'
    columns = ['id','date','index_level', 'index_name']









    # def __init__(self, **kwargs):
    #     for key in kwargs.keys():
    #         if key not in self.columns:
    #             raise ValueError(f'{key} not in {self.columns}')
    #     for k, v in kwargs.items():
    #         setattr(self, k, v)
