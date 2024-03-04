from sqlalchemy.orm import relationship, backref
from app import db
class SPStock(db.Model):
    __tablename__ = 'sp_500_stocks'
   
    #Date,Symbol,Adj Close,Close,High,Low,Open,Volume
    # columns = ['id','date', 'symbol', 'adj_close', 'close', 'high', 'low', 'open', 'volume']
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    adj_close = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    open = db.Column(db.Float)
    volume = db.Column(db.Float) 

    def to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict

    def __repr__(self):
        return f'<SPStock {self.symbol}>'
    
    # Relationships:
    # a stock has one company
    company = db.relationship('SPCompany', backref='stocks')

    





    # def __init__(self, **kwargs):
    #     for key in kwargs.keys():
    #         if key not in self.columns:
    #             raise ValueError(f'{key} not in {self.columns}')
    #     for k, v in kwargs.items():
    #         setattr(self, k, v)