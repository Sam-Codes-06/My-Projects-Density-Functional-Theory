import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('graphene_bands.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, alpha=0.5, color='k')
plt.xlim(min(k), max(k))

# Fermi energy
plt.axhline(0.900, linestyle=(0, (8, 10)), linewidth=0.75, color='k', alpha=0.5)
# High symmetry k-points (check bands_pp.out)
plt.axvline(0.0000, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(0.5774, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(0.9107, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1.5774, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1.7440, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(2.3214, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(2.6547, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(3.3214, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(3.8987, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(4.0654, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(4.4381, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(4.6047, linewidth=0.75, color='k', alpha=0.5)
# text labels
plt.xticks(ticks= [0, 0.5774, 0.9107, 1.5774, 1.7440, 2.3214, 2.6547, 3.3214, 3.8987, 4.0654, 4.4381, 4.6047],
           labels=[r'$\Gamma$', 'M', 'K', r'$\Gamma$', 'A', 'L', 'H', 'A', 'L', 'M', 'H', 'K'])
plt.ylabel("Energy (eV)")
plt.show()