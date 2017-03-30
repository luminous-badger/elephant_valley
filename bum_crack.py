#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Far right, X-axis. Bum crack of infinity ...
# JM Fri 26 Jun 2015 11:25:29 BST

from PIL import Image
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list
import sys

start = timer()

X_MIN =  0.32
X_MAX =  0.35
Y_MIN = -0.075
Y_MAX = -0.03
offset     = 0.0001
maxiter    = 9950
calc_count = 0
rnum       = 93
lenlc      =  len( colour_list ) 

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 
print 'xmin:', X_MIN ,'xmax:', X_MAX
print 'ymin:', Y_MIN ,'ymax:', Y_MAX

if ( len( sys.argv ) == 2 ):
	sys.exit()

white      = (255,255,255)
black      = (   0,   0,   0 )
randcolour = ( 248,248,255) 
dim_grey                  = (105,105,105) 
light_grey                = (211,211,211)
dark_grey                 = (169,169,169)

img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( 0, 0 )
		C = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = Z**2 + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		#mycolour = ( 23 * iter_count, 43 * iter_count, 33 * iter_count ) 
		
                if ( iter_count + rnum  >= lenlc ):
                        mycolour = colour_list[ iter_count % lenlc ]
                else:   
                        mycolour = colour_list[ iter_count + rnum  ]

		if ( iter_count <= 3 ):
			try:
				img.putpixel( ( x_pixel,  y_pixel ), white ) 
			except:
				print 'Err: X,Y', x_pixel,  y_pixel
				#pass
		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

print 'Mandelbrot and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count

fname = 'Bum_Crack_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '.png'
print 'Fname:', fname

img.show()
#img.save( fname )

