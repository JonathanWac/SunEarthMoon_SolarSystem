from vpython import *


def main1():
    # define vectors
    v1 = vector(1, 9, 4)
    v2 = vector(8, 3, 5)
    # add two vectors
    v3 = v1 + v2
    print(v3)

    # multiply vector by scalar
    v4 = 3 * v3
    print(v4)

    #magnitude of a vector
    print(f"Magnitude of v1 = {mag(v1)}")
    print(f"Magnitude of v2 = {mag(v4)}")

    # get unit vectors
    print(f"Unit vector in the direction of v3 = {norm(v3)}")
    print(f"Unit vector in the direction of v4 = {norm(v4)}")

    # get dot product
    v5 = dot(v1, v2)
    print(f"v1 dot v2 = {v5}")

    # get cross product
    v6 = cross(v1, v2)
    v7 = cross(v3, v4)
    print(f"v1 cross v2 = {v6}")
    print(f"v3 cross v4 = {v7}")

    # position vectors
    tail = vector(9.5, 7, 3)
    head = vector(4, -13, 5)


main1()
