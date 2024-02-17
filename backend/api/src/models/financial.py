# FIXME refactor into the income statement, balance sheet, and cash flow statement
class IncomeStatement:
    __table__ = 'income_statements'
    columns = ['financial_id', 'company_id', 'period', 'revenue', 'net_income', 'eps', 'reported_currency']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

class BalanceSheet:
    __table__ = 'balance_sheets'
    columns = ['financial_id', 'company_id', 'period', 'total_debt', 'total_equity', 'reported_currency']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

class CashFlowStatement:
    __table__ = 'cash_flow_statements'
    columns = ['financial_id', 'company_id', 'period', 'operating_activities', 'investing_activities', 'financing_activities', 'reported_currency']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
