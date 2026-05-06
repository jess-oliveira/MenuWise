import pandas as pd
from app.database import SessionLocal
from app.models import Food

df = pd.read_csv("data/lista_alimentos.csv") #  variável que vai usar o método read_cvs de panda para ler o arquivo (local do arquivo).


for col in ["protein", "carb", "fat"]: #     col vai percorrer onde tiver protein,carb,fat.
    df[col] = df[col].str.replace(",", ".").astype(float) # vai acessar cada coluna do dataframe = vai pegar essa coluna tratar como str vai substituir (, por .) e transformar em float.

df = df.dropna(subset=["food"]) #   tira da lista a linha que a coluna food estiver vazia. 
df["food"] = df["food"].str.strip() #   tira os espaços da coluna food.


db = SessionLocal() # conecta no banco


for _, row in df.iterrows(): # .iterrows() é um método do panda que desempacota o df, ele trás dois indices obrigatórios, usamos _ porque não usaremos o primeiro indice, e o segundo indice é o conteudo da linha.
    food = Food( # acessamos aqui nossa classe Food para conectar a ela as informações abaixo:
        food=row["food"], #food vai receber da linha a informação referente a food, e assim por diante.
        protein=row["protein"],
        carb=row["carb"],
        fat=row["fat"]
    )
    db.add(food) #vai adcionar a db as informações organizadas em food

db.commit()
db.close()

print("Importação concluída")