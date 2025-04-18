import matplotlib.pyplot as plt
import numpy as np

# load data
energy, dosup, dosdw, idos = np.loadtxt('FeO_dos.dat', unpack=True)
dos = dosup + dosdw
# make plot
plt.figure(figsize = (12, 6))
plt.plot(energy, dos, linewidth=0.75, color='red')
plt.plot(energy, dosup, linewidth=0.75, color='green')
plt.plot(energy, dosdw, linewidth=0.75, color='blue')
plt.yticks([])
plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.axvline(x=13.646, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(-6, 16)
plt.ylim(0, )
plt.text(.5, 1.7, 'Fermi energy', fontsize='medium', rotation=90)
plt.show()
