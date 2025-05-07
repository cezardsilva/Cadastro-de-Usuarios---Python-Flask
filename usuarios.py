import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd 
from urllib.parse import quote_plus

# Configuração do banco
password = quote_plus("@CDias2015")
engine = create_engine(f'mysql+pymysql://root:{password}@localhost:3306/afiliados')

def get_users():
    """Consulta todos os usuários e retorna uma lista de dicionários corretamente."""
    with engine.connect() as con:
        query = text("SELECT * FROM usuarios")
        result = con.execute(query)
        return [dict(row._mapping) for row in result]  # Ajuste aqui


def add_user(nome, idade, email, telefone):
    """Adiciona um usuário ao banco de dados."""
    with engine.begin() as con:  # Usa begin() para garantir commit automático
        query = text("INSERT INTO usuarios (nome, idade, email, telefone) VALUES (:nome, :idade, :email, :telefone)")
        con.execute(query, {"nome": nome, "idade": idade, "email": email, "telefone": telefone})


def delete_user(user_id):
    """Exclui um usuário do banco de dados."""
    with engine.begin() as con:
        query = text("DELETE FROM usuarios WHERE id = :id")
        con.execute(query, {"id": user_id})

