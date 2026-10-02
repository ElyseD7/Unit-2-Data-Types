def asses(w):
    list_T = 0
    list_S = 0
    for i in range(len(w)):
        if w[i] == "t" or "T":
            list_T += 1
        if w[i] == "s" or "S":
            list_S += 1
    if list_T > list_S:
        print("English")
    if list_T < list_S:
        print("French")
    if list_T == list_S:
        print("French")

asses("sous")


