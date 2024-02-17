

class AnalystRating:
    __table__ = 'analyst_ratings'
    columns = ['rating_id', 'company_id', 'analyst_name', 'rating', 'date']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
