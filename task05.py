def triangle_area(x, y, z):
    s = 0.5 * (x+y+z)
    area = (s * ((s-x) * (s-y) * (s-z))) ** 0.5
    return area 
    
