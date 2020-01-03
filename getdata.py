#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofgainesville.org", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofgainesville.org,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
#results = client.get("gvua-xt9q", limit=2000)
results = client.get("gvua-xt9q", where="id >= 220000049")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)


query = """
select
    incident type,
    offense date
where
    report date between 01/01/2020 and 01/03/2020
limit
    5
"""

results = client.get(socrata_dataset_identifier, query=query)
results

sodapysite = 'https://github.com/xmunoz/sodapy/blob/master/examples/soql_queries.ipynb'
