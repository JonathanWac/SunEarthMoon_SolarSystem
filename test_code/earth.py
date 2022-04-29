from vpython import *

def main():
	# simulate the motion of the earth around the sun

	# define constants
	G = 6.67408e-11

	# mass of the sun
	m_sun = 1.9891e30

	# radius of the sun (not to scale)
	# r_sun = 6.9634e8
	r_sun = 5e10

	# mass of the earth
	m_earth = 5.972e24

	# radius of the earth (not to scale)
	# r_earth = 6.367e6
	r_earth = 1e10

	# create the objects
	sun = sphere (pos=vector(0,0,0), radius = r_sun, color=color.yellow)
	
	earth = sphere (pos=vector(1.496e11,0,0), radius=r_earth, color=color.blue, make_trail = True)
	earth.velocity = vector (0,3e4,0)





	# define initial time
	t = 0

	# define time interval
	dt = 3600

	while (t < 1e10):
		rate(3000)
		earth.pos = earth.pos + earth.velocity * dt
		r_vector = earth.pos - sun.pos
		F_grav = -(G * m_sun * m_earth / (mag(r_vector)**2)) * (norm(r_vector))
		earth.velocity = earth.velocity + (F_grav / m_earth) * dt
		t = t + dt

main() 