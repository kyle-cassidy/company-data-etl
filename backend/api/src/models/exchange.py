

class Exchange:
    __table__ = 'exchanges'
    columns = ['exchange_id', 'name', 'short_name', 'country_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)