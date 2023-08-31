import numpy as np
import random

#rand_int = random.randint(a, b)

r1 = [random.randint(1, 100)for i in range(10)]
r2 = [random.randint(1, 100)for i in range(10)]
data = [r1, r2]

# Finn gjennomsnittsvektoren
mean_vector = np.mean(data, axis=0)

# Beregn kovariansmatrisen
cov_matrix = np.cov(data, rowvar=False, bias=True)
print(cov_matrix)