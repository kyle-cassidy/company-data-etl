from sqlalchemy.orm import relationship, backref
from app import db
class IncomeStatement(db.Model):
    __tablename__ = 'income_statements'
    # columns = ['id', 'company_id', 'period', 'revenue', 'net_income', 'eps', 'reported_currency' ]
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('sp_companies.id'), nullable=False)
    period = db.Column(db.Date, nullable=False)
    revenue = db.Column(db.Float, nullable=False) 
    net_income = db.Column(db.Float, nullable=False) 
    eps = db.Column(db.Float, nullable=False) 
    reported_currency = db.Column(db.String(3), nullable=False) 

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
