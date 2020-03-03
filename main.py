import numpy as np
import pandas as pd
import utils
from plots import status_plot, funding_plot
from collections import defaultdict



FILE_PATH = 'data/investments_VC.csv'
df = utils.return_df(FILE_PATH)
df = utils.remove_na(df)

df.funding_total_usd = df.funding_total_usd.apply(lambda x: '0' if x == ' -   ' else x)
df.funding_total_usd = df.funding_total_usd.apply(lambda x: utils.object_to_int(x))



# Convert ' Games ' to 'Games' -- strip spaces
df.market = df.market.apply(lambda x: x.strip())

# top 20 markets with most startups
top_market = list(df.market.value_counts()[:5].index)
status = ['operating', 'acquired', 'closed'] 
#print(f"B = Billions \t M= millions \n")
utils.return_table(df, top_market, status)


markets = top_market

def return_dict(df, markets, query):
    d = defaultdict(dict)   # a defaultdict of dict
    dd = []    # list to wrap around the above defaultdict


    for i, market in enumerate(markets):

        '''
        Step 1:     This function creates a defaultdict containing dictionary with labels and 
                    percentages in this case labels is the status (operating, closed etc.) of 
                    the company and the sizes contain the percentages corresponding to each status.

        Step 2:     Wrap the defaultdict created in the previous step with list.
        '''
        
        # step 1
        if query == 'status':
            d[i] = {'labels': status, 'sizes': utils.status_per_market(df, market, status)}
        
            # step 2
            dd.append(d[i])     # list of defualtdict

        if query == 'funding':
            _, _, angel, vc, other = utils.funding_per_market(df, market)
            d[i] = {'labels': ['vc', 'angel', 'others'], 'sizes': [angel, vc, other]}
            dd.append(d[i])
    
    return dd

status_dd = return_dict(df, markets, 'status')   
funding_dd = return_dict(df, markets, 'funding')

status_plot(df, markets, status_dd)
funding_plot(df, markets, funding_dd)