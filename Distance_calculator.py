import math

p1 = float(input('First point latitude: '))
m1 = float(input('First point longitude: '))
p2 = float(input('Second point latitude: '))
m2 = float(input('First point longitude: '))

p1 = math.radians(p1)
p2 = math.radians(p2)
m1 = math.radians(m1)
m2 = math.radians(m2)

R = 6372.8
dp = p2 - p1
dm = m2 - m1
a = (math.sin(dp/2))**2+math.cos(p1)*math.cos(p2)*(math.sin(dm/2))**2
c = 2*math.asin(math.sqrt(a))
d = R*c

print('The distance between the two points is: ',d)
