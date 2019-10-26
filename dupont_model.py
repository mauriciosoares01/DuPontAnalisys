#   --------- DuPont's Model ---------

import pandas as pd

def calc_profit_margin(net_profit, sales):
    return float(net_profit)/float(sales)

def calc_asset_turnover(sales, assets):
    return float(sales)/float(assets)

def calc_leverage(assets, net_worth):
    return float(assets)/float(net_worth)
    
def calc_roa(profit_margin, asset_turnover):
    return profit_margin * asset_turnover

def calc_roe(roa, leverage):
    return roa * leverage
