import json
from pathlib import Path
from .transactions import Transakcija

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "transakcije.json"
)

def sacuvaj_transakcije(transakcije: list[Transakcija]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as fajl:
        json.dump(transakcije,fajl, ensure_ascii=False, indent = 4)


def ucitaj_transakcije() -> list[Transakcija]:


    if not DATA_FILE.exists():
        return []

    try:

        with DATA_FILE.open("r", encoding="utf-8") as fajl:
            podaci = json.load(fajl)

    except json.JSONDecodeError:
        raise ValueError("Fajl sa transakcijama je ostecen!")

    #Validacije
    if not isinstance(podaci, list):
        raise ValueError("Podaci moraju biti lista transakcija!")

    for transakcija in podaci:
        if not isinstance(transakcija, dict):
            raise ValueError("Svaka transakcija mora biti recnik!")

        if "tip" not in transakcija:
            raise ValueError("Nedostaje tip transakcije!")

        if "iznos" not in transakcija:
            raise ValueError("Nedostaje iznos transakcije")

        if "opis" not in transakcija:
            raise ValueError("Nedostaje opis transakcije")

    return podaci

