import numpy as np
import matplotlib.pyplot as plt

delta_e = lambda x, eps: (1/np.pi)*eps/(eps*eps+x*x)

[plt.plot(delta_e(np.linspace(-1,1,500), 0.01*10**i)) for i in range(3)]
plt.show()


