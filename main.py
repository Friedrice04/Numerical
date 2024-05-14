from src.differentiation import *
from src.interpolation import *


def main():
    x = [   10.,          15.,           20.,            25.,            30.,            40.,            45.,            50.]
    fx = [  11381553.,    184091718.,    1351087483.,    6368625348.,    22650381813.,   168149106543.,  382355402808.,  797519823673.]
    ans = lagrangian(x, fx, 2)
    print(ans)
    ans = poly_newton_coefficient(x, fx, 2)
    print()
    print(ans)


if __name__ == "__main__":
    main()
