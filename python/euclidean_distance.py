import numpy as np

coord = (-2, -5)
origin = (0,0)

def euclidean_distance(point, org):
    x1 = org[0]
    y1 = org[1]
    x2 = point[0]
    y2 = point[1]
    
    dist = np.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return dist

print(euclidean_distance(coord, origin))






























