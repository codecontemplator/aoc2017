import math

def get_spiral_coords(n):
    if n == 1: return (0, 0)
    
    # 1. Find the layer (radius)
    r = math.floor((math.sqrt(n - 1) + 1) / 2)
    
    # 2. Find the max value of the previous layer
    p = (2 * r - 1) ** 2
    # 3. Side length of current layer
    en = 2 * r
    
    # 4. Determine which side and offset
    if n <= p + en:            return (r, (n - p) - r)          # Right side
    elif n <= p + 2 * en:      return (r - (n - (p + en)), r)   # Top side
    elif n <= p + 3 * en:      return (-r, r - (n - (p + 2 * en))) # Left side
    else:                      return ((n - (p + 3 * en)) - r, -r) # Bottom side
    
    
x = get_spiral_coords(361527)    
print(x)
print(x[0] + x[1])

#(301, 25)
# 326