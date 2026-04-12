import skrf as rf
import matplotlib.pyplot as plt
import numpy as np

nome_file = 'band_reject.s2p'
dut = rf.Network(nome_file)

# Conversion Hz → GHz
freq = dut.frequency.f / 1e9


mask = (freq > 1.5) & (freq < 3.0)
threshold = -3.0


s21_db = dut.s_db[:, 1, 0]
idx_min_21 = np.argmin(s21_db)
f_min_21 = freq[idx_min_21]
mag_min_21 = s21_db[idx_min_21]
indices_21 = np.where((s21_db < threshold) & mask)[0]
bw_21 = freq[indices_21[-1]] - freq[indices_21[0]] if len(indices_21) > 0 else 0


s12_db = dut.s_db[:, 0, 1]
idx_min_12 = np.argmin(s12_db)
f_min_12 = freq[idx_min_12]
mag_min_12 = s12_db[idx_min_12]
indices_12 = np.where((s12_db < threshold) & mask)[0]
bw_12 = freq[indices_12[-1]] - freq[indices_12[0]] if len(indices_12) > 0 else 0

#Plot of trasmission
plt.figure(figsize=(10, 6))
plt.plot(freq, s21_db, label='S21', linewidth=2)
plt.plot(freq, s12_db, label='S12', linestyle='--')

plt.title('Transmission (S21, S12)')
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (GHz)')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()
plt.show()

#Plot of reflections
plt.figure(figsize=(10, 5))
plt.plot(freq, dut.s_db[:, 0, 0], label='S11')
plt.plot(freq, dut.s_db[:, 1, 1], label='S22')

plt.title('Reflections (S11, S22)')
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (GHz)')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()

plt.show()

#Risultati
print("\n" + "="*40)
print(f"{'PARAMETRO':<18} | {'S21':<10} | {'S12':<10}")
print("-" * 40)
print(f"{'F_min (GHz)':<18} | {f_min_21:<10.4f} | {f_min_12:<10.4f}")
print(f"{'Mag_min (dB)':<18} | {mag_min_21:<10.2f} | {mag_min_12:<10.2f}")
print(f"{'Bandwidth (GHz)':<18} | {bw_21:<10.4f} | {bw_12:<10.4f}")
print("="*40 + "\n")