# bounce.py
#
# Exercise 1.5

bounce_frac = 3.0 / 5.0
height = 100

for i in range(10):
	height *= bounce_frac
	print(round(height, 4))
