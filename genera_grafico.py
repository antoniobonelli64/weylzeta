import numpy as np
import matplotlib.pyplot as plt
import math

def get_kaleidoscopic_fluctuations(n, k_filter):
    manifold_fluctuation = 0.0
    for k in range(1, k_filter + 1):
        manifold_fluctuation += ((-1)**(k_filter - k)) * k * math.comb(k_filter, k)
    return manifold_fluctuation

def generate_density_simulation(k_val=12):
    manifold_n = np.arange(10, 200, 2)
    t_imaginary = []
    spectral_density = []
    for n in manifold_n:
        P_k = get_kaleidoscopic_fluctuations(n, k_val)
        if P_k > 0:
            lambda_val = np.abs(P_k) / n
            t_val = np.sqrt(np.abs(lambda_val - 0.25))
            t_imaginary.append(t_val)
            spectral_density.append(lambda_val**2)
    spectral_density = np.array(spectral_density)
    return np.array(t_imaginary), 1.0 - (spectral_density / np.max(spectral_density))

# Generazione e Plot
fig, ax = plt.subplots(figsize=(8, 5))
t_raw, density_raw = generate_density_simulation(k_val=12)

x_positions = 0.5 - (t_raw / np.max(t_raw)) * 0.1
y_positions = density_raw

ax.scatter(x_positions, y_positions, color='grey', alpha=0.5, s=10, label='Dati Grezzi k=12 (Scattering)')
ax.axvline(x=0.5, color='black', linestyle='-', linewidth=2.0, label='Limite k \u2192 \u221E (Linea Critica)')

ax.set_title('Densità Spettrale dei Polinomi Caleidoscopici', fontsize=14)
ax.set_xlabel('$\sigma$ (Linea Critica $\sigma=1/2$)', fontsize=12)
ax.set_ylabel('Densità Geometrica Normalizzata', fontsize=12)
ax.set_xlim(0.0, 1.0)
ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
ax.set_xticklabels(['0', '', '1/2', '', '1'])
ax.legend(loc='upper right')

# Salva l'immagine in alta risoluzione per LaTeX
plt.savefig('Densita_Caleidoscopica.png', dpi=300, bbox_inches='tight')
print("Immagine 'Densita_Caleidoscopica.png' salvata con successo!")
