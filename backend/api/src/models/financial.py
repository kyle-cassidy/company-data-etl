
# FIXME refactor into the income statement, balance sheet, and cash flow statement
class Financial:
    __table__ = 'financials'
    columns = ['financial_id', 'company_id', 'period', 'revenue', 'net_income', 'eps', 'total_debt', 'total_equity', 'reported_currency']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)