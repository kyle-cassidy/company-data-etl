class StockMarketIndex:
    __table__ = 'stock_market_indexes'
    columns = ['id', 'name', 'symbol', 'exchange_id', 'description']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
