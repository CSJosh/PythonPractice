from graphics import *
from wheel import Wheel


newWin = GraphWin("Animated Wheel", 700, 500)
wheel_center = Point(200, 200)
tire_radius = 100

newWheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)
newWheel.set_color('green1', 'yellow1')

newWheel.draw(newWin)
newWheel.animate(newWin, 1, 0, 100)

newWin.mainloop()
