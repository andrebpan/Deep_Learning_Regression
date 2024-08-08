import pandas as pd

base = pd.read_csv('base_carros/datasets/autos.csv', encoding='ISO-8859-1')

base = base.drop('dateCrawled', axis=1)
base = base.drop('dateCreated', axis=1)
base = base.drop('nrOfPictures', axis=1)
base = base.drop('postalCode', axis=1)
base = base.drop('lastSeen', axis=1)
base = base.drop('name', axis=1)
base = base.drop('seller', axis=1)
base = base.drop('offerType', axis=1)

#valores de preços inconsistentes
i1 = base.loc[base.price <= 10]
print(i1)
base = base[base.price > 10]

i2 = base.loc[base.price > 350000]
print(i2)
base = base.loc[base.price < 350000]
