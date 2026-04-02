import skrf as rf
import matplotlib.pyplot as plt
import os

# --- Save directory = same folder as this script ---
save_dir = os.path.dirname(os.path.abspath(__file__))

# Load the S-parameter files
disp_a = rf.Network('./Measurements files/disp_a.s1p')
disp_b = rf.Network('./Measurements files/disp_b.s1p')
disp_c = rf.Network('./Measurements files/disp_c.s1p')

# =========================
# DISP A
# =========================
plt.figure(figsize=(6,5))
plt.plot(disp_a.f/1e6, disp_a.s_db[:,0,0])
plt.title('DISP A - S11 (dB)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('S11 (dB)')
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'disp_a.png'), dpi=300)
plt.close()

# =========================
# DISP B
# =========================
plt.figure(figsize=(6,5))
plt.plot(disp_b.f/1e6, disp_b.s_db[:,0,0])
plt.title('DISP B - S11 (dB)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('S11 (dB)')
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'disp_b.png'), dpi=300)
plt.close()

# =========================
# DISP C
# =========================
plt.figure(figsize=(6,5))
plt.plot(disp_c.f/1e6, disp_c.s_db[:,0,0])
plt.title('DISP C - S11 (dB)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('S11 (dB)')
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'disp_c.png'), dpi=300)
plt.close()

# =========================
# COMBINED
# =========================
plt.figure(figsize=(6,5))
plt.plot(disp_a.f/1e6, disp_a.s_db[:,0,0], label='DISP A')
plt.plot(disp_b.f/1e6, disp_b.s_db[:,0,0], label='DISP B')
plt.plot(disp_c.f/1e6, disp_c.s_db[:,0,0], label='DISP C')

plt.title('Comparison of S11 (dB)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('S11 (dB)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'combined.png'), dpi=300)
plt.close()

print("Plots saved in:", save_dir)