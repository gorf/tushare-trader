__version__ = '0.7.7'
__author__ = 'Jimmy Liu'
"""
for trading data
"""
from tushare_trader.stock.trading import (get_hist_data, get_tick_data,
                                   get_today_all, get_realtime_quotes,
                                   get_h_data, get_today_ticks,
                                   get_index, get_hists,
                                   get_k_data,
                                   get_sina_dd)

"""
for trading data
"""
from tushare_trader.stock.fundamental import (get_stock_basics, get_report_data,
                                       get_profit_data,
                                       get_operation_data, get_growth_data,
                                       get_debtpaying_data, get_cashflow_data,
                                       get_balance_sheet, get_profit_statement, get_cash_flow)

"""
for macro data
"""
from tushare_trader.stock.macro import (get_gdp_year, get_gdp_quarter,
                                 get_gdp_for, get_gdp_pull,
                                 get_gdp_contrib, get_cpi,
                                 get_ppi, get_deposit_rate,
                                 get_loan_rate, get_rrr,
                                 get_money_supply, get_money_supply_bal,
                                 get_gold_and_foreign_reserves)

"""
for classifying data
"""
from tushare_trader.stock.classifying import (get_industry_classified, get_concept_classified,
                                       get_area_classified, get_gem_classified,
                                       get_sme_classified, get_st_classified,
                                       get_hs300s, get_sz50s, get_zz500s,
                                       get_terminated, get_suspended)

"""
for macro data
"""
from tushare_trader.stock.newsevent import (get_latest_news, latest_content,
                                     get_notices, notice_content,
                                     guba_sina)

"""
for reference
"""
from tushare_trader.stock.reference import (profit_data, forecast_data,
                                     xsg_data, fund_holdings,
                                     new_stocks, sh_margins,
                                     sh_margin_details,
                                     sz_margins, sz_margin_details,
                                     top10_holders)

"""
for shibor
"""
from tushare_trader.stock.shibor import (shibor_data, shibor_quote_data,
                                  shibor_ma_data, lpr_data,
                                  lpr_ma_data)

"""
for LHB
"""
from tushare_trader.stock.billboard import (top_list, cap_tops, broker_tops,
                                     inst_tops, inst_detail)


"""
for utils
"""
from tushare_trader.util.dateu import (trade_cal, is_holiday)


"""
for DataYes Token
"""
from tushare_trader.util.upass import (set_token, get_token, get_broker,
                                set_broker, remove_broker)

from tushare_trader.datayes.api import *

from tushare_trader.internet.boxoffice import (realtime_boxoffice, day_boxoffice,
                                        day_cinema, month_boxoffice)

"""
for fund data
"""
from tushare_trader.fund.nav import (get_nav_open, get_nav_close, get_nav_grading,
                              get_nav_history, get_fund_info)

"""
for trader API
"""
from tushare_trader.trader.trader import TraderAPI


"""
for futures API
"""
from tushare_trader.futures.intlfutures import (get_intlfuture)


from tushare_trader.stock.globals import (global_realtime)


from tushare_trader.util.mailmerge import (MailMerge)
