"""
This program creates accurate 21cm figures for construction of
the protractor for a Science Aficionado Horn Radio Telescope
elevation axis.

To use this template.   Attached to board to hold telescope
(Often a 16 x 16 inch square (or 40x40cm square).   Place
the template 1 inch (or 20cm) below the top edge, 4inches 
(or 10 cm) from the front of the base.  The x and y axies of
the template should be parallel to the sides of the board.

Then drill pilot holes (1/8 inch or 3 mm) at the vertex
and each of the red dots on the templaete.

Finally take a 5/16 inch drill bit (or 8mm)and re-drill all holes
For the pairs of holes for setting th angle, tilt the drill
to connect the two holes.

After assembling the telecope, Use two 1/4 inc bolts to hold the horn 
and two more bolts to set the telescope elevation axis. 
Glen Langston, National Science Foundation 
2023 October 26 
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# This example fits a4 paper with 5mm margin printers
# 
# figure settings
figure_width = 23. # cm
figure_height = 25. # cm
left_right_margin = 1 # cm
top_bottom_margin = 1 # cm

# Don't change
left   = left_right_margin / figure_width # Percentage from height
bottom = top_bottom_margin / figure_height # Percentage from height
width  = 1 - left*2
height = 1 - bottom*2
cm2inch = 1/2.54 # inch per cm

# specifying the width and the height of the box in inches
fig = plt.figure(figsize=(figure_width*cm2inch,figure_height*cm2inch))
ax = fig.add_axes((left, bottom, width, height))

# limits settings (important)
plt.xlim(0, figure_width * width)
plt.ylim(0, figure_height * height)

# Ticks settings
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))

# Grid settings
ax.grid(color="gray", which="both", linestyle=':', linewidth=0.5)
# flip plot
ax.xaxis.tick_top()
# want y axis to increase going down
ax.invert_yaxis()

# now prepare to draw the radio arc and lambda 21cm
radius = 21.12
# now compute sin wave for 21cm
#theta = np.linspace(2 * np.pi, 0, 37)
lam = np.arange( 0., 1.05, .01)
# now create x array the radius of the circle
x = lam*radius
cm21 = 2.  # amplitude of wave
phi = lam * 2.*np.pi   # range 0 to 2 pi
nphi = len(phi)
y = cm21 * np.sin( phi)
cm21angle = 2.*np.pi*10./360.  # now rotate the plot 40 degrees
xp = (x * np.cos(cm21angle)) - (y * np.sin( cm21angle))
yp = (x * np.sin(cm21angle)) + (y * np.cos( cm21angle))
#yp = - yp
ax.plot(xp, yp, lw=3, color="purple")
ax.text( 7., 1., "21cm Wavelength", fontsize=18, color="purple")
ax.text( 9., 21.25, "Elevation Axis Template", fontsize=18, color="blue")
ax.text( 9., 21.75, "Science Aficionados -- Langston ", fontsize=12, color="blue")
ax.text( 9., 22.25, "National Science Foundation", fontsize=12, color="blue")
ax.text( 9., 22.75, "https://github.com/WVURAIL/lightwork")
# prepare to draw straight lines
y = 0. * x
# need to shift the middle text labels up, negative
yoff = [ 0, 0, 0, -.25, -.5, -.5, -.5, -.25, 0, 0] 
for iii in np.arange( 10, 91, 10):
    anangle = 2.*np.pi*iii/360.  # now rotate the plot 40 degrees
    xp = (x * np.cos(anangle)) - (y * np.sin( anangle))
    yp = (x * np.sin(anangle)) + (y * np.cos( anangle))
    ax.plot(xp, yp, lw=1, color="grey")
    # need to move label toward origin slightly
    ax.text( xp[98 - int((90-iii)/10)], yp[98]+yoff[int(iii/10)], ' '+str(iii), fontsize=18)
    xtick = [xp[97],xp[98]]
    ytick = [yp[97],yp[98]]
    ax.plot(xtick,ytick,lw=7, color="red")
    xtick = [xp[102],xp[103]]
    ytick = [yp[102],yp[103]]
    ax.plot(xtick,ytick,lw=7, color="red")

# add red dot/square at vertex
ax.plot([0.,.1],[0.,.1],lw=7, color="red")

#  now draw 5 degree tics
x = np.array([20.5, 21.5])
y = 0. * x
for iii in np.arange( 5, 91, 10):
    anangle = 2.*np.pi*iii/360.  # now rotate the plot 40 degrees
    xp = (x * np.cos(anangle)) - (y * np.sin( anangle))
    yp = (x * np.sin(anangle)) + (y * np.cos( anangle))
    ax.plot(xp, yp, lw=1, color="purple")

# add y axis tick marks inside the plot
for iii in np.arange( 5, 25, 5):
    ax.plot([0., .7],[iii,iii], lw=3, color="purple")
    ax.text(.8, iii+.2, str(iii), color="purple", fontsize=14)

# vertical line on the y axis
ax.plot([0., 0.],[0.,21.], lw=3, color="purple")

# feed probe length
y = np.array([21.-5.2, 21.0])
x = y * 0. + 18.
ax.plot(x, y, lw=3, color="green")
ax.text(18.2, 21., "Feed Probe Length", color="green", \
        rotation="vertical", fontsize=16)
ax.text(17.3, 21., "5.2cm", color="green", \
        rotation="vertical", fontsize=16)
# feed probe offset
y = np.array([21.-7.4, 21.])
x = y * 0. + 20.
ax.plot(x, y, lw=3, color="brown")
ax.text(20.2, 21., "Feed Probe Offset", color="brown", \
        rotation="vertical", fontsize=16)
ax.text(19.3, 21., "7.4cm", color="brown", \
        rotation="vertical", fontsize=16)

# draw a 21cm arc
thetas = lam * 2.*np.pi
x = radius * np.cos(thetas)
y = radius * np.sin(thetas)
ax.plot(x, y, lw=3, color="blue")

    
# save figure ( printing png file had better resolution, pdf was lighter and better on screen)
plt.show()
fig.savefig('ElAxisCm.png', dpi=1000)
plt.show()
fig.savefig('ElAxisCm.pdf')
plt.show()
fig.savefig('ElAxisCm.svg')
