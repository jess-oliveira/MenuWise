from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models
from app import schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) # parecido com CREATE TABLE IF NOT EXISTS

app = FastAPI() #variável para chamar o método importado FastAPI

def get_db(): # função pegar database / abrir conexão.
    db = SessionLocal() #   variável que da o clique para abrir a conexão (pega a chave e entra na casa)
    try:
        yield db #  conceder/fornecer , tipo tente usar db (usar a casa)
    finally: #  finalmente , independente doque acontecer
        db.close() #    feche (tranque a casa ao sair)

@app.get("/")
def read_root():
    return {"message": "MenuWise running"}