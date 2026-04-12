import skrf as rf
import matplotlib.pyplot as plt
import numpy as np


nome_file = 'circular_resonator.s2p'
dut = rf.Network(nome_file)

# Conversion Hz → GHz
freq = dut.frequency.f / 1e9

#Plot for reflections
plt.figure(figsize=(10, 5))

plt.plot(freq, dut.s_db[:, 0, 0], label='S11')
plt.plot(freq, dut.s_db[:, 1, 1], label='S22')

plt.title('Reflections (S11, S22)')
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (GHz)')
plt.grid(True)
plt.legend()

#Plot for trasmission
plt.figure(figsize=(10, 5))

plt.plot(freq, dut.s_db[:, 1, 0], label='S21')
plt.plot(freq, dut.s_db[:, 0, 1], label='S12')

plt.title('Transmission (S21, S12)')
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (GHz)')
plt.grid(True)
plt.legend()



S21 = dut.s_db[:, 1, 0]

max_indices = []
for i in range(1, len(S21)-1):
    if S21[i] > S21[i-1] and S21[i] > S21[i+1]:
        max_indices.append(i)

max_indices = sorted(max_indices, key=lambda i: S21[i], reverse=True)[:2]

print("\n---  Resonance peaks (S21) ---")

for idx in max_indices:
    f0 = freq[idx]
    peak = S21[idx]

    print(f"\nPicco a f = {f0:.3f} GHz")
    print(f"Magnitudine = {peak:.2f} dB")

    
    target = peak - 3

    i_left = idx
    while i_left > 0 and S21[i_left] > target:
        i_left -= 1

    i_right = idx
    while i_right < len(S21)-1 and S21[i_right] > target:
        i_right += 1

    f_left = freq[i_left]
    f_right = freq[i_right]

    BW = f_right - f_left

    print(f"f_low = {f_left:.3f} GHz")
    print(f"f_high = {f_right:.3f} GHz")
    print(f"Bandwidth (-3 dB) = {BW:.4f} GHz")


plt.show()
