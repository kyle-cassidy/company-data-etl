class Company:
    __table__ = 'companies'
    columns = ['id', 'name', 'ticker_symbol', 'industry_id', 'sector_id', 'exchange_id', 'location_id', 'cik', 'isEtf', 'isActivelyTrading']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
