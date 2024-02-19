


class Location:
    __table__ = 'locations'
    columns = ['location_id', 'name', 'country_id', 'state_id', 'city_id', 'zip_code', 'address']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

