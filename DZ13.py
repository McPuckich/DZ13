from random import randint

sp = [randint(0, 10) for i in range(5)]
# sp = [2, 3, 3, 4]
print(sp)


def sred(chis):  # chis = summ(a) => sred(summ(sp))
    def wrap(b):  # wrap()
        arif = chis(b) / len(b)  # chis(b) = summ(sp)  chis() = summ()
        print('Среднее арифметическое чисел =', arif)
        return arif

    return wrap


@sred
def summ(a):  #  sred(summ(a))
    s = 0
    for i in a:
        s += i
    print("Сумма чисел =", s)
    return s


summ(sp)
