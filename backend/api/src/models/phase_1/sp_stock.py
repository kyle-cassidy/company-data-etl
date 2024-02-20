class SPStock:
    __table__ = 'sp_500_stocks'
    #Date,Symbol,Adj Close,Close,High,Low,Open,Volume
    columns = ['id','date', 'symbol', 'adj_close', 'close', 'high', 'low', 'open', 'volume']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)