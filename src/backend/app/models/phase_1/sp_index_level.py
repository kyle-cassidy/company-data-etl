from sqlalchemy.orm import relationship, backref
from app import db
class SPIndexLevel(db.Model):
    __tablename__ = 'sp_500_index_levels'
    # columns = ['id','date','index_level', 'index_name']
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    index_level = db.Column(db.Float, nullable=False)
    index_name = db.Column(db.String(50), nullable=False)









    # def __init__(self, **kwargs):
    #     for key in kwargs.keys():
    #         if key not in self.columns:
    #             raise ValueError(f'{key} not in {self.columns}')
    #     for k, v in kwargs.items():
    #         setattr(self, k, v)
