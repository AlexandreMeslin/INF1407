#!/usr/bin/env python3

'''
Script para listar tabelas e colunas de um banco SQLite
Uso:
    python listar.py --db caminho/para/banco.sqlite3
'''

import sqlite3
import argparse
from pathlib import Path


def listar_tabelas_com_colunas(db_path):
    print(f'🔍 Listando tabelas e colunas do banco: {db_path}\n')
    db_path = Path(db_path)

    if not db_path.exists():
        print(f"❌ Banco não encontrado: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # pega todas as tabelas (exceto internas)
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """)

    tabelas = [t[0] for t in cursor.fetchall()]

    if not tabelas:
        print("⚠️ Nenhuma tabela encontrada.")
        return

    for tabela in tabelas:
        print(f"\n📌 Tabela: {tabela}")
        print("-" * (10 + len(tabela)))

        cursor.execute(f"PRAGMA table_info({tabela});")
        colunas = cursor.fetchall()

        for cid, nome, tipo, notnull, default, pk in colunas:
            flags = []
            if pk:
                flags.append("PK")
            if notnull:
                flags.append("NOT NULL")
            if default is not None:
                flags.append(f"DEFAULT={default}")

            flag_str = f" ({', '.join(flags)})" if flags else ""
            print(f"  • {nome:20} {tipo}{flag_str}")

    conn.close()


def main():
    parser = argparse.ArgumentParser(
        description="Lista tabelas e colunas de um banco SQLite"
    )
    parser.add_argument(
        "--db",
        required=True,
        help="Caminho para o arquivo .sqlite3"
    )

    args = parser.parse_args()
    listar_tabelas_com_colunas(args.db)


if __name__ == "__main__":
    main()
