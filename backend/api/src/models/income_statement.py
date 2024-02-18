class IncomeStatement:
    __table__ = 'income_statements'
    columns = ['income_statement_id', 'company_id', 'period', 'revenue', 'net_income', 'reported_currency', 'eps']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
