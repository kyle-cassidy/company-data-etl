class CashFlowStatement:
    __table__ = 'cash_flow_statements'
    columns = ['id', 'company_id', 'period', 'net_operating_cashflow', 'net_investing_cashflow', 'net_financing_cashflow', 'net_change_in_cash', 'reported_currency']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
