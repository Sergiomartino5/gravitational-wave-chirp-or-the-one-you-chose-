import numpy as np
import matplotlib.pyplot as plt

# time to merger (seconds, arbitrary scale)
t = np.linspace(-10, -0.1, 500)

# chirp model (scaled)
f = (-t) ** (-3/8)

plt.figure()
plt.plot(t, f)
plt.xlabel("Time to merger (s)")
plt.ylabel("Frequency (arb. units)")
plt.title("Gravitational Wave Chirp from Binary Black Hole Inspiral")
plt.grid()
plt.show()
