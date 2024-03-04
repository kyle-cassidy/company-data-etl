from sqlalchemy.orm import relationship, backref
from app import db

class SPCompany(db.Model):
    
    __tablename__ = 'sp_500_companies'
    
    # columns = ['id','exchange', 'symbol', 'short_name', 'long_name', 'sector', 'industry', 'current_price', 'market_cap', 'ebitda', 'revenue_growth', 'city', 'state', 'country', 'long_business_summary', 'weight']
    
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String(10))
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    short_name = db.Column(db.String(100), nullable=False)
    long_name = db.Column(db.String(100), nullable=False)
    sector = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100))
    current_price = db.Column(db.Float)
    market_cap = db.Column(db.Float)
    ebitda = db.Column(db.Float)
    revenue_growth = db.Column(db.Float)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    long_business_summary = db.Column(db.String(1000))
    weight = db.Column(db.Float)

    def to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_
    
    def __repr__(self):
        return f'<SPCompany {self.short_name}>'

    # Relationships:

    # a company has many stocks
    stocks = db.relationship('SPStock', backref='company')

    # a company has many income statements
    income_statements = db.relationship('IncomeStatement', backref='company')
    
    # a company has many cash flow statements
    cash_flow_statements = db.relationship('CashFlowStatement', backref='company')

    # a company has many balance sheets
    balance_sheets = db.relationship('BalanceSheet', backref='company')


    # old ORM constructor
    # def __init__(self, **kwargs):
    #     for key in kwargs.keys():
    #         if key not in self.columns:
    #             raise ValueError(f'{key} not in {self.columns}')
    #     for k, v in kwargs.items():
    #         setattr(self, k, v)


