#!/usr/bin/env python3
import sqlite3
import argparse
from pathlib import Path


def listar_tabelas(cursor):
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """)
    return [t[0] for t in cursor.fetchall()]


def remover_tabelas(db_path, force=False):
    db_path = Path(db_path)

    if not db_path.exists():
        print(f"❌ Banco não encontrado: {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    tabelas = listar_tabelas(cursor)

    if not tabelas:
        print("⚠️ Nenhuma tabela encontrada.")
        return

    print(f"📦 Banco: {db_path}")
    print(f"📋 Tabelas encontradas: {len(tabelas)}\n")

    for tabela in tabelas:
        if force:
            confirmar = "s"
        else:
            confirmar = input(f"❓ Remover tabela '{tabela}'? (s/N): ").strip().lower()

        if confirmar == "s":
            print(f"🗑️ Removendo {tabela}...")
            cursor.execute(f"DROP TABLE IF EXISTS {tabela};")
            conn.commit()
        else:
            print(f"⏩ Pulando {tabela}")

    conn.close()
    print("\n✅ Operação finalizada.")


def main():
    parser = argparse.ArgumentParser(
        description="Remove interativamente todas as tabelas de um banco SQLite"
    )
    parser.add_argument("--db", required=True, help="Arquivo do banco SQLite")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Remove todas as tabelas sem perguntar (PERIGOSO!)"
    )

    args = parser.parse_args()
    remover_tabelas(args.db, force=args.force)


if __name__ == "__main__":
    main()
