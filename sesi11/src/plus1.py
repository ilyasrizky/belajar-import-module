def Plus1(a):
    if a == 1:
        return (a)
    else:
        return (a + 1)


bil = int(input("Masukan Bilangan : "))

print("%d + 1 = %d" % (bil, Plus1(bil)))
