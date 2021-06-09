class Feld:
    # spielbrettkonstruktor für ursprungszustand, wenn noch nicht gespielt wurde
    def __init__(self):
        self.status = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # züge
    def mach_zug(self, spielzelle, spieler):
        if self.ist_gueltiger_zug(spielzelle):
            self.status[spielzelle] = spieler.symbol
            return True
        return False

    def ist_gueltiger_zug(self, spielzelle):
        if self.status[spielzelle] == 0:
            return True
        else:
            return False

    def pruef_gewonnen(self, spieler):
        s = spieler.symbol
        if self.status[0] == s and self.status[1] == s and self.status[2] == s:
            return True
        elif self.status[3] == s and self.status[4] == s and self.status[5] == s:
            return True
        elif self.status[6] == s and self.status[7] == s and self.status[8] == s:
            return True
            
        elif self.status[0] == s and self.status[3] == s and self.status[6] == s:
            return True
        elif self.status[1] == s and self.status[4] == s and self.status[7] == s:
            return True
        elif self.status[2] == s and self.status[5] == s and self.status[8] == s:
            return True

        elif self.status[0] == s and self.status[4] == s and self.status[8] == s:
            return True
        elif self.status[2] == s and self.status[4] == s and self.status[6] == s:
            return True

    def ist_voll(self):
        for i in self.status:
            if i == 0:
                return False
        return True

    # mögliche zeichen
    def ausgebbares_zeichen(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"

    def feldausgabe(self):
        print(" " + self.ausgebbares_zeichen(self.status[0]) + " | " + self.ausgebbares_zeichen(self.status[1]) + " | " + self.ausgebbares_zeichen(self.status[2]) + " \n" +
              " " + self.ausgebbares_zeichen(self.status[3]) + " | " + self.ausgebbares_zeichen(self.status[4]) + " | " + self.ausgebbares_zeichen(self.status[5]) + " \n" +
              " " + self.ausgebbares_zeichen(self.status[6]) + " | " + self.ausgebbares_zeichen(self.status[7]) + " | " + self.ausgebbares_zeichen(self.status[8]) + " \n")

# spieler
class Spieler:
    # bekommt symbol zugewiesen
    def __init__(self, symbol):
        self.symbol = symbol


if __name__ == '__main__':
    # bekommt X
    spieler_a = Spieler(1)
    # bekommt 0
    spieler_b = Spieler(-1)
    # instanzvariable spielbrett
    feld = Feld()
    aktiver_spieler = spieler_a

    while not feld.ist_voll():
        feld.feldausgabe()
        try:
            spielzelle = int(input("Welche Position möchtest du markieren? [1-9]"))
        except ValueError:
            continue
        spielzelle = spielzelle - 1
        if spielzelle < 0 or spielzelle > 8:
            print("Gib eine Zahl zwischen 1 und 9 ein")
            continue
        if not feld.mach_zug(spielzelle, aktiver_spieler):
            print("Falscher Zug! Gib eine Zahl zwischen 1 und 9 ein")
            continue

        if feld.pruef_gewonnen(aktiver_spieler):
            print("Hast gewonnen! Glückwunsch.")
            break

        if aktiver_spieler == spieler_a:
            aktiver_spieler = spieler_b
        else:
            aktiver_spieler = spieler_a

    while feld.ist_voll():
        if not feld.pruef_gewonnen(aktiver_spieler):
            print("Unentschieden!")
            break