#!python
#!python
cubit.cmd('reset')

cubit.cmd('create surface circle radius 0.00075 zplane ')
cubit.cmd('create surface circle radius 0.0012 zplane ')
cubit.cmd('create surface circle radius 0.00669 zplane ')
cubit.cmd('create surface circle radius 0.007417 zplane ')
cubit.cmd('create surface circle radius 0.0075 zplane')

for i in xrange(4,0,-1):
  cubit.cmd('subtract volume ' + str(i) + ' from volume ' + str(i+1) + ' keep')
  cubit.cmd('delete body ' + str(i+1))

cubit.cmd('compress all')
cubit.cmd('merge all')

cubit.cmd('curve 1  interval 20')
cubit.cmd('curve 1  scheme equal')

cubit.cmd('surface 1  scheme circle fraction 0.6 interval 1')
cubit.cmd('mesh surface 1 ')

for i in xrange(5, 1, -1):
  cubit.cmd('surface ' + str(i) + ' scheme hole rad_intervals 3 bias 0.0 ')
  cubit.cmd('mesh surface ' + str(i))


yy = 5

x_pitch=0.016
y_pitch=0.0142

#x_pitch = 12
#y_pitch = 10

x0 = 0
y0 = 0

length_row = 5

D_pellet = 0.8190

number_center_row=5
number_bottom_row=number_center_row-((yy-1)/2)
current_length=number_bottom_row

Master_matrix = []

def GenerateRow(x_pitch, x0, y0, length_row):
  row_xy = []
  for i in xrange(0,length_row):
    row_xy.append( (x0+i*x_pitch, y0) )
  return row_xy

for k in xrange(0, ((yy-1)/2)+1, 1):
  x_current=x0-0.5*x_pitch*k
  y_current=y0+y_pitch*k
  Master_matrix = Master_matrix + GenerateRow(x_pitch, x_current, y_current, current_length)
  current_length = current_length+1

current_length = current_length-1

for k in xrange(((yy-1)/2)+1, yy, 1):
  x_current2=x_current+0.5*x_pitch*(k-((yy-1)/2))
  y_current2=y_current+y_pitch*(k-((yy-1)/2))
  current_length = current_length-1
  Master_matrix = Master_matrix + GenerateRow(x_pitch, x_current2, y_current2, current_length)

for xy in Master_matrix:
  print xy
  cubit.cmd('Surface 1 5 4 3 2  copy move x ' + str(xy[0]) + ' y ' + str(xy[1]))

pellet_radius = (number_center_row / 2.) * x_pitch

cubit.cmd('create surface circle radius ' + str(1.05 * pellet_radius) + ' zplane')

cubit.cmd('move Surface 101  location ' + str(((number_bottom_row/2.) - 1/2.) * x_pitch) + ' ' + str((yy/2. - 1/2.) * y_pitch))

vol_string = ''
for i in xrange(1, 101):
  vol_string += str(i) + ' '

cubit.cmd('subtract volume ' + vol_string + ' from volume 101 keep')
cubit.cmd('delete body 101')

cubit.cmd('merge  all')
cubit.cmd('compress all')

surface_string = ''
for i in xrange(1, 96):
  surface_string += str(i) + ' '

cubit.cmd('surface 96  size auto factor 3')
cubit.cmd('mesh surface 96 ')

cubit.cmd('block 1 surface ' + surface_string)
cubit.cmd('block 2 surface 96')

block 1 2 element type quad4

cubit.cmd('Sideset 1 curve 96')

cubit.cmd('export Genesis  "/Users/bhiscox/projects/FiberFrog/problems/singlefiber.e"')
