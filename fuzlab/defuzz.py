# defuzz.py
# by Eduardo Avelar
# August 2022
# Modified by Efendi Nasiboglu, July 2024

import numpy as np

def defuzz(fis, x, y, defuzz_method):
    
    if defuzz_method == 'centroid':
        total_area = sum(y)
        if total_area==0:
            return np.mean(x)
        return sum(y * x) / total_area
    elif defuzz_method == 'wabl':
        c = fis.WablOptimizm
        level_sets = fis.WablDegrees
        p = fis.WablImportances
        levels = np.linspace(0, 1.0, level_sets)
        
        left = np.zeros(level_sets)
        right = np.zeros(level_sets)
        sum1 = 0
        sum2 = 0
        for i in range(level_sets):
            if len(x[y>=levels[i]])>0:    
                left[i]=min(x[y>=levels[i]])
                right[i]=max(x[y>=levels[i]])
                sum1 += p[i]
                sum2 += (c*right[i] + (1-c)*left[i])*p[i]
        return sum2/sum1;
    elif defuzz_method == 'bisector':
        total_area = sum(y)
        data_n = len(x)
        tmp = y[0]
        for k in range(1, data_n):
            tmp = tmp + y[k]
            if tmp >= total_area/2:
                break
        return x[k]
    elif defuzz_method == 'mom':
        return np.mean(x[y == max(y)])
    elif defuzz_method == 'som':
        tmp = x[y == max(y)]
        which = np.argmin(abs(tmp))
        return tmp[which]
    elif defuzz_method == 'lom':
        tmp = x[y == max(y)]
        which = np.argmax(abs(tmp))
        return tmp[which]
    elif defuzz_method == 'wtaver':
        return sum(x * y) / sum (y)
    else:
        raise ValueError('The input for `type`, %s, was incorrect.' % (type))
    