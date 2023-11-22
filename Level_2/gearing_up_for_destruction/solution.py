from fractions import Fraction

def solution(pegs):
    if len(pegs) < 2:
        return [-1, -1]

    sum_distances = sum((-1) ** i * (pegs[i + 1] - pegs[i]) for i in range(len(pegs) - 1))
    
    if len(pegs) % 2 == 0:
        first_gear_radius = Fraction(-2 * sum_distances, 3)
    else:
        first_gear_radius = Fraction(2 * sum_distances, 1)

    if first_gear_radius < 1:
        return [-1, -1]

    current_radius = first_gear_radius
    for i in range(len(pegs) - 1):
        distance = pegs[i + 1] - pegs[i]
        next_radius = distance - current_radius

        if next_radius <= 0:
            return [-1, -1]
        current_radius = next_radius

    return [first_gear_radius.numerator, first_gear_radius.denominator]
