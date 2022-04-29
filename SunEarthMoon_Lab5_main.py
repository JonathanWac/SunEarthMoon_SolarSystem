# References
# https://gist.github.com/CodeDotJS/64f0d3d86d05b93af3b6
# https://pypi.org/project/solarsystem/
# https://www.astropy.org/

import solarsystem
import astropy
from vpython import *

G = 6.67408e-11


def gravAcc(obj, otherObj):
    rVector = obj.pos - otherObj.pos
    acceleration = -((G * otherObj.mass) / mag2(rVector))
    acceleration *= norm(rVector)
    return acceleration


def main1():
    planetoidList = []



    # In km (Equatorial radius)
    # earthRadius = 6378.137
    # sunRadius = earthRadius * 109.2
    # moonRadius = 0.2725 * earthRadius
    ############################################ Creating Planet Radi ############################################

    sunRadius = 5e10
    mercury = 0
    venus = 0
    earthRadius = 1e9
    moonRadius = 1000
    mars = 0
    jupiter = 0
    saturn = 0
    uranus = 0
    neptune = 0
    pluto = 0

    ############################################ Creating Planet Distances ############################################
    # in km
    moonDistScale = 10000
    earthDistFromSun = 1.495e11
    moonDistFromEarth = 3.848e8
    mercury = 0
    venus = 0
    mars = 0
    jupiter = 0
    saturn = 0
    uranus = 0
    neptune = 0
    pluto = 0

    # moonDistScale = 10000
    # earthDistFromSun = 149600000
    #
    # moonDistFromEarth = 3.848e8
    # mercury = 0
    # venus = 0
    # mars = 0
    # jupiter = 0
    # saturn = 0
    # uranus = 0
    # neptune = 0
    # pluto = 0


    ############################################ Creating Planet Spheres ############################################
    sun = sphere(pos=vector(0, 0, 0), radius=sunRadius, color=color.orange)
    earth = sphere(pos=vector(earthDistFromSun, 0, 0), radius=earthRadius, color=color.green, make_trail=True)
    moon = sphere(pos=vector(earthDistFromSun + moonDistFromEarth, 0, 0), radius=moonRadius,
                  color=color.blue, opacity=0)
    bigMoon = sphere(pos=vector(earthDistFromSun + 50 * moonDistFromEarth, 0, 0), radius=moonRadius * 1000,
                     color=color.blue, opacity=1, make_trail=True)
    # mercury = sphere(pos=vector(-1, 0, 0), radius=-2, color=color.cyan, make_trail=True)
    # venus = sphere(pos=vector(-1, 0, 0), radius=-2, color=color.cyan, make_trail=True)
    # mars = sphere(pos=vector(-1, 0, 0), radius=-2, color=color.cyan, make_trail=True)
    # jupiter = sphere(pos=vector(-1, 0, 0), radius=-2, color=color.cyan, make_trail=True)
    # saturn = sphere(pos=vector(-1, 0, 0), radius=-2, color=color.cyan, make_trail=True)
    # uranus = sphere(pos=vector(-1, 0, 0), radius=-2, color=color.cyan, make_trail=True)
    # neptune = sphere(pos=vector(-1, 0, 0), radius=-2, color=color.cyan, make_trail=True)
    # pluto = sphere(pos=vector(-1, 0, 0), radius=-2, color=color.cyan, make_trail=True)
    scene.camera.follow(sun)

    ############################################ Creating Planet Masses ############################################

    sun.mass = 1.9891e30
    earth.mass = 5.972e24
    moon.mass = 7.348e22
    # mercury.mass = 0
    # venus.mass = 0
    # mars.mass = 0
    # jupiter.mass = 0
    # saturn.mass = 0
    # uranus.mass = 0
    # neptune.mass = 0
    # pluto.mass = 0


    # velocities
    sun.velocity = vector(0, 0, 0)
    earth.velocity = vector(0, 2.978e4, 0)
    moon.velocity = vector(0, 1022, 0) + earth.velocity
    # mercury.velocity = vector(0, 0, 0)
    # venus.velocity = vector(0, 0, 0)
    # mars.velocity = vector(0, 0, 0)
    # jupiter.velocity = vector(0, 0, 0)
    # saturn.velocity = vector(0, 0, 0)
    # uranus.velocity = vector(0, 0, 0)
    # neptune.velocity = vector(0, 0, 0)
    # pluto.velocity = vector(0, 0, 0)

    planetoidList.append(sun)
    planetoidList.append(earth)
    planetoidList.append(moon)

    # define initial time
    t = 0

    # define time interval
    dt = 3600

    while t < 1e10:
        rate(300)

        for obj1 in planetoidList:
            for obj2 in planetoidList:
                if obj1 != obj2:
                    obj1.velocity += gravAcc(obj1, obj2) * dt

        for obj in planetoidList:
            obj.pos += obj.velocity * dt

        r_me = earth.pos - moon.pos
        bigMoon.pos = moon.pos + (50 * mag(r_me) * norm(r_me))

        t = t + dt


main1()
