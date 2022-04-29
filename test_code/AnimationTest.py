from vpython import *


def main1():
    ball = sphere(pos=vector(0,0,0), radius = 0.5, color = color.red)

    dx = 0.05

    while(ball.pos.x < 1):
        rate(30)
        ball.pos.x += dx
    ...
    #motion under gravity

    #define the object
    ball = sphere(pos=vector(-5,0,0), radius = 0.5, color = color.red)
    ball.mass = 1

    F_grav = vector(0, ball.mass * -9.8, 0)

    #initial velocity
    ball.velocity = vector(5, 5, 0)

    #initial time
    t=0
    dt = 0.01

    #drag coefficient (air resistance)
    drag_coeff = 0.1

    while(t<4):
        rate(30)
        F_drag = drag_coeff * (mag(ball.velocity)**2) * (-norm(ball.velocity))
        F_net = F_grav + F_drag
        ball.velocity += (F_net / ball.mass) *dt
        ball.pos += ball.velocity*dt


        t += dt



main1()