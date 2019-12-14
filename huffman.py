from heapq import*
from collections import*
 
def huffmanencode(symb2freq):
    
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 
txt = "Basic huffman encoding test"
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1

huff = huffmanencode(symb2freq)

print(huff, "\n")
print( "Symbol\t\tFreq\t\tHuffman Code")
for p in huff:
    print(p[0],"\t\t",symb2freq[p[0]],"\t\t\t", p[1])