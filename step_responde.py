import numpy as np         # Usado para criar o vetor t.

import matplotlib.pyplot as plt      # Usado para plotar os gráficos.

from matplotlib.ticker import AutoMinorLocator  # Usado para criar as marcas nos gráficos.

import control as clt


t_inicial = 0.0 
t_final = 30.0 
quais_T=np.linspace(-1, t_final,1000)
G_s = clt.tf([1.],[1.,1.,1.])

T_mf,yout_mf = clt.step_response(G_s,quais_T[quais_T>0]) 

fig = plt.figure()

# Configurando o gráfico.

# Dando nome aos eixos.
ax = fig.add_subplot(111)
ax.set_xlabel('time', fontsize = 24)
ax.set_ylabel('y', fontsize = 24)

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
plt.plot(T_mf,yout_mf,'k-', label = 'Continuo')
plt.title(u'Resposta ao Degrau', fontsize = 24)

# Legenda.
ax.legend()
legend = ax.legend(loc=1, fontsize='large')

#Comando para mostrar o grafico
plt.show()
