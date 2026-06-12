#!/usr/bin/env python3
import sqlite3
import argparse
from pathlib import Path


def listar_registros(db_path, table):
    db_path = Path(db_path)

    if not db_path.exists():
        print(f"❌ Banco não encontrado: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verificar se a tabela existe
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name=?;
    """, (table,))
    if not cursor.fetchone():
        print(f"❌ Tabela '{table}' não existe.")
        return

    # Obter nomes das colunas
    cursor.execute(f"PRAGMA table_info({table});")
    columns = [col[1] for col in cursor.fetchall()]

    # Buscar registros
    cursor.execute(f"SELECT * FROM {table};")
    rows = cursor.fetchall()

    print(f"\n📦 Banco: {db_path}")
    print(f"📋 Tabela: {table}")
    print(f"📊 Registros: {len(rows)}\n")

    # Imprimir cabeçalho
    print(" | ".join(columns))
    print("-" * 80)

    # Imprimir linhas
    for row in rows:
        print(" | ".join(str(x) for x in row))

    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Lista todos os registros de uma tabela SQLite")
    parser.add_argument("--db", required=True, help="Arquivo do banco SQLite")
    parser.add_argument("--table", required=True, help="Nome da tabela")

    args = parser.parse_args()
    listar_registros(args.db, args.table)


if __name__ == "__main__":
    main()
