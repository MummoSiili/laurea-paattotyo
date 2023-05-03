import sys, pickle, time

lista = []

# Kirjoita teksti ja palauta se aikaleimalla
def add_value():
    teksti = input('Kirjoita uusi merkintä: ')
    teksti = teksti + ':::' + time.strftime('%X %x') +'\n'
    return teksti

def main():
    # Testataan onko muistio.dat olemassa
    

    while True:

        # Tulostaa valikon
        print('''
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: ''', end='')

        valinta = input()

        # Valikon vaihtoehdot käsitellään str. Ei käännöstä int-muotoon
        if valinta == '1':
            with open('muistio.dat', 'rb') as file:
                sisalto = pickle.load(file)
            print(sisalto)
        elif valinta == '2':
            lista.append(add_value())
        elif valinta == '3':
            pass
        elif valinta == '4':
            pass
        elif valinta == '5':
            with open('muistio.dat', 'wb') as file:
                file.write(pickle.dump(lista))
            print('Lopetetaan.')
            sys.exit(0)

if __name__ == "__main__":
    main()
