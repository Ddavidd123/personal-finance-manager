from finance.transactions import (
    Transakcija,
    dodaj_transakciju,
    izracunaj_stanje
)

def prikazi_meni() -> None:
    print("===== PERSONAL FINANCE MANAGER =====")
    print("1. Dodaj prihod")
    print("2. Dodaj rashod")
    print("3. Prikazi stanje")
    print("4. Prikazi sve transakcije")
    print("0. Izlaz")

def pokreni_aplikaciju() -> None:
    transakcije: list[Transakcija] = []

    while True:

        prikazi_meni()

        izbor = input("Izaberi opciju: ").strip()

        if izbor == "1":
            try:
                iznos = float(input("Unesi iznos: "))
                opis = input("Unesi opis: ").strip()

                dodaj_transakciju(
                    transakcije,
                    "prihod",
                    iznos,
                    opis
                )
                print("Prihod je uspesno dodat!")
            except ValueError as greska:
                print(f"Greska: {greska}")

        elif izbor == "2":
            try:
                iznos = float(input("Unesi iznos: "))
                opis = input("Unesite opis: ").strip()

                dodaj_transakciju(
                    transakcije,
                    "rashod",
                    iznos,
                    opis
                )
                print("Rashod uspesno dodat!")
            except ValueError as greska:
                print(f"Greska: {greska}")

        elif izbor == "3":
            stanje = izracunaj_stanje(transakcije)
            print(f"Trenutno stanje: {stanje:.2f} RSD")

        elif izbor == "4":
            print(transakcije)



        elif izbor == "0":
            print("Dovidjenja!")
            break
        else:
            print("Nepostojeca opcija")



if __name__ == "__main__":
    pokreni_aplikaciju()


