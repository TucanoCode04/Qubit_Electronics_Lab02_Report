import skrf as rf
import numpy as np

net = rf.Network('./passband.s2p')['1.5-3ghz']

def get_stats(nome,m,n):
    mag = net.s_db[:,m,n]
    idx_max = np.argmax(mag)
    idx_min = np.argmin(mag)

    print(f'{nome} Max: {mag[idx_max]:.2f}db at {net.f[idx_max]/1e6:.2f}MHz')
    print(f'{nome} Min: {mag[idx_min]:-2f}db at {net.f[idx_min]/1e6:.2f}Mhz')

get_stats("S22",1,1)
get_stats("S12",0,1)

s21_db = net.s_db[:, 1, 1]
idx_peak = np.argmin(s21_db)
f_center = net.f[idx_peak]
val_peak = s21_db[idx_peak]

target = val_peak + 3
idx_l = np.argmin(np.abs(s21_db[:idx_peak] - target))
idx_h = np.argmin(np.abs(s21_db[idx_peak:] - target)) + idx_peak

f_l, f_h = net.f[idx_l], net.f[idx_h]
bw = f_h - f_l
q_factor = f_center / bw

print(f"f peak: {f_center/1e6:.2f} MHz")
print(f"bandwidth: {bw/1e6:.2f} MHz")
print(f"quality factor: {q_factor:.2f}")