#!/usr/bin/python
# -*-coding:utf-8-*-

'''
Binary find
'''

# def binFind(alist, key):
# 	low = 0
# 	high = len(alist) - 1
	
# 	while high - low >=1:
# 		if high - low == 1:
# 			if key == alist[high] or key == alist[low]:
# 				return key
# 			else:
# 				print "Can't find it!"
# 				return
# 		mid = (high + low) / 2
# 		# print "%d, %d, %d" %(low, mid, high)
# 		if key == alist[mid]:
# 			return key
# 		if key > alist[mid]:
# 			low = mid
# 		if key < alist[mid]:
# 			high = mid

def binFind(alist, low, high, key):
	if high - low < 2:
		if alist[low] == key or alist[high] == key: return key
		else: return
	else:
		mid = (low + high) // 2
		if alist[mid] == key: return key
		if key > alist[mid]: 
			low = mid + 1
			return binFind(alist, low, high, key)
		else:
			high = mid
			return binFind(alist, low, high, key)


if __name__ == '__main__':	
	a = range(2, 50, 4)
	print 'alist is:', a
	low = 0
	high = len(a) - 1
	mid = (high + low) / 2
	b = [binFind(a, low, high, c) for c in range(50)]
	print b

