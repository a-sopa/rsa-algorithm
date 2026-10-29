import matplotlib.pyplot as plt
import numpy as np

labels = ['Encryption', 'Decryption']
python_times = [0.040996, 0.324084]
c_times = [0.006139, 0.051282]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width/2, python_times, width, label='Python 3', color="#F3D216")
rects2 = ax.bar(x + width/2, c_times, width, label='C (-O3)', color="#598FCC")

ax.set_ylabel('Total Time in Seconds (10,000 iterations)')
ax.set_title('RSA Performance Benchmark: C vs. Python')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, fmt='%.3fs', padding=3)
ax.bar_label(rects2, fmt='%.3fs', padding=3)

plt.tight_layout()
plt.savefig('benchmark_chart.png', dpi=300)
print("Generated benchmark_chart.png successfully.")