import datetime as dt
import os
import pandas as pd
from pytrends.request import TrendReq


class GoogleTrendAPI:
    """
    get Google Trend data. Input: keyword, start date, end date. Output: data frame save to csv
    call method: self.get_data
    """

    def __init__(self):
        self.pytrend = TrendReq()  # connect to Google

    def _build_payload(self):
        return self.pytrend.build_payload(kw_list=['bitcoin'])

    def _build_time_series_data(self):
        time_df = self.pytrend.interest_over_time()
        return time_df