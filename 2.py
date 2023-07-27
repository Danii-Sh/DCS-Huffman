import itertools
import numpy as np
from scipy.linalg import solve


#Example Huffman coding implementation
# Distributions are represented as dictionaries of { 'symbol': probability }
# Codes are dictionaries too: { 'symbol': 'codeword' }

def huffman(p):
    '''Return a Huffman code for an ensemble with distribution p.'''
    assert(0.9999 <= sum(p.values()) <= 1.0001) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        return dict(zip(p.keys(), ['0', '1']))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(p.items(), key=lambda (i,pi): pi)
    return sorted_p[0][0], sorted_p[1][0]




np.set_printoptions(threshold=np.inf)

print ('Enter number of Symbols ')
i= int(input())
print ('Enter string size ')
j= int(input())
a = np.random.randint(i,size=j)
#print a
print type(a)
print "****"



print ('Enter coding length k ')
k = int(input ())

b=np.empty
b=a
if(len(a)%k !=0):
    for count1 in range (0,((int(len(a)/k)+1)*k)-len(a)):
        b=np.append(b,np.random.randint(i))


#print b
#print (len(b))
print "****"
all_codes_counts=[[],[]]


for count1 in range (0,int(len(b)/k)):
    m=''
    for count2 in range (0,k):
        m=m+str(b[count2+(count1*k)])
    
#    sys.stdout.write(m)
#    sys.stdout.write(' ')
    
    if m in all_codes_counts[0]:
        all_codes_counts[1][all_codes_counts[0].index(m)] +=1
        c=0
    else:
        all_codes_counts[0].append(m)
        all_codes_counts[1].append(1)
print "****"
print all_codes_counts
print "****"


ex={}

for count1 in range (0,int(len(all_codes_counts[0]))):
    ex[all_codes_counts[0][count1]]=(float(all_codes_counts[1][count1])/float(int(len(b)/k)))

print ex
print "****"
print ('Symbol , Huffman Code : Pair is : ')
huffcode= huffman(ex)
print huffcode
print "****"
#print huffcode

Avg_HuffCode_Len=0
for  count1 in range (0,int(len(all_codes_counts[0]))):
    Avg_HuffCode_Len+=(ex[all_codes_counts[0][count1]])* len(huffcode[all_codes_counts[0][count1]])
print 'Average HuffmanCode Length is ',Avg_HuffCode_Len


