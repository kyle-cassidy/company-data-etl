from sqlalchemy.orm import relationship, backref
from app import db
class CashFlowStatement(db.Model):
    __tablename__ = 'cash_flow_statements'
    # columns = ['id', 'company_id', 'period', 'net_operating_cashflow', 'net_investing_cashflow', 'net_financing_cashflow', 'net_change_in_cash', 'reported_currency']
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('sp_500_companies.id'), nullable=False)
    period = db.Column(db.Date, nullable=False)
    net_operating_cashflow = db.Column(db.Float, nullable=False)
    net_investing_cashflow = db.Column(db.Float, nullable=False)
    net_financing_cashflow = db.Column(db.Float, nullable=False)
    net_change_in_cash = db.Column(db.Float, nullable=False)
    reported_currency = db.Column(db.String(3), nullable=False)
    
    def to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_
 
    def __repr__(self):
        return f'<CashFlowStatement {self.period} {self.company_id}>'





    # def __init__(self, **kwargs):
    #     for key in kwargs.keys():
    #         if key not in self.columns:
    #             raise ValueError(f'{key} not in {self.columns}')
    #     for k, v in kwargs.items():
    #         setattr(self, k, v)
