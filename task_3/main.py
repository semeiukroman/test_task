
import pandas as pd


column_positions = [(34, 44), (605, 637), (88, 110), (136, 141), (156, 157)]                                                #   crating set of tuples to save columns positions in txt

data = pd.read_fwf('PP0006_MULTI.txt', encoding='ISO-8859-2', colspecs=column_positions, header = None)

data.columns = ['indeks', 'nazwa', 'cena', 'ilosc w opakowaniu', 'grupa rabatowa']


data = data[(data['cena'] > 0) & (data['ilosc w opakowaniu']) > 0]                                                          #   editing data in frame
data.loc[:, 'cena'] = data['cena'].astype(str)                                                                              #
data.loc[:, 'cena'] = data['cena'].apply(lambda x: x[:-2] + ',' + x[-2:])                                                   #   adding correct price display


data = data.drop_duplicates()
data = data.dropna()


data.to_csv('./price_list_task3.csv', index = False, sep = '\t')