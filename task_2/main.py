
import pandas as pd
import pandasql as ps

our_data = pd.read_csv('price_list.csv', sep = '\t')
sample = pd.read_csv('sample_supplier.csv', sep = '\t')

our_data = our_data.drop_duplicates(['part_number', 'price'])
sample = sample.drop_duplicates(['part_number', 'price'])

sample['price'] = sample['price'].astype(str)
sample['price'] = sample['price'].str.replace('.', ',')

our_data['price'] = our_data['price'].astype(str)
our_data['price'] = our_data['price'].str.replace('.', ',')

pysqldf = lambda q: ps.sqldf(q, globals())              # creating pandasql environment

query = """
SELECT 
    o.part_number, 
    o.manufacturer, 
    o.price AS price_our_data, 
    s.price AS price_sample
FROM 
    our_data o
JOIN 
    sample s ON o.part_number = s.part_number AND o.manufacturer = s.manufacturer
"""

result_df = pysqldf(query)

result_df.to_csv('./price_comparison_result.csv', index = False, sep = '\t')