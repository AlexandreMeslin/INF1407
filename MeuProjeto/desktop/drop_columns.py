#!/usr/bin/env python3
import sqlite3
import argparse
from pathlib import Path


def get_columns(cursor, table):
    cursor.execute(f"PRAGMA table_info({table});")
    return [row[1] for row in cursor.fetchall()]  # row[1] = column name


def recreate_table_without_column(conn, cursor, table, drop_col):
    # obter schema original
    cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table}';")
    create_sql = cursor.fetchone()[0]

    # remover coluna do CREATE TABLE
    cols = get_columns(cursor, table)
    new_cols = [c for c in cols if c != drop_col]

    if not new_cols:
        print("❌ Não é permitido remover todas as colunas!")
        return

    # construir novo CREATE TABLE
    cursor.execute(f"PRAGMA table_info({table});")
    col_defs = cursor.fetchall()
    new_defs = [c for c in col_defs if c[1] != drop_col]
    new_schema = ", ".join([f"{c[1]} {c[2]}" for c in new_defs])

    temp_table = f"{table}_tmp"

    print(f"🔧 Recriando tabela sem a coluna '{drop_col}'...")

    cursor.execute(f"CREATE TABLE {temp_table} ({new_schema});")
    cursor.execute(f"INSERT INTO {temp_table} ({', '.join(new_cols)}) SELECT {', '.join(new_cols)} FROM {table};")
    cursor.execute(f"DROP TABLE {table};")
    cursor.execute(f"ALTER TABLE {temp_table} RENAME TO {table};")

    conn.commit()


def interactive_drop_columns(db_path, table):
    db_path = Path(db_path)
    if not db_path.exists():
        print(f"❌ Banco não encontrado: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cols = get_columns(cursor, table)
    if not cols:
        print("❌ Tabela não existe ou não tem colunas.")
        return

    print(f"\n📦 Banco: {db_path}")
    print(f"📋 Tabela: {table}")
    print(f"🔎 Colunas encontradas: {cols}\n")

    for col in cols:
        confirm = input(f"❓ Remover coluna '{col}'? (s/N): ").strip().lower()
        if confirm == "s":
            recreate_table_without_column(conn, cursor, table, col)
        else:
            print(f"⏩ Pulando {col}")

    conn.close()
    print("\n✅ Finalizado.")


def main():
    parser = argparse.ArgumentParser(description="Remove interativamente colunas de uma tabela SQLite")
    parser.add_argument("--db", required=True, help="Arquivo do banco SQLite")
    parser.add_argument("--table", required=True, help="Nome da tabela")

    args = parser.parse_args()
    interactive_drop_columns(args.db, args.table)


if __name__ == "__main__":
    main()
