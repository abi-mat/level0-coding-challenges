def triangle(x, y, z):
    semiperimeter = 0.5 * (x+y+z) 
    s = semiperimeter
    area = (s * ((s-x) * (s-y) * (s-z))) ** 0.5
    print(area)
