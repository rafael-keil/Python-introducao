def arrumaValor(hora, minuto, segundo):

    hora, minuto, segundo = arrumaHora(hora, minuto, segundo)
    hora, minuto, segundo = arrumaMinuto(hora, minuto, segundo)
    hora, minuto, segundo = arrumaSegundo(hora, minuto, segundo)

    return(hora, minuto, segundo)


def arrumaHora(hora, minuto, segundo):
    if hora > 24:
        hora = hora % 24

    if hora < 0:
        hora = 24 + hora

    return(hora, minuto, segundo)


def arrumaMinuto(hora, minuto, segundo):
    if minuto > 60:
        minuto = minuto % 60
        hora += 1
        hora, minuto, segundo = arrumaHora(hora, minuto, segundo)

    if minuto < 60:
        minuto = 60 + minuto
        hora -= 1
        hora, minuto, segundo = arrumaHora(hora, minuto, segundo)

    return(hora, minuto, segundo)


def arrumaSegundo(hora, minuto, segundo):
    if segundo > 60:
        segundo = segundo % 60
        minuto += 1
        hora, minuto, segundo = arrumaMinuto(hora, minuto, segundo)

    if segundo < 60:
        segundo = 60 + segundo
        minuto -= 1
        hora, minuto, segundo = arrumaMinuto(hora, minuto, segundo)

    return(hora, minuto, segundo)


class Relogio(object):
    def __init__(self, hour_, minute_, second_):
        self.hour = hour_
        self.minute = minute_
        self.second = second_

    def __str__(self):
        return "%0.2d:%0.2d:%0.2d" % (self.hour, self.minute, self.second)

    def __add__(self, other):

        hora = (self.hour + other.hour) % 24
        minuto = (self.minute + other.minute) % 60
        segundo = (self.second + other.second) % 60

        hora, minuto, segundo = arrumaValor(hora, minuto, segundo)

        return Relogio(hora, minuto, segundo)

    def __sub__(self, other):
        hora = self.hour - other.hour
        minuto = self.minute - other.minute
        segundo = self.second - other.second

        hora, minuto, segundo = arrumaValor(hora, minuto, segundo)

        return Relogio(hora, minuto, segundo)

    def __eq__(self, other):
        return (self.hour == other.hour and self.minute == other.minute and
                self.second == other.second)

    def __ne__(self, other):
        return not(self.hour == other.hour and self.minute == other.minute and
                   self.second == other.second)

    def __gt__(self, other):
        if self.hour > other.hour:
            return True

        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True

            elif self.minute == other.minute:
                if self.second > other.second:
                    return True

                else:
                    return False

            else:
                return False

        else:
            return False

    def __ge__(self, other):
        if self.hour < other.hour:
            return True

        elif self.hour == other.hour:
            if self.minute < other.minute:
                return True

            elif self.minute == other.minute:
                if self.second < other.second:
                    return True

                else:
                    return False

            else:
                return False

        else:
            return False

    def __lt__(self, other):
        if self.hour > other.hour:
            return True

        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True

            elif self.minute == other.minute:
                if self.second > other.second:
                    return True

                else:
                    return False

            else:
                return False

        else:
            return False

    def __le__(self, other):
        return (self < other) or (self == other)

#
# Exemplo de uso
#


c1 = Relogio(18, 37, 32)
c2 = Relogio(20, 0, 30)

print(type(c1))

print("Objeto c1 :", c1)
print("Objeto c2 :", c2)

print("c1  +  c2 =", c1 + c2)
print("c1  -  c2 =", c1 - c2)
print("c1  == c2 ?", c1 == c2)
print("c1  != c2 ?", c1 != c2)
print("c1  >  c2 ?", c1 > c2)
print("c1  <  c2 ?", c1 < c2)
print("c1  >= c2 ?", c1 >= c2)
print("c1  <= c2 ?", c1 <= c2)
