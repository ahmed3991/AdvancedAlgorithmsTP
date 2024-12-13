#TODO: put the code here

import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path
from collections import namedtuple

sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    DataGeneratorFactory,
    StringGenerator,
    TimeAndSpaceProfiler,
    ComplexityAnalyzer,
    ComplexityVisualizer,
    ComplexityDashboardVisualizer
)


## Data Generation

factory = DataGeneratorFactory()
factory.register_generator("string",StringGenerator(['A','B','C','D','E']))

lengths = [10, 100, 1000]
nbr_experiments=3

random_pairs = [
    factory.get_generator("string").generate_pair(size,size) for _ in range(nbr_experiments) for size in lengths
]

different_pairs = [
    factory.get_generator("string").generate_diff_pair(size,size) for _ in range(nbr_experiments) for size in lengths
]

identical_pairs = [
    factory.get_generator("string").generate_ident_pair(size) for _ in range(nbr_experiments) for size in lengths
]

print(random_pairs[0])

## Functions

def longest_string(x,y):
    return x if len(x) > len (y) else y

def lcs_rec_memo(x,y,i,j,memo):

    if(i,j) in memo:
        return memo[(i,j)]

    if i == 0 or j == 0 :
        return ""
    
    if x[i-1] == y [j-1]:
        memo[(i,j)] = lcs_rec_memo(x,y,i-1,j-1,memo) + x[i-1]
        return memo[(i,j)]
    
    lcs1=lcs_rec_memo(x,y,i-1,j,memo)
    lcs2=lcs_rec_memo(x,y,i,j-1,memo)

    memo[(i,j)] = longest_string(lcs1,lcs2)
    return memo[(i,j)]

def lcs_rec(x,y,i,j):

    if i == 0 or j == 0 :
        return ""

    if x[i-1]==y[j-1] :
        return lcs_rec(x,y,i-1,j-1) + x[i-1]
    
    lcs1 = lcs_rec(x,y,i-1,j)
    lcs2 = lcs_rec(x,y,i,j-1)

    return longest_string(lcs1,lcs2)

def lcs_dp(x,y):

    n=len(x)
    m=len(y)

    dp = [["" for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + x[i-1]
            else:
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j])>len(dp[i][j-1]) else dp[i][j-1]

    return dp[n][m]


## Benchmarking