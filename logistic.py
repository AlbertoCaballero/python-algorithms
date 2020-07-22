
import matplotlib.pyplot as plt

#x now
xa = 0.2

#x latter
xb = 0

#factor
r = 0

#ranges
start = 0
finish = 45

#values
val = []
rs = []

for x in range(start, finish):
    r = r + 0.1
    xb = r*xa*(1-xa)
    rs.append(r)
    val.append(xb)
    xa = xb

fig = plt.figure(figsize=(50,50))
ax = fig.add_subplot(111)

ax.set(xlabel='Lambda', ylabel='Population', title='Logistic Equation')
ax.scatter(rs, val)

plt.show()

