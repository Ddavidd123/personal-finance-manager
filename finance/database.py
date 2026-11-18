import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent.parent /"data"/"finance.db"

def kreiraj_bazu() -> None:
    DB_FILE.parent.mkdir(parents=True,exist_ok=True)

    with sqlite3.connect(DB_FILE) as konekcija:
        konekcija.execute(
            """
            CREATE TABLE IF NOT EXISTS transakcije(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tip TEXT NOT NULL,
                iznos REAL NOT NULL,
                opis TEXT NOT NULL
            );
            """
        )
