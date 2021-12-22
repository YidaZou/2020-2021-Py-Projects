"""
Yida Zou
"""

from statistics import mean
import scipy.stats as st
inputData = open("CIData.txt",'r')
data = []
for row in inputData:
  data += [float(row)]
inputData.close()

# we will need the size of the data list later
n = len(data)

# sample average
xBar = mean(data)

#stdDev
sigma = 2.65

z = st.norm.ppf(1-(1-0.8)/2)

muLow = xBar - z*sigma/n**(1/2)
muHigh = xBar + z*sigma/n**(1/2)

print("The confidence interval for the population mean of our supplier density is:")
print(muLow, "< mu <", muHigh)