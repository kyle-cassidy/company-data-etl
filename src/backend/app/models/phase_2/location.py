from api.src.db import db
import api.src.models as models


class Location:
    __table__ = 'locations'
    columns = ['id', 'name', 'country_id', 'state_id', 'city_id', 'zip_code', 'address']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

class Country:
    __table__ = 'countries'
    columns = ['id', 'name']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
            
class State:
    __table__ = 'states'
    columns = ['id', 'name', 'country_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def cities(self, cursor):
        query_str = "SELECT cities.* FROM cities WHERE state_id = %s"
        cursor.execute(query_str, (self.id,))
        records = cursor.fetchall()
        return db.build_from_records(models.City, records)
    
class City:
    __table__ = 'cities'
    columns = ['id', 'name', 'state_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def state(self, cursor):
        query_str = "SELECT states.* FROM states WHERE state_id = %s"
        cursor.execute(query_str, (self.state_id,))
        record = cursor.fetchone()
        return db.build_from_record(models.State, record)
    
class ZipCode:
    __table__ = 'zip_codes'
    columns = ['id', 'zip_code', 'city_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    @classmethod
    def find_by_code(self, code, cursor):
        query = f"""SELECT * FROM {self.__table__} WHERE code = %s """
        cursor.execute(query, (code,))
        record =  cursor.fetchone()
        obj = db.build_from_record(self, record)
        return obj

    def locations(self, cursor):
        query_str = "SELECT locations.* FROM locations WHERE zipcode_id = %s"
        cursor.execute(query_str, (self.id,))
        records = cursor.fetchall()
        return db.build_from_records(models.Location, records)

    def city(self, cursor):
        query_str = "SELECT cities.* FROM cities WHERE id = %s"
        cursor.execute(query_str, (self.city_id,))
        record = cursor.fetchone()
        return db.build_from_record(models.City, record)
    
