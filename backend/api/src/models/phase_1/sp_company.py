class SPCompany:
    __table__ = 'sp_500_companies'
    columns = ['id','exchange', 'symbol', 'short_name', 'long_name', 'sector', 'industry', 'current_price', 'market_cap', 'ebitda', 'revenue_growth', 'city', 'state', 'country', 'long_business_summary', 'weight']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
