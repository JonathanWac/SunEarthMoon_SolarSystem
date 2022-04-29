import math
from vpython import *


# Position at each time
def positionMoon(t):
    theta = theta0 + AngularVelocityMoon * t
    return theta


def positionEarth(t):
    return theta0 + AngularVelocityEarth * t


def fromDaysToS(d):
    return d * 24 * 60 * 60


def fromStoDays(s):
    return s / 60 / 60 / 24


def fromDaysToh(d):
    return d * 24


lamp = local_light(pos=vector(0, 0, 0), color=color.yellow)
# Data in units according to the International System of Units
G = 6.67 * math.pow(10, -11)

# Mass of the Earth
earthMass = 5.973 * math.pow(10, 24)
# Mass of the Moon
moonMass = 7.347 * math.pow(10, 22)

# Mass of the Sun
sunMass = 1.989 * math.pow(10, 30)
# Radius Earth-Moon
distEarthToMoon = 384400000
# Radius Sun-Earth
distSunToEarth = 149600000000
# RadiusMoonToSun = 227900000000
# Force Earth-Moon
ForceEarthMoon = G * (earthMass * moonMass) / math.pow(distEarthToMoon, 2)
# Force Earth-Sun
ForceEarthSun = G * (sunMass * earthMass) / math.pow(distSunToEarth, 2)

# Angular velocity of the Moon with respect to the Earth (rad/s)
AngularVelocityMoon = math.sqrt(ForceEarthMoon / (moonMass * distEarthToMoon))
# Velocity v of the Moon (m/s)
velocityMoon = AngularVelocityMoon * distEarthToMoon
print("Angular velocity of the Moon with respect to the Earth: ", AngularVelocityMoon, " rad/s")
print("Velocity v of the Moon: ", velocityMoon / 1000, " km/s")

# Angular velocity of the Earth with respect to the Sun(rad/s)
AngularVelocityEarth = math.sqrt(ForceEarthSun / (earthMass * distSunToEarth))

# Velocity v of the Earth (m/s)
velocityEarth = AngularVelocityEarth * distSunToEarth

print("Angular velocity of the Earth with respect to the Sun: ", AngularVelocityEarth, " rad/s")
print("Velocity v of the Earth: ", velocityEarth / 1000, " km/s")

# Initial angular position
theta0 = 0

# Graphical parameters
# print("\nSimulation Earth-Moon-Sun motion\n")
days = 365
seconds = fromDaysToS(days)
# print("Days: ",days)
# print("Seconds: ",seconds)

moonPosRelToEarth = vector(384, 0, 0)
sun = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=700)
earth = sphere(pos=vector(1500, 0, 0), color=color.blue, radius=60, make_trail=True)
moon = sphere(pos=earth.pos + moonPosRelToEarth, color=color.white, radius=10, make_trail=True)

# thetaTerra1 = 0
t = 0
dt = 5000
# dthetaE = positionEarth(t+dt)- positionEarth(t)
# dthetaM = positionMoon(t+dt) - positionMoon(t)
#
# print("delta t:",dt,"seconds. Days:",fromStoDays(dt),"hours:",fromDaysToh(fromStoDays(dt)),sep=" ")
# print("Variation angular position of the Earth:",dthetaE,"rad/s that's to say",degrees(dthetaE),"degrees",sep=" ")
# print("Variation angular position of the Moon:",dthetaM,"rad/s that's to say",degrees(dthetaM),"degrees",sep=" ")

while t < seconds:
    rate(500)
    thetaAngleEarth = positionEarth(t + dt) - positionEarth(t)
    thetaMoon = positionMoon(t + dt) - positionMoon(t)
    # Rotation only around z axis (0,0,1)
    earth.pos = rotate(earth.pos, angle=thetaAngleEarth, axis=vector(0, 1, 0))
    moonPosRelToEarth = rotate(moonPosRelToEarth, angle=thetaMoon, axis=vector(0, 1, 0))
    moon.pos = earth.pos + moonPosRelToEarth

    t += dt
