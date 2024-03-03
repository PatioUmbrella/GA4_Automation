import os
import pandas as pd
from jj_data_connector.ga4 import GA4Report, Metrics, Dimensions

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'api_key.json'
property_id = '353700449'

# creating GA4Report object instance
ga4 = GA4Report(property_id)

# variables
dimension_list = ['date', 'browser']
metric_list = ['totalUsers', 'bounceRate']
date_range1 = ('2023-11-01', '2023-11-30')
date_range2 = ('2023-12-01', '2023-12-31')

# run the GA4 report
report = ga4.run_report(
    dimension_list, 
    metric_list, 
    date_ranges=[date_range1, date_range2],
    row_limit=10,
    offset_row=0
)

# remember to execute lines one by one!

# report.keys()
# print(report['response'])

print(report['headers'])
print(report['rows'])

df = pd.DataFrame(columns=report['headers'], data=report['rows'])
print(df)

# export to CSV and Excel files
df.to_csv("c:/Users/Samsquanch/Desktop/No Half Measures/work/reports/report1.csv", index=False)
