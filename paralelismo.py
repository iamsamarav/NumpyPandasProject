import pandas as pd
import numpy as np
from multiprocessing import Pool

base = pd.read_csv("C:/Users/samar/Downloads/archive (5)/Student_performance_data _.csv",
                   encoding="ISO-8859-1")
print(base.head(10))

def media(base):
    total_media = base['Age'].mean()
    base['Media'] = total_media
    return base

def paralelismo(base, func, n_cores = 8):
    base_split = np.array_split(base, n_cores)
    pool = Pool(n_cores)
    base = pd.concat(pool.map(func, base_split))
    pool.close()
    pool.join()
    return base