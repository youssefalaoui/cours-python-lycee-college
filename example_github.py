##### Liens utiles
# parameteres: https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html
# scatter: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html
# loi normale https://fr.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/normal-distributions-library/a/normal-distributions-review
# random : https://docs.python.org/fr/3/library/random.html
# styles: https://matplotlib.org/stable/gallery/style_sheets/fivethirtyeight.html

####################################
####################################
# Graphe simple
####################################
####################################


import matplotlib.pyplot as plt

plt.plot([1,3,4],[2,1,6])

plt.show()


####################################
####################################
# Graphe de statistiques
####################################
####################################



import matplotlib.pyplot as plt

regions = ['Île-de-France', 'Champagne-Ardenne', 'Picardie', 'Haute-Normandie', 'Centre']

salaires_moins_26 = [24375, 21826, 21741, 22172, 21830]

plt.plot(regions, salaires_moins_26)

plt.xlabel('Regions')
plt.ylabel('Salaires < 26')
plt.title('Salaire median par region ')

plt.show()

####################################
####################################
# Trace de courbe
####################################
####################################

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100) #
y = 2*x**2+3*x-4

plt.axis([-10, 20, -10, 10])

plt.grid()

plt.plot(x,y)
plt.show()

####################################
####################################
# Trace de courbe de Cos et Sin
####################################
####################################
# y = cos(x) + 3 sin(2x) [-4, 4]

import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
import numpy as np
from math import *

abscisses = np.linspace(-4, 4, 100)
ordonnees = [cos(x) + 3 * sin(2*x) for x in abscisses]

plt.plot(abscisses, ordonnees)
plt.show()

####################################
####################################
# Trace de courbe de Cos et Sin avec numpy
####################################
####################################

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4,100)
y = np.cos(x)+3*np.sin(2*x)
plt.plot(x,y)
plt.show()


####################################
####################################
# Tracés de courbes dans le même repère
####################################
####################################

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 4, 10)
y = -2 * x + 3
plt.plot(x, y, label="-2x+3", color='r')
y = 3*x**2 + 4*x - 3
plt.plot(x, y, label="3x2+4x-3", color='#d3d3d3', linestyle='--', marker='.')
plt.legend()
plt.show()

####################################
####################################
# Tracés de courbes dans le même repère
####################################
####################################

#####  label dynamique !!!
# y= cos(nx)
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
for n in range(1, 5):
    y = np.cos(n*x)
    plt.plot(x, y, label="n="+str(n))

plt.legend(loc="lower right")
plt.show()


####################################
####################################
# Bar / Bâtons
####################################
####################################

import matplotlib.pyplot as plt
import numpy as np


x = [3, 5, 6, 7]
y = [4, 1, 3, 4]
plt.bar(x,y)

plt.show()

x = ['Jan', 'Fev', 'Mar', 'Avr']
y = [4, 1, 3, 4]


####################################
####################################
# Histogrammes
####################################
####################################

import numpy as np
import matplotlib.pyplot as plt

x = [21, 22, 23, 3, 5, 6, 77, 8, 9, 10, 31, 32, 33, 34, 35, 36, 37, 18, 49, 50, 100]

# x.sort()
#
# print(x)



valeurs_y, valeurs_x, patches = plt.hist(x, bins=4, edgecolor='black')

plt.xticks(valeurs_x)
plt.yticks(valeurs_y)
plt.legend()

plt.show()


######



####################################
####################################
# Histogrammes en horizontal
####################################
####################################
import numpy as np
import matplotlib.pyplot as plt

x = [21, 22, 23, 3, 5, 6, 77, 8, 9, 10, 31, 32, 33, 34, 35, 36, 37, 18, 49, 50, 100]

plt.hist(x,
         bins=5,
         orientation='horizontal',
         edgecolor='black',
         hatch='x')
plt.ylabel('valeurs')
plt.xlabel('frequences')
plt.title("Representation sous forme d'histograme")
plt.legend()

plt.show()



####################################
####################################
# Histogrammes empilés
####################################
####################################


import numpy as np
import matplotlib.pyplot as plt

x1 = [1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]
x2 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]

bins = [ x + 0.5 for x in range(0, 6)]

# print(bins)
plt.hist([x1, x2],
         bins = bins,
         color=['yellow', 'green'],
         edgecolor='black',
         label=['x1', 'x2'],
         hatch='/',
         histtype='barstacked'
)
plt.legend()
plt.show()



####################################
####################################
# distribution gaussienne standard (moyenne 0, écart-type 1).
####################################
####################################


import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)
plt.hist(x, bins=10)
plt.show()



####################################
####################################
# lance 2 des
####################################
####################################

import matplotlib.pyplot as plt
import numpy as np
from random import *

liste =[randint(1,6)+randint(1,6) for _ in range(1000)]
plt.hist(liste,11)

plt.show()


####################################
####################################
# nuage de points
####################################
####################################

import matplotlib.pyplot as plt
import numpy as np

x = [ 1, 3, 2, 1]
y = [ 2, 3, 1, 3]
plt.scatter(x,y)

plt.show()

####################################
####################################
# nuage de points ameliore
####################################
####################################

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 2.4, 4.2, 5.6, 8.2]

plt.scatter(x, y,
            c=['cyan', 'skyblue', 'blue', 'navy', 'black'],
            s=[1110, 90, 70, 50, 30],
            marker='s',
            edgecolors='none')

plt.title('representation de points avec differentes couleurs et tailles')
plt.axis('equal')
plt.plot([0, 4], [0, 9], color='red', linestyle='solid')
plt.show()

####################################
####################################
# Nuage de points avec condition y<x2
####################################
####################################
from random import random

import matplotlib.pyplot as plt

def donner_couleur(x, y):
    couleurs=[]
    for i in range(len(x)):
        if y[i]<x[i]**2 : couleurs.append("r")
        else: couleurs.append('b')
    return couleurs


x = [random() for _ in range(5000)]
y = [random() for _ in range(5000)]

plt.scatter(x, y, s=1, c=donner_couleur(x, y))
plt.show()


#Exemple simple: plt.scatter(x, y, s=1, c=['b', 'r'])

####################################
####################################
# Bonus salaire de developpeurs
####################################
####################################


from matplotlib import pyplot as plt

# plt.style.available
plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')

# plt.xkcd()

# Median Developer Salaries by Age
ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]



plt.plot(ages_x, py_dev_y,label='Python')

plt.plot(ages_x, js_dev_y, label='JavaScript')

plt.plot(ages_x, dev_y, color='#444444', linestyle ='--', marker='.', label='Tous les Devs')

plt.xlabel('Ages')
plt.ylabel('Salaire Median (EUR)')
plt.title('Salaire Median (EUR) par Age')

plt.legend()

plt.grid(True)
#plt.tight_layout()

plt.savefig('demo.png')
plt.show()

