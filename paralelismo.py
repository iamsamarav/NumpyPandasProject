import pandas as pd
import numpy as np
from multiprocessing import Pool

base = pd.read_csv("C:/Users/samar/Downloads/archive (5)/Student_performance_data _.csv",
                   encoding="ISO-8859-1")
print(base.head(10))


def media(basee):
    total_media = basee['Age'].mean()
    basee['Media'] = total_media
    return basee


def paralelismo(basee, func, n_cores=8):
    base_split = np.array_split(basee, n_cores)
    pool = Pool(n_cores)
    basee = pd.concat(pool.map(func, base_split))
    print(basee)
    pool.close()
    pool.join()
    return basee


if __name__ == '__main__':
    base = pd.read_csv("C:/Users/samar/Downloads/archive (5)/Student_performance_data _.csv",
                       encoding="ISO-8859-1")
    print(base.head(10))

    base = paralelismo(base, media)
    print(base)