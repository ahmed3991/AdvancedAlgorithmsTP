import random
import sys
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Any


sys.path.append(str(Path(__file__).parent.parent))

# --- GENERATOR ---
class DataGenerator(ABC):
    @abstractmethod
    def generate(self, size: int) -> Any:
        """Generate synthetic data of the given size."""
        pass
class StringGenerator(DataGenerator):

    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choices(self.alphabet, k=size))

    def generate_pair(self, length_m: int, length_n: int, similarity: float = 0.5) -> tuple[str, str]:
        common_length = int(min(length_m, length_n) * similarity)
        common_part = ''.join(random.choices(self.alphabet, k=common_length))

        remaining_m = ''.join(random.choices(self.alphabet, k=length_m - common_length))
        remaining_n = ''.join(random.choices(self.alphabet, k=length_n - common_length))

        string1 = common_part + remaining_m
        string2 = common_part + remaining_n

        return string1, string2
    
# --- END GENERATOR ---

# --- LCS Recursive without memoization ---
def lcs_recursive(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return ""
    if string1[-1] == string2[-1]:
        return lcs_recursive(string1[:-1], string2[:-1]) + string1[-1]
    else:
        lcs1 = lcs_recursive(string1[:-1], string2)
        lcs2 = lcs_recursive(string1, string2[:-1])
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2

# --- END LCS Recursive --- 

# --- LCS Buttom Up --- 
def lcs_buttom_up(S1, S2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs_buttom_up = [""] * (index+1)
    lcs_buttom_up[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs_buttom_up[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    # Printing the sub sequences
    # print("S1 : " + S1 + "\nS2 : " + S2)
    # print("LCS: " + "".join(lcs_algo))

    return "".join(lcs_buttom_up)
# --- END LCS Buttom Up --- 

# --- Main --- 
if __name__ == "__main__":
        str1, str2 = StringGenerator().generate_pair(10, 10)  

        print("String 1: ", str1)
        print("String 2: ", str2)

        print("The LCS using Recursive algorithm is ", lcs_recursive(str1, str2)) 
        print("The LCS using Buttom Up algorithm is ", lcs_buttom_up(str1, str2, len(str1), len(str2)))           
        

