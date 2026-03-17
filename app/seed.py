from faker import Faker
import random
from sqlalchemy.orm import Session
from .models import Veiculo, Motorista, Proprietario

fake = Faker("pt_BR")

MARCAS = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen"]
CORES = ["Preto", "Branco", "Prata", "Vermelho", "Azul"]
SITUACOES = ["ativo", "irregular", "roubado", "furto"]
LICENCIAMENTO = ["em dia", "vencido"]


def gerar_placa():
    letras = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))
    numeros = "".join(random.choices("0123456789", k=4))
    return letras + numeros


def seed_db(db: Session):

    for _ in range(2000):

        motorista = Motorista(
            nome=fake.name(),
            cpf=fake.cpf(),
            cnh=str(random.randint(100000000, 999999999))
        )

        veiculo = Veiculo(
            placa=gerar_placa(),
            renavam=str(random.randint(10000000000, 99999999999)),
            marca=random.choice(MARCAS),
            modelo=fake.word(),
            cor=random.choice(CORES),
            ano=random.randint(2000, 2024),
            situacao=random.choice(SITUACOES),
            licenciamento=random.choice(LICENCIAMENTO)
        )

        db.add(motorista)
        db.add(veiculo)
        db.flush()

        rel = Proprietario(
            veiculo_id=veiculo.id,
            motorista_id=motorista.id
        )

        db.add(rel)

    db.commit()