import numpy as n

pixelvalue = n.array([0, 1, 2, 3, 4, 5, 6, 7])
no_of_pixels = n.array([8, 10, 10, 2, 12, 16, 4, 2])

N = sum(no_of_pixels)
print(N)

i = len(no_of_pixels)
pdf = n.divide(no_of_pixels, N)
print(pdf)

cdf = n.array([])
_sum = 0

for i in range(0, len(pdf)):
    _sum = _sum + pdf[i]
    cdf = n.append(cdf, _sum)

print(cdf)

k = len(pixelvalue) - 1

multipliedarray = n.multiply(cdf, k)
print(multipliedarray)

rounded_values = n.round(multipliedarray)
print(rounded_values)

newPixelCount = n.zeros(len(pixelvalue))



for x in range(0,len(pixelvalue)):
    for y in range(0,len(pixelvalue)):

for i in range(0,len(rounded_values)):
    sum_=no_of_pixels[i]
    for j in range(0,len(rounded_values)):
        if rounded_values[i]==rounded_values(j) and i!=j:
            sum_=sum_+no_of_pixels[j]
            i=i+1                 v  b    mmnhv u975
        else:
            sum_=sum_+0




print(pixelvalue)
print(no_of_pixels)
print(newPixelCount)
