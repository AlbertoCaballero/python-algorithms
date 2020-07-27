import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as graph
import statsmodels.formula.api as smf
from scipy import stats

dataset = pd.read_csv('datos.csv', index_col=False, sep=" ",header=0)

#print(dataset.head())
#dataset.head()

# Asign data to X and Y
dataframe = pd.DataFrame(
            {'X': dataset.gastos,
                     'y': dataset.ventas}
            )
print(dataset)

print(dataframe)

# Calculate the mean of X and y
xmean = np.mean(dataset.gastos)
ymean = np.mean(dataset.ventas)
print("vi prom = " + str(xmean))
print("vo prom = " + str(ymean))

# Calculate the terms needed for the numator and denominator of beta
dataframe['xycov'] = (dataframe['X'] - xmean) * (dataframe['y'] - ymean)
dataframe['xvar'] = (dataframe['X'] - xmean)**2

# Calculate beta and alpha
beta = dataframe['xycov'].sum() / dataframe['xvar'].sum()
alpha = ymean - (beta * xmean)
print('A = ' + str(alpha))
print('B = ' + str(beta))

# Show calculated model
print('Y = A + BX : ')
print('Y = ' + str(alpha) + ' + ' + str(beta) + 'X')

ypred = alpha + beta * dataframe['X']
print(ypred)


# Plot regression agains data
graph.figure(figsize=(12, 6))
graph.plot(dataframe['X'], ypred) #regression line
graph.plot(dataframe['X'], dataframe['y'], 'ro') #actual data
graph.title('Datos y linea de mejor ajuste')
graph.xlabel('Gastos')
graph.ylabel('Ventas')

graph.show()
