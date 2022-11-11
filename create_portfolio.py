from model import portfolio_tracker_model as pf
from interface import fortuneo_data_extractor as ftn_data
from interface import stock_info_interface as smarket_info

if __name__ == '__main__':
    operations = ftn_data.extract_operations_from_csv("data/MCO_pea_operations.csv")
    pf_pea = pf.Portfolio(operations)
    pf_values = smarket_info.portfolio_last_stock_prices(pf_pea)
    pf_pea.set_ticker_values_from_prices(pf_values)
    pf_pea.summary()


