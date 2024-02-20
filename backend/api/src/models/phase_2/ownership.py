

class Ownership:
    __table__ = 'ownership'
    columns = ['id', 'company_id', 'holder_name', 'shares_held', 'date']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)