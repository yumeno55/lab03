def puzirek(a, obr = False):
    N = len(a)
    if (obr == False):
        i = 0
        while i < N - 1:
            j = 0
            while j < N - 1 - i:
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                j += 1
            i += 1
    else:
        i = 0
        while i < N - 1:
            j = 0
            while j < N - 1 - i:
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                j += 1
            i += 1
    return a


a = [32, 45, 3, 89, 37, 22, 14, 5, 8]
print(puzirek(a, True))