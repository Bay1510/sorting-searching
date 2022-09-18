from termcolor import colored
import os

data_awal = ['galda', 'zaki', ['ibnu', 'zaki'], 'kalam', ['zaki', 'ari', 'ibnu'], 'zaki']
data_str = []
data_list = {}

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def partition(l, kiri, kanan):
  pivot = l[kiri]
  urutan = kiri+1
  for j in range(kiri+1,kanan):
    if l[j] <= pivot:
      l[urutan],l[j]=l[j],l[urutan]
      urutan += 1
  l[urutan-1],l[kiri] = l[kiri],l[urutan-1]
  return urutan

def quicksort(data, kiri, kanan):
  if kanan <= kiri:
    return
  q = partition(data, kiri, kanan)
  quicksort(data, kiri, q-1)
  quicksort(data, q, kanan)
  return data

def fibonacci_search(data, x, n):
    fibMM0 = 0 
    fibMM1 = 1 
    fibMM = fibMM0 + fibMM1 
    while (fibMM < n):
        fibMM0 = fibMM1
        fibMM1 = fibMM
        fibMM = fibMM0 + fibMM1
    offset = -1 
    

    while (fibMM > 1):
        i = min(offset+fibMM0, n-1)
        if (data[i] < x):
            fibMM = fibMM1
            fibMM1 = fibMM0
            fibMM0 = fibMM - fibMM1
            offset = i
        elif (data[i] > x):
            fibMM = fibMM0
            fibMM1 = fibMM1 - fibMM0
            fibMM0 = fibMM - fibMM1
        else:
            return i


    if(fibMM1 and data[n-1] == x):
        return n-1


for i in range(len(data_awal)): #DATA TO DATA_STR
    if type(data_awal[i]) != list:
        data_str.append(data_awal[i])
        quicksort(data_str,0,len(data_str))
    else:
        data_list[i] = data_awal[i] #DATA TO DATA_LIST

for j in data_list:
    quicksort(data_list[j],0,len(data_list[j]))
    data_str.insert(j,data_list[j]) #INSERT DATA_LIST TO DATA_STR
#=============================================================================#
clear()
print(colored(data_awal, 'red'))
print(colored(data_str , 'magenta'))
print("")
x = 'zaki' #SEARCH
print("RESULT SEARCH ZAKI")
for i in reversed(range(len(data_str))):
    if data_str[i] == x:
        print('zaki berada di index ke -',i)
    else: 
        if type(data_str[i]) == list:
            data = fibonacci_search(data_str[i],x,len(data_str[i]))
            print("zaki berada di index ke -",i, 'kolom,', data)
        