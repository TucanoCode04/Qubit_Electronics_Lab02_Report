import matplotlib.pyplot as plt
import skrf as rf

net = rf.Network('./antennap1.s1p')
net.frequency.unit = 'MHz'

fig, axes = plt.subplots(1, 1, figsize=(12, 10))
net.plot_s_db(m=0, n=0, ax=axes,color = 'red')
axes.set_title('S11', fontsize=22)
axes.grid(True, which='both', alpha=0.5)
axes.set_xlabel('Frequency (MHz)', fontsize=18)
axes.set_ylabel('Magnitude (dB)', fontsize=18)
axes.tick_params(axis='both', which='major', labelsize=14)  
axes.get_legend().remove()
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show() 