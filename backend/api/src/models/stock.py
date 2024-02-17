class Stock:
    __table__ = 'stocks'
    columns = ['price_id', 'company_id', 'date', 'open_price', 'high_price', 'low_price', 'close_price', 'adjusted_close_price', 'volume']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)