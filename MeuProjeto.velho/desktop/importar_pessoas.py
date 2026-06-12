import sqlite3
import sys
import random
import datetime
import os

# Caminho do banco SQLite do Django
DB_PATH = "../MeuSite/db.sqlite3"


# ------------------------
# Funções auxiliares
# ------------------------

def gerar_email(nome: str) -> str:
    '''
    Gera um email fictício para uma pessoa com base em seu nome.
    O email é composto por uma versão "slug" do nome (tudo minúsculo, espaços substituídos por pontos)
    seguida de um número aleatório e o domínio "@example.com".
    Exemplo: "João Silva" -> "joao.silva1234@example.com"

    :param nome: O nome da pessoa para gerar o email
    :return: Um email fictício gerado a partir do nome
    '''
    base = nome.lower().replace(" ", ".")
    return f"{base}{random.randint(1,9999)}@example.com"

def gerar_telefone() -> str:
    '''
    Gera um número de telefone fictício.

    :return: Um número de telefone fictício no formato "+55XX9XXXXYYYY", onde XX é um código de área aleatório, e XXXXYYYY é um número de telefone aleatório
    '''
    return f"+55{random.randint(11, 99)}9{random.randint(1000,9999)}{random.randint(1000,9999)}"

def gerar_data_nascimento() -> str:
    '''
    Gera uma data de nascimento fictícia entre os anos de 1960 e 2005.
    A data é formatada como "YYYY-MM-DD".

    :return: Uma data de nascimento fictícia no formato "YYYY-MM-DD"
    '''
    ano = random.randint(1960, 2005)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)
    return f"{ano}-{mes:02d}-{dia:02d}"

def inserir_pessoa(nome: str):
    '''
    Insere uma nova pessoa no banco de dados SQLite com um nome fornecido e outros dados gerados aleatoriamente (idade, salário, email, telefone, data de nascimento).
    O campo de avatar é deixado como NULL.

    :param nome: O nome da pessoa a ser inserida no banco de dados
    '''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    idade = random.randint(18, 70)
    salario = round(random.uniform(1500, 12000), 2)
    email = gerar_email(nome)
    telefone = gerar_telefone()
    dtNasc = gerar_data_nascimento()

    cursor.execute("""
        INSERT INTO contatos_pessoa (avatar, nome, idade, salario, email, telefone, dtNasc)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (None, nome, idade, salario, email, telefone, dtNasc))

    conn.commit()
    conn.close()

# ------------------------
# Programa principal (CLI)
# ------------------------
def main() -> None:
    '''
    Função principal do programa.
    Verifica se o banco de dados SQLite existe, e se um arquivo de nomes foi fornecido como argumento de linha de comando.
    Se o arquivo de nomes for encontrado, lê os nomes e insere cada um como uma nova pessoa no banco de dados usando a função inserir_pessoa.
    Exibe mensagens de erro apropriadas se o banco de dados ou o arquivo de nomes não forem encontrados, e uma mensagem de sucesso ao final da importação.

    :return: None
    '''
    if not os.path.exists(DB_PATH):
        print(f"ERRO: Banco '{DB_PATH}' não encontrado. Ajuste a variável DB_PATH no código.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Uso: python importar_pessoas.py <arquivo_de_nomes.txt>")
        sys.exit(1)

    caminho = sys.argv[1]

    if not os.path.exists(caminho):
        print(f"ERRO: Arquivo '{caminho}' não encontrado.")
        sys.exit(1)

    with open(caminho, "r", encoding="utf-8") as f:
        nomes = [linha.strip() for linha in f.readlines() if linha.strip()]

    total = 0
    for nome in nomes:
        inserir_pessoa(nome)
        total += 1

    print(f"Importação concluída! {total} pessoas inseridas no banco SQLite.")


if __name__ == "__main__":
    main()
