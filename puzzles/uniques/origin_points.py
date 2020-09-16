# Given a random set of points on a 2 dimensional plane and an origin point,
# where each point is a combination of a TAG eg 'A' or 'B' or any character 
# where each point is in the form (x,y)
# Calculate the radius of a circle that will encompas the nearest N points
# where No points in N have the same tag.


import heapq


def heapify_points(p, tags, o=(0,0)):
	# will MinHeap sort all points by distance from origin
	h = [
		( (p[i][0]-o[0])**2 + (p[i][1]-o[1])**2, tags[i], p[i] )
		for i in range(len(tags))
	]
	heapq.heapify(h)
	return h

def get_unique_points(h):
	tags = ""
	points = []
	while len(h):
		d, t, p = heapq.heappop(h)
		if t in tags:
			break
		else:	
			tags = tags + t
			points.append((d,t,p,))
	# return radius of furthest point in set plus set.
	return points[-1][0]**.5,  points

def get_nearest_points(h, n):
	if n >= len(h):
		n = len(h)
	return [heapq.heappop(h) for _ in range(n)]

def get_furthest_points(h, n):
	heapq._heapify_max(h)
	if n >= len(h):
		n = len(h)
	nh =  [heapq.heappop(h) for _ in range(n)]
	heapq.heapify(h)
	return nh

if __name__ == '__main__':
	from random import randint, choice
	from string import ascii_uppercase
	for _ in range(10):
		num_points = randint(1,20)
		points = [(randint(0,100), randint(0,100)) for _ in range(num_points)]
		tags = ''.join([choice(ascii_uppercase[:4]) for _ in range(num_points)])
		h = heapify_points(points, tags, o=(0,0))
		print(h)
		#print('Nearest  3: ', get_nearest_points(h, 3))
		#print('Furthest 3: ', get_furthest_points(h, 3))
		print('Unique   s: ', get_unique_points(h), '\n')



