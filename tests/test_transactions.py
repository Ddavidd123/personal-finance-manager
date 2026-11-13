import pytest
from finance.transactions import izracunaj_stanje, dodaj_transakciju

def test_izracunaj_stanje_prazna_lista():
    transakcije = []

    rezultat = izracunaj_stanje(transakcije)
    
    assert rezultat == 0.0

def test_izracunaj_stanje_sa_prihodom():
    transakcije = [
        {
            "tip": "prihod",
            "iznos": 10000.0,
            "opis": "Plata"
        }
    ]

    rezultat = izracunaj_stanje(transakcije)

    assert rezultat == 10000.0

def test_izracunaj_stanje_sa_prihodom_i_rashodom():
    transakcije = [
        {
            "tip": "prihod",
            "iznos": 10000.0,
            "opis": "plata"
        },

        {
            "tip": "rashod",
            "iznos": 2500.0,
            "opis": "troskovi"
        }

    ]

    rezultat = izracunaj_stanje(transakcije)

    assert rezultat == 7500.0

def test_dodaj_transakciju_negativan_iznos():
    transakcije = []

    with pytest.raises(ValueError):
        dodaj_transakciju(transakcije,"prihod",-500,"Plata")


    assert transakcije == []

def test_dodaj_transakciju_nula():
    transakcije = []

    with pytest.raises(ValueError):
        dodaj_transakciju(transakcije,"prihod",0.0,"Plata")


def test_dodaj_transakciju_uspesno():
    transakcije = []

    dodaj_transakciju(
        transakcije,
        "prihod",
        5000.0,
        "Bonus"
    )

    assert len(transakcije) == 1

    assert transakcije[0]["tip"] == "prihod"

    assert transakcije[0]["iznos"] == 5000.0

    assert transakcije[0]["opis"] == "Bonus"