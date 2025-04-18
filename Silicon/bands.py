import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(8, 6)

# load data
data = np.loadtxt('si_bands.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, alpha=0.5, color='k')
plt.xlim(min(k), max(k))

# Fermi energy
fermi = 6.616
plt.axhline(fermi, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)
plt.axvline(0.0000, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1.0000, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1.3536, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1.9659, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(3.0266, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(3.8926, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(4.5997, linewidth=0.75, color='k', alpha=0.5)
# text labels
plt.xticks(ticks= [0.0000, 1.0000, 1.3536, 1.9659, 3.0266, 3.8926, 4.5997], \
           labels=[r'$\Gamma$', 'X', 'U', 'K', r'$\Gamma$', 'L', 'X'])
plt.ylabel("Energy (eV)")
plt.text(2.3, 5.6, 'Fermi energy', fontsize= 'small')
plt.show()