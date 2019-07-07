import numpy as np

t = np.array([2, 3, 5, 7])
nc = np.array([250, 300, 200, 250])
sc = np.sum(nc)
p = nc / sc
pa = np.cumsum(p)
np.random.seed(0)
u = np.random.random(size=100)
j = 0  # contador de datos de U
di = np.empty(shape=[len(u)])
for x in u:
    i = 0  # contador de prob
    while i < len(pa):
        if x < pa[i]:
            di[j] = t[i]
            i = len(pa)
        else:
            i = i + 1
    j = j + 1

print(di)

