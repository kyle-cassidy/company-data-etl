class BalanceSheet:
    __table__ = 'balance_sheets'
    columns = ['balance_sheet_id', 'company_id', 'period', 'total_debt', 'total_equity', 'reported_currency']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
