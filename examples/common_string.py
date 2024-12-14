#TODO: put the code here

print('Please use the complexity library')


from generator import StringGenerator  # Importation du générateur de chaînes
import random
import time

# Implémentation récursive sans mémorisation
def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0, ""
    elif X[m - 1] == Y[n - 1]:
        length, subsequence = lcs_recursive(X, Y, m - 1, n - 1)
        return length + 1, subsequence + X[m - 1]
    else:
        length1, subsequence1 = lcs_recursive(X, Y, m - 1, n)
        length2, subsequence2 = lcs_recursive(X, Y, m, n - 1)
        if length1 > length2:
            return length1, subsequence1
        else:
            return length2, subsequence2

# Implémentation récursive avec mémorisation (cache)
def lcs_recursive_memo(X, Y, m, n, memo):
    if m == 0 or n == 0:
        return 0, ""
    if memo[m][n] != -1:
        return memo[m][n], ""
    
    if X[m - 1] == Y[n - 1]:
        length, subsequence = lcs_recursive_memo(X, Y, m - 1, n - 1, memo)
        memo[m][n] = length + 1
        return memo[m][n], subsequence + X[m - 1]
    else:
        length1, subsequence1 = lcs_recursive_memo(X, Y, m - 1, n, memo)
        length2, subsequence2 = lcs_recursive_memo(X, Y, m, n - 1, memo)
        if length1 > length2:
            memo[m][n] = length1
            return length1, subsequence1
        else:
            memo[m][n] = length2
            return length2, subsequence2

# Implémentation dynamique (Bottom-Up)
def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return dp[m][n], ''.join(reversed(lcs))

# Fonction de comparaison des approches
def compare_approaches(X, Y):
    m, n = len(X), len(Y)
    
    # Test récursif sans mémorisation
    start = time.time()
    result_recursive, lcs_recursive_str = lcs_recursive(X, Y, m, n)
    time_recursive = time.time() - start
    
    # Test récursif avec mémorisation
    memo = [[-1] * (n + 1) for _ in range(m + 1)]
    start = time.time()
    result_memo, lcs_memo_str = lcs_recursive_memo(X, Y, m, n, memo)
    time_memo = time.time() - start
    
    # Test dynamique (Bottom-Up)
    start = time.time()
    result_dp, lcs_dp_str = lcs_dp(X, Y)
    time_dp = time.time() - start
    
    # Affichage des résultats
    print(f"LCS (recursive): Length = {result_recursive}, Subsequence = '{lcs_recursive_str}' (Time: {time_recursive:.6f}s)")
    print(f"LCS (recursive with memoization): Length = {result_memo}, Subsequence = '{lcs_memo_str}' (Time: {time_memo:.6f}s)")
    print(f"LCS (dynamic programming): Length = {result_dp}, Subsequence = '{lcs_dp_str}' (Time: {time_dp:.6f}s)")
    
    # Estimation de la consommation mémoire
    memory_recursive = m * n * 2  # Estimation simple
    memory_memo = m * n * 2
    memory_dp = m * n * 4
    
    print(f"Memory usage (recursive): {memory_recursive} bytes")
    print(f"Memory usage (memoization): {memory_memo} bytes")
    print(f"Memory usage (dp): {memory_dp} bytes")

if __name__ == "__main__":
    # Exemple avec deux chaînes simples
    X = "ABCBDAB"
    Y = "BDCAB"
    
    print("Simple case (ABCBDAB, BDCAB):")
    compare_approaches(X, Y)
    
    # Cas extrême avec de grandes chaînes
    X_large = "A" * 1000
    Y_large = "A" * 1000
    print("\nExtreme case (1000 'A's):")
    compare_approaches(X_large, Y_large)
    
    # Génération de chaînes aléatoires avec StringGenerator
    generator = StringGenerator(['A', 'B', 'C'])
    X_random = generator.generate(100)
    Y_random = generator.generate(100)
    print("\nRandom case (100 characters):")
    compare_approaches(X_random, Y_random)
