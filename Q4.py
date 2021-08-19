import numpy as np         # Usado para criar o vetor t.

import matplotlib.pyplot as plt      # Usado para plotar os gráficos.

from matplotlib.ticker import AutoMinorLocator  # Usado para criar as marcas nos gráficos.

# Aqui começa o código.

t_inicial = 0.0        # Esse é o tempo inicial.

t_final = 30.0       # Tempo final.

n = 10

delta_t = 0.5 # Esse é o passo de tempo.

n = int((t_final - t_inicial)/delta_t)
t = np.linspace(t_inicial,t_final,n+1)  

y = np.zeros(n+1, float)

u = np.zeros(n+1, float)

for i in range(0,n-1):         # i vai de 0 a n-1.
    y[i+2] = 1.5*y[i+1] - (0.75)*y[i] + 0.25

fig = plt.figure()

for i in range(n+1):
    u[i] = 1

# Configurando o gráfico.

# Dando nome aos eixos.
ax = fig.add_subplot(111)
ax.set_xlabel('time', fontsize = 24)
ax.set_ylabel('y[Kt]', fontsize = 24)

# Colocando as marcas. 
plt.xticks(size = 22)
plt.yticks(size = 22)
minor_locator = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minor_locator)
minor_locator = AutoMinorLocator(5)
ax.yaxis.set_minor_locator(minor_locator)
plt.tick_params(which='both', width=0.8)
plt.tick_params(which='major', length=5)
plt.tick_params(which='minor', length=2.5)


# Limites dos eixos na hora de plotar. 
plt.axis((t_inicial - 0.1, t_final + 0.1, 0.0, 1.5))


plt.plot(t, y, '-go',lw = 3, label = 'Discretizado')
plt.plot(t, u, lw = 3, color = 'blue', label = 'Entrada')
plt.title(u'Resposta ao Degrau', fontsize = 24)

# Legenda.
ax.legend()
legend = ax.legend(loc=1, fontsize='large')

#Comando para mostrar o grafico
plt.show()
