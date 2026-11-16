import finance.storage as storage
import pytest

def test_sacuvaj_i_ucitaj_transakcije(tmp_path, monkeypatch):
    test_fajl = tmp_path / "transakcije.json"

    monkeypatch.setattr(storage,"DATA_FILE", test_fajl)

    transakcije = [
        {
            "tip": "prihod",
            "iznos": 10000.0,
            "opis": "Plata"
        }
    ]

    storage.sacuvaj_transakcije(transakcije)

    ucitane = storage.ucitaj_transakcije()


    assert ucitane == transakcije

def test_ucitaj_transakcije_nepostojeci_fajl(tmp_path,monkeypatch):

    test_fajl = tmp_path / "nepostojeci.json"

    monkeypatch.setattr(storage, "DATA_FILE", test_fajl)

    transakcije = storage.ucitaj_transakcije()

    assert transakcije == []

def test_ucitaj_transakcije_ostecen_json(tmp_path,monkeypatch):
    test_fajl = tmp_path / "pokvaren.json"
    test_fajl.write_text("{ovo nije ispravan json", encoding="utf-8")

    monkeypatch.setattr(storage, "DATA_FILE", test_fajl)

    with pytest.raises(ValueError):
        storage.ucitaj_transakcije()

def test_ucitaj_transakcije_pogresan_format(tmp_path, monkeypatch):
    test_fajl = tmp_path / "pogresan.json"

    test_fajl.write_text(
        '{"ime": "Marko"}',
        encoding="utf-8"
    )

    monkeypatch.setattr(storage,"DATA_FILE", test_fajl)

    with pytest.raises(ValueError):
        storage.ucitaj_transakcije()

def test_ucitaj_transakcije_prazan_opis(tmp_path, monkeypatch):
    test_fajl = tmp_path / "prazan_opis.json"

    test_fajl.write_text(
        '[{"tip": "rashod", "iznos": 1500.0, "opis": "   "}]',
        encoding="utf-8"
    )

    monkeypatch.setattr(storage,"DATA_FILE", test_fajl)

    with pytest.raises(ValueError):
        storage.ucitaj_transakcije()

def test_ucitaj_transakcije_negativan_iznos(tmp_path, monkeypatch):
    test_fajl = tmp_path / "negativan_iznos.json"

    test_fajl.write_text('[{"tip": "rashod", "iznos": -1600, "opis": "namirnice"}]',
                         encoding="utf-8")

    monkeypatch.setattr(storage, "DATA_FILE", test_fajl)

    with pytest.raises(ValueError):
        storage.ucitaj_transakcije()