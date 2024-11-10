## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now

t =[10,2,1,14,8,7,6,9]

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
print(sort_selection (t))
## TODO: make Benchmarks

print('hello')