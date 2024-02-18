class CashFlowStatement:
    __table__ = 'cash_flow_statements'
    columns = ['cashflow_statement_id', 'company_id', 'period', 'operating_activities', 'investing_activities', 'financing_activities', 'reported_currency']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)
