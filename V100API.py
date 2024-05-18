import os
import pandas as pd
import csv
from jj_data_connector.ga4 import GA4Report, Metrics, Dimensions

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'apiKey.json'
property_id = id

ga4 = GA4Report(property_id)

dimension_list = ['date', 'browser']
metric_list = ['totalUsers', 'bounceRate']
date_range1 = ('2023-1-01', '2023-12-31')
date_range2 = ('2024-01-01', '2024-12-31')

report = ga4.run_report(
    dimension_list, 
    metric_list, 
    date_ranges=[date_range1, date_range2],
    row_limit=10,
    offset_row=10
)
report['row_count']

print(report['response'])

report['headers']
report['rows']
df = pd.DataFrame(columns=report['headers'], data=report['rows'])
print(df)

df.to_csv('demo1.csv', index=False)