
import pandas as pd

def createBrandReport(dataframe):                                                                                   #   creating brand report in txt file function
    brands = dataframe.groupby('manufacturer').size()
    with open('./brand_report.txt', 'w', encoding='utf-8') as file:
        for brand, count in brands.items():
            file.write(f'{brand} - {count} rows\n')

data = pd.read_csv('data.csv', sep='\t' )                                                             # reading source files
price = pd.read_csv('prices.csv', sep = '\t')
quantity = pd.read_csv('quantity.csv', sep = '\t', header=None)


quantity.columns = ['part_number', 'quantity']                                                                      #   adding headers to quantity df

quantity['quantity'] = pd.to_numeric(quantity['quantity'].str.replace('>', ''))                                     #   converting quantity values to numeric type
quantity = quantity[quantity['quantity'] > 0]                                                                       #   to get rid of 0
                                         									    #   then converting quantities back to
                                                     								    #   object type
quantity['quantity'] = quantity['quantity'].apply(lambda x: '>10' if x > 10 else str(x))


price['price'] = price['price'].str.replace(',', '.').astype(float)                                                 #   converting price to float type
price = price[price['price'] > 0]                                                                                   #   getting rid of 0 values


merged_df = pd.merge(data, price, on='part_number')                                                                 #   merging dataframes into one frame
merged_df = pd.merge(merged_df, quantity, on='part_number')


final_df = merged_df.sort_values('part_number').drop_duplicates()                                                   #   sorting merged dataframe and getting rid of duplicates
final_df.dropna(subset=['part_number', 'manufacturer', 'price', 'quantity'], inplace=True)                          #   drop rows with empty values

final_df.to_csv('./price_list.csv', index = False, sep = '\t')
createBrandReport(final_df)




