import pandas as pd
import inflection

df = pd.read_csv("zomato.csv")


# Remove espaços iniciais e finais de cada str para evitar conflito
for x in list(df.columns):
    text = f"df['{x}'].dtypes"
    if pd.eval(text) == 'object':
        df[x] = df[x].str.strip()

# Remove linhas do dataframe que estao vazias
df = df.dropna(axis=0).reset_index(drop=True)
df = df.drop_duplicates().reset_index(drop=True)


COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]

df["Country"] = df.loc[:, "Country Code"].apply(lambda x: country_name(x)) # Criando coluna nova a partir do dicionario Pre config


#Criação do Tipo de Categoria de Comida

def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

df["Price type"] = df.loc[:, "Price range"].apply(lambda x: create_price_tye(x))

#  Criação do nome das Core
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]

df["Color name"] = df.loc[:, "Rating color"].apply(lambda x: color_name(x))

df["Cuisines"] = df.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])

df.to_csv('C:\\Users\\Gabriel\\Desktop\\CODES\\projeto_1\\zomato_clean.csv', index=False)