#FORWARD FINITE DIFFERENCES
import matplotlib.pyplot as plt
t = []
x = []
with open('posData.csv','rt') as fid:
  count = 1
  for line in fid:
    # skip header
    if count > 1:
      line2 = line.strip('\n')
      list1 = line2.split(',')
      t.append(float(list1[0]))
      x.append(float(list1[1]))
    else:
      count += 1;
v = []
a = []
n = len(x)
for i in range(n - 1):
  d = (x[i + 1] - x[i]) / (t[i + 1] - t[i])
  v.append(d)
for i in range(n - 2):
  d = (v[i + 1] - v[i]) / (t[i + 1] - t[i])
  a.append(d)
ax1 = plt.subplot(3, 1, 1)
ax1.plot(t, x, 'bo-')
ax1.set(ylabel='x')
ax2 = plt.subplot(3, 1, 2)
ax2.plot(t[0:n - 1], v, 'ro-')
ax2.set(xlabel='time', ylabel='dx/dt by Forward finite difference')
ax2 = plt.subplot(3, 1, 3)
ax2.plot(t[0:n - 2], a, 'go-')
ax2.set(xlabel='time', ylabel='d2x/dt2 by Forward finite difference')
plt.show()

#BACKWARD FINITE DIFFERENCES
t = []
x = []
with open('posData.csv','rt') as fid:
  count = 1
  for line in fid:
    # skip header
    if count > 1:
      line2 = line.strip('\n')
      list1 = line2.split(',')
      t.append(float(list1[0]))
      x.append(float(list1[1]))
    else:
      count += 1;
v = []
a = []
n = len(x)
for i in range(1, n):
  d = (x[i] - x[i-1]) / (t[i] - t[i-1])
  v.append(d)
for i in range(2, n):
  d = (v[i-1] - v[i-2]) / (t[i] - t[i-1])
  a.append(d)
ax1 = plt.subplot(3, 1, 1)
ax1.plot(t, x, 'bo-')
ax1.set(ylabel='x')

ax2 = plt.subplot(3, 1, 2)
ax2.plot(t[1:n], v, 'ro-')
ax2.set(xlabel='time', ylabel='dx/dt by Backward finite difference')

ax2 = plt.subplot(3, 1, 3)
ax2.plot(t[2:n], a, 'go-')
ax2.set(xlabel='time', ylabel='d2x/dt2 by Backward finite difference')
plt.show()

#CENTRAL FINITE DIFFERENCES
t = []
x = []
with open('posData.csv','rt') as fid:
  count = 1
  for line in fid:
    # skip header
    if count > 1:
      line2 = line.strip('\n')
      list1 = line2.split(',')
      t.append(float(list1[0]))
      x.append(float(list1[1]))
    else:
      count += 1;
v = []
a = []
n = len(x)
for i in range(1, n-1):
  d = (x[i+1] - x[i-1]) / (t[i+1] - t[i-1])
  v.append(d)
for i in range(2, n-2):
  d = (v[i] - v[i-2]) / (t[i+1] - t[i-1])
  a.append(d)
ax1 = plt.subplot(3, 1, 1)
ax1.plot(t, x, 'bo-')
ax1.set(ylabel='x')
ax2 = plt.subplot(3, 1, 2)
ax2.plot(t[1:n - 1], v, 'ro-')
ax2.set(xlabel='time', ylabel='dx/dt by Central finite difference')
ax2 = plt.subplot(3, 1, 3)
ax2.plot(t[2:n - 2], a, 'go-')
ax2.set(xlabel='time', ylabel='d2x/dt2 by Central finite difference')
plt.show()