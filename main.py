import random


def gen_random(amount, start, stop):
    res = []
    for i in range(0,amount):
        res.append(random.randrange(start, stop+1))
    return(res)


def squared_cont(start,stop):
    mas = []
    for i in range(start,stop+1):
        mas.append(i+i**2)
    return mas


def sort(data):
    res = sorted(data, key=abs, reverse=False)
    return res


