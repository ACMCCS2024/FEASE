from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
from charm.toolbox.ABEnc import ABEnc
from msp import MSP
from policytree import PolicyParser
from secretutil import SecretUtil
import time

import re, numpy, copy

group = PairingGroup('MNT224')

sum_time = 0       
for i in range(10):
    start = time.time()

    g_1 = group.random(G1)
    
    end = time.time()
    time_1 = end - start
    sum_time += time_1
    
times = sum_time/10

print('Choose a generator from G1:', format(times * 1000, '7.2f'))
with open('Results/Test.txt', 'a') as f:
    f.write('Choose a generator from G1:' + format(times * 1000, '7.2f'))
    f.write('\n')         

sum_time = 0
for i in range(10):
    start = time.time()

    g_2 = group.random(G2)  
  
    end = time.time()
    time_1 = end - start    
    sum_time += time_1
    
times = sum_time/10    
print('Choose a generator from G2:', format(times * 1000, '7.2f'))
with open('Results/Test.txt', 'a') as f:
    f.write('Choose a generator from G2:' + format(times * 1000, '7.2f'))
    f.write('\n')
    
sum_time = 0
for i in range(10):       
    start = time.time()

    a = group.random(ZR)

    end = time.time()
    time_1 = end - start
    sum_time += time_1
    
times = sum_time/10        
print('Choose a random number from ZR:', format(times * 1000, '7.2f'))  
with open('Results/Test.txt', 'a') as f:
    f.write('Choose a random number from ZR:' + format(times * 1000, '7.2f'))
    f.write('\n')
    
sum_time = 0
for i in range(10):  
    start = time.time()

    e_g1g2 = pair(g_1, g_2)

    end = time.time()
    time_1 = end - start
    sum_time += time_1    

times = sum_time/10     
print('Calculate a pairing G1 x G2 -> GT:', format(times * 1000, '7.2f')) 
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate a pairing G1 x G2 -> GT:' + format(times * 1000, '7.2f')) 
    f.write('\n')
    
sum_time = 0
for i in range(10):  
    start = time.time()

    pk_1 = g_1 ** a
 
    end = time.time()
    time_1 = end - start
    sum_time += time_1 
    
times = sum_time/10       
print('Calculate an exponentiation on G1:', format(times * 1000, '7.2f'))  
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate an exponentiation on G1:' + format(times * 1000, '7.2f')) 
    f.write('\n')
    
sum_time = 0
for i in range(10): 
    start = time.time()

    pk_2 = g_2 ** a

    end = time.time()
    time_1 = end - start
    sum_time += time_1 
    
times = sum_time/10         
print('Calculate an exponentiation on G2:', format(times * 1000, '7.2f'))  
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate an exponentiation on G2:' + format(times * 1000, '7.2f')) 
    f.write('\n')
    
sum_time = 0
for i in range(10): 
    start = time.time()

    pk_3 = e_g1g2 ** a

    end = time.time()
    time_1 = end - start
    sum_time += time_1   
    
times = sum_time/10       
print('Calculate an exponentiation on GT:', format(times * 1000, '7.2f'))  
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate an exponentiation on GT:' + format(times * 1000, '7.2f')) 
    f.write('\n')
    
sum_time = 0
for i in range(10): 
    start = time.time()

    kw = 'L'
    Hash = group.hash(kw, G1)

    end = time.time()
    time_1 = end - start    
    sum_time += time_1  
    
times = sum_time/10         
print('Calculate the hash of a string to G1:', format(times * 1000, '7.2f'))  
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate the hash of a string to G1:' + format(times * 1000, '7.2f')) 
    f.write('\n')
    
sum_time = 0
for i in range(10): 
    start = time.time()

    kw = 'L'
    Hash = group.hash(kw, G2)

    end = time.time()
    time_1 = end - start
    sum_time += time_1     

times = sum_time/10     
print('Calculate the hash of a string to G2:', format(times * 1000, '7.2f'))  
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate the hash of a string to G2:' + format(times * 1000, '7.2f')) 
    f.write('\n')

a = group.random(ZR)
b = group.random(ZR)
tk_1 = g_1 ** a
tk_2 = g_1 ** b
tk_3 = g_2 ** a
tk_4 = g_2 ** b

sum_time = 0
for i in range(10): 
    start = time.time()

    tk_12 = tk_1 * tk_2

    end = time.time()
    time_1 = end - start
    sum_time += time_1      

times = sum_time/10     
print('Calculate a multiplication on G1:', format(times * 10000, '7.2f'))  
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate a multiplication on G1:' + format(times * 1000, '7.2f')) 
    f.write('\n')
    
sum_time = 0
for i in range(10): 
    start = time.time()

    tk_34 = tk_3 * tk_4

    end = time.time()
    time_1 = end - start
    sum_time += time_1  

times = sum_time/10          
print('Calculate a multiplication on G2:', format(times * 10000, '7.2f')) 
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate a multiplication on G2:' + format(times * 1000, '7.2f')) 
    f.write('\n')
    
sum_time = 0
for i in range(10): 
    start = time.time()

    pair = e_g1g2 * e_g1g2

    end = time.time()
    time_1 = end - start
    sum_time += time_1     

times = sum_time/10      
print('Calculate a multiplication on GT:', format(times * 10000, '7.2f')) 
with open('Results/Test.txt', 'a') as f:
    f.write('Calculate a multiplication on GT:' + format(times * 1000, '7.2f')) 
    f.write('\n')
