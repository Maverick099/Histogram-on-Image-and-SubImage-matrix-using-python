import numpy as n

pixelvalue = n.array([0, 1, 2, 3, 4, 5, 6, 7])
no_of_pixels = n.array([8, 10, 10, 2, 12, 16, 4, 2])

N = sum(no_of_pixels)
print(N)

i = len(no_of_pixels)
pdf = n.divide(no_of_pixels, N)
print(pdf)

cdf = n.array([])
sum = 0

for i in range(0, len(pdf)):
    sum = sum + pdf[i]
    cdf=n.append(cdf,sum)

print(cdf)


k=len(pixelvalue)-1

multipliedarray=n.multiply(cdf,k)
print(multipliedarray)

rounded_values=n.round(multipliedarray)
print(rounded_values)


newPixelCount =n.array([])
for i in range(0,len(pixelvalue)):
    sum=0
    for j  in range(0,len(pixelvalue)):
        if pixelvalue[i]==rounded_values[j]:
            sum=sum+no_of_pixels[j]
            newPixelCount = n.append(newPixelCount, sum)
        else:
            newPixelCount = n.append(newPixelCount, sum)
            




print(newPixelCount)
