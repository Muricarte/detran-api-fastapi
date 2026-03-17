from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True)
    placa = Column(String, unique=True)
    renavam = Column(String, unique=True)
    marca = Column(String)
    modelo = Column(String)
    cor = Column(String)
    ano = Column(Integer)
    situacao = Column(String)
    licenciamento = Column(String)

    proprietario = relationship("Proprietario", back_populates="veiculo")


class Motorista(Base):
    __tablename__ = "motoristas"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    cnh = Column(String)

    veiculos = relationship("Proprietario", back_populates="motorista")


class Proprietario(Base):
    __tablename__ = "proprietarios"

    id = Column(Integer, primary_key=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"))
    motorista_id = Column(Integer, ForeignKey("motoristas.id"))

    veiculo = relationship("Veiculo", back_populates="proprietario")
    motorista = relationship("Motorista", back_populates="veiculos")