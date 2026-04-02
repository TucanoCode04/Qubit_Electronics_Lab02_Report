import skrf as rf
import matplotlib.pyplot as plt
import os

# --- Save directory ---
save_dir = os.path.dirname(os.path.abspath(__file__))

# Load configurations
config_1 = rf.Network('./Measurements files/circulator_p11_p22.s2p')
config_2 = rf.Network('./Measurements files/circulartor_p11_p23.s2p')

# =========================
# CONFIG 1 - REFLECTION
# =========================
plt.figure(figsize=(6,5))

plt.plot(config_1.f/1e6, config_1.s_db[:,0,0], label='S11')
plt.plot(config_1.f/1e6, config_1.s_db[:,1,1], label='S22')

plt.title('Config 1 - Reflections (S11, S22)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Magnitude (dB)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'config1_reflection.png'), dpi=300)
plt.close()

# =========================
# CONFIG 1 - TRANSMISSION
# =========================
plt.figure(figsize=(6,5))

plt.plot(config_1.f/1e6, config_1.s_db[:,1,0], label='S21')
plt.plot(config_1.f/1e6, config_1.s_db[:,0,1], label='S12')

plt.title('Config 1 - Transmission (S21, S12)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Magnitude (dB)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'config1_transmission.png'), dpi=300)
plt.close()

# =========================
# CONFIG 2 - REFLECTION
# =========================
plt.figure(figsize=(6,5))

plt.plot(config_2.f/1e6, config_2.s_db[:,0,0], label='S11')
plt.plot(config_2.f/1e6, config_2.s_db[:,1,1], label='S22')

plt.title('Config 2 - Reflections (S11, S22)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Magnitude (dB)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'config2_reflection.png'), dpi=300)
plt.close()

# =========================
# CONFIG 2 - TRANSMISSION
# =========================
plt.figure(figsize=(6,5))

plt.plot(config_2.f/1e6, config_2.s_db[:,1,0], label='S21')
plt.plot(config_2.f/1e6, config_2.s_db[:,0,1], label='S12')

plt.title('Config 2 - Transmission (S21, S12)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Magnitude (dB)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'config2_transmission.png'), dpi=300)
plt.close()

print("Plots saved in:", save_dir)