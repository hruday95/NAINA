import pandas as pd
from datetime import datetime


class event_manager():

    def __init__(self):
        self.data = pd.read_excel('src/engine/data/Bday.xlsx', sheet_name='Family')

    def event_finder(self):
        data = self.data.sort_values('Date')
        # event_month = data[]
        # upcoming_events = data[]
