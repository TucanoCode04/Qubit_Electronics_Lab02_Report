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
get_stats("S11",0,0)
get_stats("S21",1,0)

s21_db = net.s_db[:, 0, 1]
idx_peak = np.argmax(s21_db)
f_center = net.f[idx_peak]
val_peak = s21_db[idx_peak]

target = val_peak - 3
idx_l = np.argmin(np.abs(s21_db[:idx_peak] - target))
idx_h = np.argmin(np.abs(s21_db[idx_peak:] - target)) + idx_peak

f_l, f_h = net.f[idx_l], net.f[idx_h]
bw = f_h - f_l
q_factor = f_center / bw

print(f"f low: {f_l/1e6:.2f} MHz")
print(f"f high: {f_h/1e6:.2f} MHz")
print(f"f peak: {f_center/1e6:.2f} MHz")
print(f"bandwidth: {bw/1e6:.2f} MHz")
print(f"quality factor: {q_factor:.2f}")

#calculating the match. bw at -10db
s11_db = net.s_db[:, 0, 0]
under_11 = np.where(s11_db < -10)[0]
if len(under_11)>0:
    f_match_bw = net.f[under_11[-1]] - net.f[under_11[0]]
    print(f"Matching bandwidth S11 at -10dB: {f_match_bw/1e6:.2f} MHz")

s22_db = net.s_db[:, 1, 1]
under_22 = np.where(s22_db < -10)[0]
if len(under_22)>0:
    f_match_bw = net.f[under_22[-1]] - net.f[under_22[0]]
    print(f"Matching bandwidth S22 at -10dB: {f_match_bw/1e6:.2f} MHz")
