from typing import TypedDict, Literal


class Transakcija(TypedDict):
    tip: Literal["prihod", "rashod"]
    iznos: float
    opis: str


def dodaj_transakciju(transakcije: list[Transakcija],
    tip: Literal["prihod", "rashod"],
    iznos: float,
    opis: str) -> None:

    if iznos <= 0:
        raise ValueError("Iznos mora biti veci od 0")

    nova_transakcija: Transakcija = {
        "tip": tip,
        "iznos": iznos,
        "opis": opis
    }

    transakcije.append(nova_transakcija)


def izracunaj_stanje(transakcije: list[Transakcija]) -> float:
    stanje = 0.0
    for transakcija in transakcije:
        if transakcija["tip"] == "prihod":
            stanje += transakcija["iznos"]
        else:
            stanje -= transakcija["iznos"]

    return stanje

