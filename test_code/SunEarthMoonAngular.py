from vpython import *

global AngularVelocityMoon
global AngularVelocityEarth

def currentAngle(time, AngularVelocity, startingTheta):
    return startingTheta + AngularVelocity * time

def positionMoon(t, theta0):
    theta = theta0 + AngularVelocityMoon * t
    return theta


def positionEarth(t, theta0):
    return theta0 + AngularVelocityEarth * t

def main1():
    G = 6.67408e-11

    # mass
    sunMass = 1.9891e30
    earthMass = 5.972e24
    moonMass = 7.348e22

    # In km (Equatorial radius)
    # earthRadius = 6378.137
    # sunRadius = earthRadius * 109.2
    # moonRadius = 0.2725 * earthRadius
    earthRadius = 1e10
    sunRadius = 5e10
    moonRadius = earthRadius / 4



    # in km
    moonDistScale = 10000
    distSunToEarth = 1.496e11
    distEarthToMoon = 384399.9 * moonDistScale

    # Gravitational Forces
    ForceEarthMoon = (G * earthMass * moonMass) / (distEarthToMoon**2)
    ForceEarthSun = (G * earthMass * sunMass) / (distSunToEarth**2)

    # Angular Velocities
    AngularVelocityMoon = sqrt(ForceEarthMoon / (moonMass * distEarthToMoon))
    AngularVelocityEarth = sqrt(ForceEarthSun / (earthMass * distSunToEarth))

    # Centripital Velocity
    velocityMoon = AngularVelocityMoon * distEarthToMoon
    velocityEarth = AngularVelocityEarth * distSunToEarth

    moonPosRelToEarth = vector(distEarthToMoon, 0, 0)
    sun = sphere(pos=vector(0, 0, 0), radius=sunRadius, color=color.orange)
    earth = sphere(pos=vector(distSunToEarth, 0, 0), radius=earthRadius, color=color.green, make_trail = True)
    moon = sphere(pos= earth.pos + moonPosRelToEarth , radius=moonRadius, color=color.blue, make_trail = True)

    # velocities
    earth.velocity = vector(0, 3e4, 0)
    moon.velocity = vector(0, 1e4, 0)

    # define initial time
    t = 0
    # define time interval
    dt = 3600
    startingTheta = 0

    while (t < 1e10):
        rate(3000)
        thetaAngleEarth = positionEarth(t + dt, startingTheta) - positionEarth(t, startingTheta)
        thetaMoon = positionMoon(t + dt, startingTheta) - positionMoon(t, startingTheta)

        # thetaAngleEarth = currentAngle(t + dt, AngularVelocityEarth, startingTheta) - currentAngle(t, AngularVelocityEarth, startingTheta)
        # thetaMoon = currentAngle(t + dt, AngularVelocityMoon, startingTheta) - currentAngle(t, AngularVelocityMoon, startingTheta)
        # Rotation only around z axis (0,0,1)
        earth.pos = rotate(earth.pos, angle=thetaAngleEarth, axis=vector(0, 0, 1))
        moonPosRelToEarth = rotate(moonPosRelToEarth, angle=thetaMoon, axis=vector(0, 0, 1))
        moon.pos = earth.pos + moonPosRelToEarth


        t = t + dt





main1()
