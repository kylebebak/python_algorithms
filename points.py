class Segment:
    """Line segment."""

    def __init__(self, a, b):
        self.a = a
        self.b = b
        return self

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b


class Point:
    """A point in 2d space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def intersect_segments(U, V):
    return ccw(U.a, V.a, V.b) != ccw(U.b, V.a, V.b) and ccw(U.a, U.b, V.a) != ccw(
        U.a, U.b, V.b
    )
