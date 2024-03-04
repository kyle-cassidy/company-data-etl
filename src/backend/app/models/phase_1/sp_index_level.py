from sqlalchemy.orm import relationship, backref
from app import db
class SPIndexLevel(db.Model):
    __tablename__ = 'sp_500_index_levels'
    # columns = ['id','date','index_level', 'index_name']
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False) #FIXME - change to date. ERROR: ValueError: Invalid isoformat string: '2/18/14'
    index_level = db.Column(db.Float, nullable=False)
    index_name = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_









    # def __init__(self, **kwargs):
    #     for key in kwargs.keys():
    #         if key not in self.columns:
    #             raise ValueError(f'{key} not in {self.columns}')
    #     for k, v in kwargs.items():
    #         setattr(self, k, v)
