from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, crud
from .seed import seed_db

app = FastAPI(title="API DETRAN Fake (SEM DOCKER)")

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    db = SessionLocal()

    if not db.query(models.Veiculo).first():
        print("🔄 Gerando +2000 veículos...")
        seed_db(db)
        print("✅ Banco pronto!")


@app.get("/consulta/{placa}")
def consulta(placa: str, db: Session = Depends(get_db)):

    veiculo = crud.buscar_por_placa(db, placa)

    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    proprietario = veiculo.proprietario[0].motorista

    return {
        "placa": veiculo.placa,
        "renavam": veiculo.renavam,
        "marca": veiculo.marca,
        "modelo": veiculo.modelo,
        "cor": veiculo.cor,
        "ano": veiculo.ano,
        "situacao": veiculo.situacao,
        "licenciamento": veiculo.licenciamento,
        "proprietario": {
            "nome": proprietario.nome,
            "cpf": proprietario.cpf,
            "cnh": proprietario.cnh
        }
    }