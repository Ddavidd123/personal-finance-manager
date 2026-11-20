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


def dodaj_transakciju_u_bazu(
    tip: str,
    iznos: float,
    opis: str
    ) -> None:

    with sqlite3.connect(DB_FILE) as konekcija:
        konekcija.execute(
            """
            INSERT INTO transakcije (tip,iznos,opis)
            VALUES (?, ?, ?)
            """,
            (tip, iznos, opis)
        )

def ucitaj_transakcije_iz_baze() -> list[tuple]:
    with sqlite3.connect(DB_FILE) as konekcija:
        kursor = konekcija.execute(
            "SELECT id, tip, iznos, opis FROM transakcije"

        )

        return kursor.fetchall()

if __name__ == "__main__":
    kreiraj_bazu()

    transakcije = ucitaj_transakcije_iz_baze()

    for transakcija in transakcije:
        print(transakcija)

