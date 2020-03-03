import numpy as np
import pandas as pd


def return_df(file_path):
    df = pd.read_csv(file_path, encoding='ISO-8859-2')
    df = df.rename(columns={' market ': 'market', ' funding_total_usd ': 'funding_total_usd'})
    return df


def remove_na(df):
    df = df.dropna(subset=['name', 'country_code', 'status', 'market'])
    df = df.drop(['founded_at', 'founded_month', 'founded_quarter', 'founded_year', 'state_code', 'homepage_url'], axis=1)
    df = df.fillna('None')
    return df

# function to convert string object to int64
def object_to_int(s): 
    return int(''.join(s.strip().split(',')))
    

# return the operating, acquired, closed percentage of startups in each market
def status_per_market(df, market, status):
    percentages = []
    for _, curr in enumerate(status):
        startup_status = df[(df['market'] == market) & (df['status'] == curr)].shape[0]
        total_startup = df[df['market'] == market].shape[0]
        percentages.append((startup_status/total_startup)*100)
    # list containing percent of operating, acquired, closed startups for each market
    return percentages
        

def funding_per_market(df, market):
    # tf_per_mkt : total funding for each market
    BILLION = 1000000000
    tf_all = df.funding_total_usd.sum()
    total_funding_per_mkt = df[(df['market'] == market)].funding_total_usd.sum()
    angel = df[(df['market'] == market)].angel.sum()
    vc = df[(df['market'] == market)].venture.sum()
    others = (total_funding_per_mkt - (angel + vc))/BILLION
    
    return total_funding_per_mkt/BILLION, (total_funding_per_mkt/tf_all)*100, angel/BILLION, vc/BILLION, others
    
    
def return_table(df, markets, status):
    print(f"Market/Startup\t operating  acquired  closed  funding(B) funding(%) angel(B) vc(B)")
    print(f"="*84)
    
    for market in markets: 
        spm = status_per_market(df, market, status)
        tf, fpm, angel, vc, _ = funding_per_market(df, market)
        nmarket = market + ' ' * (max([len(m) for m in markets]) - len(market))
        
        print(f"{nmarket}\t{spm[0]:.1f}\t{spm[1]:.1f}\t{spm[2]:.1f}\t{tf:.2f}\t\t{fpm:.1f}\t{angel:.2f}\t{vc:.2f}")




