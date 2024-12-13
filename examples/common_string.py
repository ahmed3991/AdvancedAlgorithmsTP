#TODO: put the code here

import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path
from collections import namedtuple

sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    DataGeneratorFactory,
    RandomDataGenerator,
    LinearDataGenerator,
    TimeAndSpaceProfiler,
    ComplexityAnalyzer,
    ComplexityVisualizer,
    ComplexityDashboardVisualizer
)


## Data Generation

## Functions

def longest_string(x,y):
    return x if len(x) > len (y) else y

def lcs_rec(x,y,i,j):
    if i == 0 or j == 0 :
        return ""
    
    if x[i-1] == y [j-1]:
        return lcs_rec(x,y,i-1,j-1) + x[i-1]
    
    lcs1=lcs_rec(x,y,i-1,j)
    lcs2=lcs_rec(x,y,i,j-1)

    return longest_string(lcs1,lcs2)

x="AGGTAB"
y="GXTXAYB"
print(lcs_rec(x,y,len(x),len(y)))

## Benchmarking