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