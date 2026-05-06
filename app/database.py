import os
from dotenv import load_dotenv
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv() # Carrega as variáveis do arquivo .env

DATABASE_URL = os.getenv("DATABASE_URL") # Busca a URL lá do .env

engine = create_engine(DATABASE_URL) # conhecta a url(endereço da casa)
SessionLocal = sessionmaker( #  mantem a conexão aberta para uso (andar/mexer na casa)
    autocommit=False,   # você decide quando salvar
    autoflush=False,    # evita envio automático
    bind=engine #   vínculo
)
Base = declarative_base() # método de sqlalchemy declara que o que receber Base de parametro herdará sua estrutura de tabela.