from sqlalchemy.orm import Session
from . import models


def buscar_por_placa(db: Session, placa: str):
    return db.query(models.Veiculo).filter(
        models.Veiculo.placa == placa
    ).first()