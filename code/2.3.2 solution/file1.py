#!/usr/bin/python
# -*- coding: utf-8 -*-
goodstr = "I come in peace."
evilstr = "Prepare to be destroyed!"
"""
                <m�T[�4w��$��h��Y��gV��͇	x�������;8����~�L��ӑ�7���ފ�7����3��4]���γ��>�"erWKu���vF#Q��;�I�^�Ǥ,z�3i���k֓�W
"""
goodhex = "00000000000000003c6db6545b941a34f779268e61d24a794688ffc59b9b6675684eacd8715978eb1bffccb19a076dbfb3b38e093dc7fb87efc4cb4fad391bf37c1c5d9de8ab737d1fef210d63380c9345da883f2ceb3bb17903ed11d226572574b75da09597764623511988b23bc549821c5eddc7a42cf7ad93369b395e86bd6939b57"
evilhex = "00000000000000003c6db6545b941a34f779268e61d24a79468ffc59b9b6675684eacd8715978eb1bffccb19a076dbfb3bb8e093dc7fb87efc4cb4fad391bfb7c1c5d9de8ab737d1fef210d63380c9345da883f2ceb3bb97903ed11d226572574b75da09597764623511988b23bc549829c5dddc7a42cf7ad93369b395e8ebd6939b57"
# read the python file itself, if it's xxx, print peace, otherwise print evil
f = open(__file__, 'r')
pylines = f.readlines()
temp = pylines[5]
concat = ""
for letter in temp:
	tmp = ord(letter)
	concat = concat + hex(tmp)[2:]
concat = concat[:-1]
if(concat == goodhex):
	print goodstr
else:
	print evilstr
