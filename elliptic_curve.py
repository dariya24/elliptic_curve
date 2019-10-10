class EllipticCurve:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class PointOnEllipticCurve:
    def __init__(self, x, y, curve):
        if round(y**2, 3) != round(x**3 + curve.a * x + curve.b, 3):
            raise ValueError('This point is not on the curve')
        self.x = x
        self.y = y
        self.curve = curve

    def __type__(self):
        if self.y == None:
            return 'point of infinity'
        else:
            return 'point of elliptic curve'

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def add(self, point):

        if self.x != point.x and self.y != point.y:
            s = (self.y - point.y) / (self.x - point.x) # this is slope of the line
            x = s**2 - (self.x + point.x)
            y = s*(self.x - point.x) - self.y

        if self.x == point.x and self.y == point.y:
            s = (3*self.x**2 + self.curve.a) / 2*self.y
            x = s**2 - 2*self.x
            y = s*(self.x - point.x) - self.y

        if self.x == point.x or self.x == 0:
            x = 0
            y = None

        return PointOnEllipticCurve(x, y)

    def multiplication(self, k, curve):
        for i in range(k):
            return self.add(self, self, curve)
