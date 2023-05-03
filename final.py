import sys, pickle, time

# Kirjoita teksti ja palauta se aikaleimalla
def add_value():
    teksti = input('Kirjoita uusi merkintä: ')
    teksti = teksti + ':::' + time.strftime('%X %x')
    return teksti

def change_marking(lista, lista_index):
    print(lista[lista_index])
    print('Anna uusi teksti:', end='')
    teksti = input()
    teksti = teksti + ':::' + time.strftime('%X %x')
    lista[lista_index] = teksti
    return lista

def delete_marking(lista, lista_index):
    print(f'Poistettiin merkintä {lista[lista_index]}')
    lista.pop(lista_index)
    return lista

def main():
    # Testataan onko muistio.dat olemassa
    try:
        file = open('muistio.dat', 'rb')
        lista = pickle.load(file)
        file.close()
    except:
        print('Virhe tiedostossa, luodaan uusi muistio.dat.')

        with open('muistio.dat', 'wb') as file:
            lista = []
            pickle.dump(lista, file)

    # Suoritetaan ohjelmaa niin kauan kunnes valitaan lopeta.
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
            for value in lista:
                print(value, end='')
        elif valinta == '2':
            lista.append(add_value())
        elif valinta == '3':
            print(f'Listalla on {len(lista)} merkintää.')
            print('Mitä niistä muutetaan?: ', end='')
            lista_index = int(input())
            lista_index = lista_index - 1
            lista = change_marking(lista, lista_index)
        elif valinta == '4':
            print(f'Listalla on {len(lista)} merkintää.')
            print('Mitä niistä poistetaan?: ', end='')
            lista_index = int(input())
            lista_index = lista_index - 1
            lista = delete_marking(lista, lista_index)
        elif valinta == '5':
            with open('muistio.dat', 'wb') as file:
                pickle.dump(lista, file)
            print('Lopetetaan.')
            sys.exit(0)

if __name__ == "__main__":
    main()
