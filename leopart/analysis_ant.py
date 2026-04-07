import skrf as rf
import numpy as np

net = rf.Network('./antennap1.s1p')['5-6.5ghz']

mag = net.s_db[:,0,0]
idx_min = np.argmin(mag)
f_min = net.f[idx_min]
print(f'frequency of the dip: {f_min/1e6:.2f} Mhz \nreturn loss : {mag[idx_min]:2f} dB')


under_11 = np.where(mag < -10)[0]
if len(under_11)>0:
    f_match_bw = net.f[under_11[-1]] - net.f[under_11[0]]
    print(f"Matching bandwidth S11 at -10dB: {f_match_bw/1e6:.2f} MHz")