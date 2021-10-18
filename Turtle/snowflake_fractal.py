import turtle as t
from typing import Tuple
from math import sqrt


def snowflake_side(start: Tuple[float, float], end: Tuple[float, float], iterations: int) -> None:
    if iterations == 0:
        t.goto(end)
    else:
        difference_vector_x = end[0] - start[0]
        difference_vector_y = end[1] - start[1]
        first_midpoint = (start[0] + difference_vector_x/3,
                          start[1] + difference_vector_y/3)
        second_midpoint = (start[0] + difference_vector_x *
                           2/3, start[1] + difference_vector_y*2/3)
        outer_point = (start[0] + difference_vector_x/2 - difference_vector_y*sqrt(3)/6,
                       start[1] + difference_vector_y/2 + difference_vector_x*sqrt(3)/6)

        snowflake_side(start, first_midpoint, iterations-1)
        # t.left(60)
        snowflake_side(first_midpoint, outer_point, iterations-1)
        # t.right(120)
        snowflake_side(outer_point, second_midpoint, iterations-1)
        # t.left(60)
        snowflake_side(second_midpoint, end, iterations-1)


def snowflake(start: Tuple[float, float], size: int, iterations: int) -> None:
    right_point = (start[0] + size, start[1])
    bottom_point = (start[0] + size/2, start[1]-size*sqrt(3)/2)

    t.penup()
    t.setposition(start)
    t.pendown()

    snowflake_side(start, right_point, iterations)
    # t.right(120)
    snowflake_side(right_point, bottom_point, iterations)
    # t.right(120)
    snowflake_side(bottom_point, start, iterations)


t.speed(0)
snowflake((-350, 200), 700, 6)
t.mainloop()
