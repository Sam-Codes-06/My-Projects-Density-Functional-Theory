import matplotlib.pyplot as plt
import numpy as np

# load data
energy, dos, idos = np.loadtxt('al_dos.dat', unpack=True)

# make plot
plt.figure(figsize = (12, 6))
plt.plot(energy, dos, linewidth=0.75, color='red')
plt.yticks([])
plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.axvline(x=7.939, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(-6, 16)
plt.ylim(0, )
plt.fill_between(energy, 0, dos, where=(energy < 7.939), facecolor='red', alpha=0.25)
plt.text(6, 1.7, 'Fermi energy', fontsize='medium', rotation=90)
plt.show()