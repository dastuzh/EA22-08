import os
import os.path
import gzip

import numpy as np







if __name__ == '__main__':
    a = np.array([0,0,0,1,2])
    index = np.where(a==2)
    print(index)