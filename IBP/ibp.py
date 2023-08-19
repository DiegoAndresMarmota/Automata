import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ibp = np.array([
    ['', 'Pantoprazol', 'Omeprazol', 'Lansoprazol', 'Rabeprazol'], 
    #['Vida Media de Activación']
    ['pH 1.2', 4, 2, 2, 13], 
    ['pH 5.0', 128, 60, 70, ''], 
    ['pH 5.1', 309, 101, 90, 9], 
    ['pH 6.0', 1260, 451, 382, ''], 
    ['pH 7.0', 4383, 2342, 2100, ''],
    #['Vida Media de Eliminación']
    ['', 82, 80, 165, 76],
    #['Tomado de Kromer W, Kruger U, Huber R, Hartmann M, Steinijans VW - Differences in pH-Dependent activation Rates of Substituted Benzimidazoles and Biolocal in vitro Correlatos. Pharmacology 1998; 56: 57-70']
    ])


#Actividad enzimatica tipo
ibp_matplot_a = [1.2, 5, 5.1, 6.0, 7.0]
ibp_matplot_b = [0.7, 1.2, 1.7, 2.1, 4.3]
ibp_matplot_c = [0.9, 1.5, 1.7, 2.0, 3.6]
ibp_matplot_d = [0.5, 1.1, 2.0, 2.2, 1.5]

print(pd.DataFrame(data=ibp))


#Caracteristicas del gráfico de lineas
plt.plot(ibp_matplot_a, ibp_matplot_d, color='red', linewidth=3, label='Variación de IBP en el pH - Pantoprazol')
plt.plot(ibp_matplot_b, ibp_matplot_d, color='green', linewidth=3, label='Variación de IBP en el pH - Omeprazol')
plt.plot(ibp_matplot_c, ibp_matplot_d, color='blue', linewidth=3, label='Variación de IBP en el pH - Lansoprazol')


#Caracteristicas del gráfico de barras
plt.bar(ibp_matplot_a, ibp_matplot_d, color='red', label='Variación de IBP en el pH - Pantoprazol')
plt.bar(ibp_matplot_b, ibp_matplot_d, color='green', label='Variación de IBP en el pH - Omeprazol')
plt.bar(ibp_matplot_c, ibp_matplot_d, color='blue', label='Variación de IBP en el pH - Lansoprazol')


#Caracteristicas del gráfico de dispersión
plt.scatter(ibp_matplot_a, ibp_matplot_d, color='red', label='Variación de IBP en el pH - Pantoprazol')
plt.scatter(ibp_matplot_b, ibp_matplot_d, color='green', label='Variación de IBP en el pH - Omeprazol')
plt.scatter(ibp_matplot_c, ibp_matplot_d, color='blue', label='Variación de IBP en el pH - Lansoprazol')

#Encabezado
plt.title('Variación de IBP en el pH')
plt.ylabel('Variación de IBP')
plt.xlabel('pH')


#Figura
plt.legend()
plt.grid(True)
plt.show()


#print('Mediana de IBP:', ibp.median(axis=1, skipna=True, numeric_only=True))
#print('Desviación estandar de IBP:', ibp.std())
#print('Percentil 0.25% IBP:', ibp.quantile(0.25))