
#%%
import pandas as pd
import numpy as np
from collections import namedtuple
#from haversine import haversine
#import plotly.express as px
#import plotly.graph_objects as go
#import folium
#from PIL import Image
#import inflection


df = pd.read_csv("zomato_clean.csv")

#%%
"""GERAL"""
#1. Quantos restaurantes únicos estão registrados?
df['Restaurant Name'].nunique()

#2. Quantos países únicos estão registrados?
df['Country Code'].nunique()


#3. Quantas cidades únicas estão registradas?

df['City'].nunique()

#4. Qual o total de avaliações feitas?

df['Aggregate rating'].count()

#5. Qual o total de tipos de culinária registrados?

df['Cuisines'].nunique()

"""PAIS"""

#1. Qual o nome do país que possui mais cidades registradas?
df.loc[:,['City','Country']].groupby(['Country']).count().sort_values(by=['City'], ascending=False).reset_index().iat[0,0]

#2. Qual o nome do país que possui mais restaurantes registrados?
df.loc[:,['Restaurant ID','Country']].groupby(['Country']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index().iat[0,0]

#3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?

df.loc[df['Price range'] == 4,['Price range','Country']].groupby(['Country']).count().sort_values(by=['Price range'], ascending=False).reset_index().iat[0,0]

#4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
df.loc[:,['Cuisines','Country']].groupby(['Country']).nunique().sort_values(by=['Cuisines'], ascending=False).reset_index().iat[0,0]

#5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
df.loc[:,['Votes','Country']].groupby(['Country']).nunique().sort_values(by=['Votes'], ascending=False).reset_index().iat[0,0]

#6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
df.loc[df['Is delivering now'] == 1,['Is delivering now','Country']].groupby(['Country']).nunique().sort_values(by=['Is delivering now'], ascending=False).reset_index().iat[0,0]

#7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
df.loc[:,['Has Table booking','Country']].groupby(['Country']).nunique().sort_values(by=['Has Table booking'], ascending=False).reset_index().iat[0,0]

#8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
df.loc[:,['Votes','Country']].groupby(['Country']).mean().sort_values(by=['Votes'], ascending=False).reset_index().iat[0,0]

#9. Qual o nome do país que possui, na média, a maior nota média registrada?
df.loc[:,['Votes','Country']].groupby(['Country']).mean().sort_values(by=['Votes'], ascending=False).reset_index().iat[0,0]
#10. Qual o nome do país que possui, na média, a menor nota média registrada?

df.loc[:,['Votes','Country']].groupby(['Country']).mean().sort_values(by=['Votes']).reset_index().iat[0,0]

#11. Qual a média de preço de um prato para dois por país?
np.round(df.loc[:,['Average Cost for two','Country']].groupby(['Country']).mean().reset_index(),2)  

"""Cidade"""
#1. Qual o nome da cidade que possui mais restaurantes registrados
df.loc[:,['Restaurant ID','City']].groupby(['City']).count().sort_values(by=['City'], ascending=False).reset_index().iat[0,0]
#2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
#4?

df.loc[df['Aggregate rating'] >= 4,['Aggregate rating','City']].groupby(['City']).count().sort_values(by=['City'],ascending=False).reset_index().iat[0,0]
#3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
#2.5?
df.loc[df['Aggregate rating'] <= 2.5,['Aggregate rating','City']].groupby(['City']).count().sort_values(by=['City'],ascending=False).reset_index().iat[0,0]
#4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
np.round(df.loc[:,['Average Cost for two','City']].groupby(['City']).mean().sort_values(by=['City'], ascending=False).reset_index(),2).iat[0,0]
#5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
#distintas?
df.loc[:,['City','Cuisines']].groupby(['City']).count().sort_values(by=['Cuisines'], ascending=False).reset_index().iat[0,0]
#6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
#reservas?

df.loc[df['Has Table booking'] ==1,['Restaurant Name','City']].groupby(['City']).count().sort_values(by=['Restaurant Name'], ascending=False).reset_index().iat[0,0]

#7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
#entregas? 
df.loc[df['Is delivering now'] ==1,['Restaurant Name','City']].groupby(['City']).count().sort_values(by=['Restaurant Name'], ascending=False).reset_index().iat[0,0]

#8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
#aceitam pedidos online?
df.loc[df['Has Online delivery'] ==1,['Restaurant Name','City']].groupby(['City']).count().sort_values(by=['Restaurant Name'], ascending=False).reset_index().iat[0,0]

"""Restaurantes"""
#1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
df.loc[:,['Aggregate rating','Restaurant Name']].groupby(['Restaurant Name']).max().sort_values(by=['Restaurant Name'],ascending=False).reset_index().iat[0,0]


#2. Qual o nome do restaurante com a maior nota média?
df.loc[:,['Aggregate rating','Restaurant Name']].groupby(['Restaurant Name']).max().sort_values(by=['Aggregate rating'],ascending=False).reset_index().iat[0,0]

#3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
#pessoas?
df.loc[:,['Average Cost for two','Restaurant Name']].groupby(['Restaurant Name']).max().sort_values(by=['Average Cost for two'],ascending=False).reset_index().iat[0,0]

#4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
#média de avaliação?
df.loc[df['Cuisines'] =='Brazilian',['Aggregate rating','Cuisines','Restaurant Name']].groupby(['Restaurant Name','Cuisines']).mean().sort_values(by=['Aggregate rating']).reset_index().iat[0,0]


#5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
#possui a maior média de avaliação?
df.loc[df['Cuisines'] =='Brazilian',['Aggregate rating','Cuisines','Restaurant Name']].groupby(['Restaurant Name','Cuisines']).mean().sort_values(by=['Aggregate rating'],ascending=False).reset_index().iat[0,0]

#6. Os restaurantes que aceitam pedido online são também, na média, os
#restaurantes que mais possuem avaliações registradas?

np.round(df.loc[:,['Has Online delivery','Votes']].groupby(['Has Online delivery']).mean().reset_index().sort_values(by='Votes', ascending=False),2)    

#7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
#possuem o maior valor médio de um prato para duas pessoas?

np.round(df.loc[:,['Has Table booking','Average Cost for two']].groupby(['Has Table booking']).mean().reset_index().sort_values(by='Average Cost for two', ascending=False),2)

#8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
#possuem um valor médio de prato para duas pessoas maior que as churrascarias
#americanas (BBQ)?
jp = np.round(df.loc[(df['Cuisines'] == 'Japanese') & (df['Country'] == 'United States of America'),['Average Cost for two']].mean().iat[0],2)
bbq = np.round(df.loc[(df['Cuisines'] == 'BBQ') & (df['Country'] == 'United States of America'),['Average Cost for two']].mean().iat[0],2)
res = namedtuple("Result", ['jp','bbq'])
res(jp,bbq)

"""Tipos de Culinária"""
#1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
#restaurante com a maior média de avaliação?
df['Cuisines'] =='Italian'

df.loc[df['Cuisines'] =='Italian',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating', ascending=False).iat[0,0]
#2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
#restaurante com a menor média de avaliação?

df.loc[df['Cuisines'] =='Italian',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating').iat[0,0]
#3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
#restaurante com a maior média de avaliação?
df.loc[df['Cuisines'] =='American',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating', ascending=False).iat[0,0]


#4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
#restaurante com a menor média de avaliação?
df.loc[df['Cuisines'] =='American',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating').iat[0,0]

#5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
#restaurante com a maior média de avaliação?
df.loc[df['Cuisines'] =='Arabian',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating', ascending=False).iat[0,0]

#6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
#restaurante com a menor média de avaliação?
df.loc[df['Cuisines'] =='Arabian',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating').iat[0,0]


#7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
#restaurante com a maior média de avaliação?

df.loc[df['Cuisines'] =='Japanese',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating', ascending=False).iat[0,0]

#8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
#restaurante com a menor média de avaliação?
df.loc[df['Cuisines'] =='Japanese',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating').iat[0,0]

#9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
#restaurante com a maior média de avaliação?
df.loc[df['Cuisines'] =='Home-made',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating',ascending=False).iat[0,0]


#10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
#restaurante com a menor média de avaliação?
df.loc[df['Cuisines'] =='Home-made',['Cuisines','Restaurant Name','Aggregate rating']].groupby(['Restaurant Name','Cuisines']).mean().reset_index().sort_values(by='Aggregate rating').iat[0,0]

#11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
#pessoas?

np.round(df.loc[:,['Cuisines','Average Cost for two']].groupby(['Cuisines']).mean().reset_index().sort_values(by='Average Cost for two', ascending=False),2).iat[0,0]


#12. Qual o tipo de culinária que possui a maior nota média?
np.round(df.loc[:,['Cuisines','Aggregate rating']].groupby(['Cuisines']).mean().reset_index().sort_values(by='Aggregate rating', ascending=False),2).iat[0,0]


#13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
#online e fazem entregas?

df.loc[(df['Has Online delivery'] == 1) & (df['Is delivering now'] == 1),['Cuisines','Restaurant ID']].groupby(['Cuisines']).count().reset_index().sort_values(by='Restaurant ID', ascending=False)