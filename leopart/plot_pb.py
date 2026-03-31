import matplotlib.pyplot as plt
import skrf as rf


net = rf.Network('./passband.s2p')['1.5-3ghz']
net.frequency.unit = 'MHz'

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

net.plot_s_db(m=0, n=0, ax=axes[0,0], title='S11' ,color = 'red')
net.plot_s_db(m=1, n=0, ax=axes[0,1], title='S21' ,color = 'red')
net.plot_s_db(m=0, n=1, ax=axes[1,0], title='S12' ,color = 'red')
net.plot_s_db(m=1, n=1, ax=axes[1,1], title='S22' ,color = 'red')

for ax in axes.flat:
    ax.grid(True, which='both', alpha=0.5)
    ax.set_xlabel('Frequency (MHz)')
    ax.get_legend().remove()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()  