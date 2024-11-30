## TODO: TP should be HERE


## TODO: Data Generation

# TODO : Use numpy
# random_arrays= [] -> i name val
# TODO : Use range
# sorted_arrays= [] -> val = np.random.randint(1,4*length,size=length) replace val = np.sort(np.random.randint(1,4*length,size=length))
# TODO : Use range
# inverse_sorted_arrays = [] -> val = np.random.randint(1,4*length,size=length) replace val = np.fliplr(np.sort(np.random.randint(1,4*length,size=length)))
# that is it ,i do this for reduce size code because all this have same ideas .
nbr_experiments = 10

from tqdm import tqdm , trange

import numpy as np
np.random.seed(42)

tests = []

#lenghts = [1000,10000,100000,1000000]

lenghts = np.array(range(5,15,2))

tests_per_length = 5

for length in lenghts:
    for _ in range(tests_per_length):

        val = np.random.randint(1,4*length,size=length)

        test = (length, val)

        tests.append(test)

def sort_selection (t):
    i=0
    swap =0
    comp = 0
    for i in range(len(t)):
        j=i
        for j in range(len(t)):
          comp = comp + 1
          if t[j]>t[i] :
              c= t[i]
              t[i]=t[j]
              t[j]=c
              swap=swap+1
    return 'sort_selection', comp , swap


def sort_bull (t):
    i=0
    swap =0
    comp = 0
    for i in range(len(t)):
        for j in range(len(t)-i-1):
            comp = comp + 1
            if t[j]>t[j+1] :
              c= t[j+1]
              t[j+1]=t[j]
              t[j]=c
              swap=swap+1

    return 'sort_bull',comp , swap



def sort_insertion (t):
    comp = 0
    swap = 0
    for i in range(1,len(t)):
          c=t[i]
          j=i-1
          comp = comp + 1
          while (j>=0 and c < t[j]):
                comp = comp + 1
                t[j+1] = t[j]
                j=j-1
                swap=swap+1
          t[j+1] = c
    comp = comp - 1
    return 'sort_insertion' ,comp , swap

## TODO: Complete the code

funcs = [sort_bull, sort_insertion,sort_selection]

results = []

for i , (length, val) in tqdm(enumerate(tests),ncols=len(tests)):

    for func in funcs:

        func_name,comparison,swap = func(val)

        results.append((i,func_name,length,comparison ,swap ))
df = pd.DataFrame(results, columns=['id_test','function_name','array_length','comparison','swap'])

print(df)

df.to_csv('results.csv', index=False)

import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')

group_columns = ['function_name', 'array_length']
cal_columns = ['comparison', 'swap']

group_df = df.groupby(group_columns,as_index=False).mean()

calculated_results = group_df[group_columns+cal_columns]

function_names = list(calculated_results['function_name'].unique())

plt.title("comparaison")
plt.ylabel("array_length")
plt.xlabel("NB_comparison")
for function_name in function_names:
    df_plot = calculated_results[calculated_results['function_name'] == function_name]
    plt.plot(df_plot['array_length'], df_plot['comparison'],label=function_name)
plt.legend()

plt.title("swap")
plt.ylabel("array_length")
plt.xlabel("NB_swap")
for function_name in function_names:
    df_plot = calculated_results[calculated_results['function_name'] == function_name]
    plt.plot(df_plot['array_length'], df_plot['swap'],label=function_name)
plt.legend()

from complexity import get_complexity

y_plot = df_plot['array_length']
x_plot = df_plot['comparison']

get_complexity(x_plot,y_plot)

from complexity import get_complexity

y_plot = df_plot['array_length']
x_plot = df_plot['swap']

get_complexity(x_plot,y_plot)
 
# TODO: Complete the benchmark code
