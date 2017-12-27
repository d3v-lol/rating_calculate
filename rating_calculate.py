#!/usr/bin/python
#coding:utf8

from math import sqrt

'''
	We seek a balance between the proportion of positive estimates and 
	the uncertainty of a small number of observations.
	Use solution by Edwin Wilson. 

	as input:
		- sum of rating scores
		- ratings count
		- [min, max] rating scores
	as return:
		- user "middle" rating
'''

#----------------------------------------------------------------
#func

def calculate_rating(_sum_rating, _count_rating, _range):
	width_range = float(_range[1] - _range[0])
	quantile  = 1.64485

	phat   = (_sum_rating - _count_rating * _range[0]) / \
			width_range / float(_count_rating)
	rating = (
		phat + quantile * quantile / (2 * _count_rating) - \
		quantile * sqrt(
			(phat * (1 - phat) + quantile * quantile / \
			(4 * _count_rating)
		) / _count_rating)
	) / (1 + quantile * quantile / _count_rating)

	return rating * width_range + _range[0]

#----------------------------------------------------------------
#example run

if __name__ == '__main__':
	print calculate_rating(435, 100,[1,5])

