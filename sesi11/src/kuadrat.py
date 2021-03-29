def kuadrat(x, y):
    if y == 0:
        return 1
    else:
        return x * kuadrat(x, y-1)


x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))

print("%d kuadrat %d = %d" % (x, y, kuadrat(x, y)))
