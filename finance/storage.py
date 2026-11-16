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


def validiraj_transakciju(transakcija: object) -> None:
    if not isinstance(transakcija,dict):
        raise ValueError("Svaka transakcija mora biti recnik!")

    if "tip" not in transakcija:
        raise ValueError("Nedostaje tip transakcije!")

    if "iznos" not in transakcija:
        raise ValueError("Nedostaje iznos transakcije")

    if "opis" not in transakcija:
        raise ValueError("Nedostaje opis transakcije")

    if transakcija["tip"] not in ("prihod", "rashod"):
        raise ValueError("Nepoznat tip transakcije")

    iznos = transakcija["iznos"]

    if isinstance(iznos, bool) or not isinstance(iznos, (int, float)):
        raise ValueError("Iznos mora biti broj!")

    if iznos <= 0:
        raise ValueError("Iznos mora biti veci od nule!")

    opis = transakcija["opis"]


    if not isinstance(opis, str) or not opis.strip():
        raise ValueError("Opis mora biti neprazan tekst!")

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
       validiraj_transakciju(transakcija)

    return podaci

