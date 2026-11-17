from finance.storage import validiraj_transakciju
import pytest

def test_validiraj_transakciju():
    transakcija = {
        "tip": "poklon",
        "iznos": 5000.0,
        "opis": "Rodjendan"
    }

    with pytest.raises(ValueError):
        validiraj_transakciju(transakcija)


def test_validiraj_transakciju_ispravna():
    transakcija = {
        "tip": "prihod",
        "iznos": 5000.0,
        "opis": "Plata"
    }


    validiraj_transakciju(transakcija)

@pytest.mark.parametrize("iznos",[-500,0,"hiljadu",True])
def test_validiraj_transakciju_neispravan_iznos(iznos):
    transakcija = {
        "tip": "prihod",
        "iznos": iznos,
        "opis": "Plata"
    }

    with pytest.raises(ValueError):
        validiraj_transakciju(transakcija)

@pytest.mark.parametrize("opis",["", "   ", 123, None])
def test_validiraj_transakciju_neispravan_opis(opis):
    transakcija = {
        "tip": "rashod",
        "iznos": 1500.0,
        "opis": opis
    }

    with pytest.raises(ValueError):
        validiraj_transakciju(transakcija)