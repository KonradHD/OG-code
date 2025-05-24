import math
import numpy as np

class intersectionAnalyzer():
    def __init__(self):
        self.coefficient_matrix = {}
        self.coefficient_matrix["line"] = []
        self.coefficient_matrix["circle"] = []
        self.intersection_counter = {}
        self.intersections_limit = 10


    def save_line_coeffictients(self, X0, Y0, X1, Y1):
        A = Y1 - Y0
        B = X0 - X1
        C = X1 * Y0 - X0 * Y1
        coeffictients = [round(A, 2), round(B, 2), round(C, 2)]
        self.count_intersections(coeffictients, "line")
        self.coefficient_matrix["line"].append(coeffictients)


    def save_circle_coefficients(self, x0, y0, r):
        coeffictients = [round(x0, 2), round(y0, 2), round(r, 2)]
        self.count_intersections(coeffictients, "circle")
        self.coefficient_matrix["circle"].append(coeffictients)


    def set_intersection_limit(self, intersection_limit):
        self.intersections_limit = intersection_limit
    

    def next_surface(self):
        self.coefficient_matrix["line"].clear()
        self.coefficient_matrix["circle"].clear()
        self.intersection_counter.clear()


    def solve_linear_equasion(self, coef1, coef2):
        A1, B1, C1 = coef1
        A2, B2, C2 = coef2

        # Sprawdzenie czy linie są tożsame (wszystkie współczynniki proporcjonalne)
        if A1 * B2 == A2 * B1 and A1 * C2 == A2 * C1 and B1 * C2 == B2 * C1:
            raise Exception("Lines cannot overlap each other in the same surface.")
        A = np.array([
            [A1, B1],
            [A2, B2]
        ])
        B = np.array([
            -C1,
            -C2
        ])
        try:
            wynik = np.linalg.solve(A, B)
            return [(round(float(wynik[0]), 2), round(float(wynik[1]), 2))]
        except np.linalg.LinAlgError:
            return []
    

    def solve_linear_circle(self, line_coef, circle_coef):
        A, B, C = line_coef
        h, k, R = circle_coef

        points = []

        if B != 0:
            # y = (-Ax - C)/B i podstawienie do równania okręgu
            def y(x): return (-A * x - C) / B
            # Równanie: (x - h)^2 + (y(x) - k)^2 = r^2
            a = A**2 / B**2 + 1
            b = 2 * (A * C / B**2 + A * k / B - h)
            c = (C**2 / B**2 + 2 * C * k / B + k**2 + h**2 - R**2)

            discriminant = b**2 - 4 * a * c
            if discriminant < 0:
                return []  # Brak punktów wspólnych
            elif discriminant == 0:
                x = -b / (2 * a)
                points.append((round(x, 2), round(y(x), 2)))
            else:
                sqrt_disc = math.sqrt(discriminant)
                x1 = (-b + sqrt_disc) / (2 * a)
                x2 = (-b - sqrt_disc) / (2 * a)
                points.append((round(x1, 2), round(y(x1), 2)))
                points.append((round(x2, 2), round(y(x2), 2)))
        else:
            # Prosta pionowa: x = const = -C / A
            x = -C / A
            D = R**2 - (x - h)**2
            if D < 0:
                return []  # Brak punktów wspólnych
            elif D == 0:
                y = k
                points.append((round(x, 2), round(y, 2)))
            else:
                sqrt_D = math.sqrt(D)
                y1 = k + sqrt_D
                y2 = k - sqrt_D
                points.append((round(x, 2), round(y1, 2)))
                points.append((round(x, 2), round(y2, 2)))

        return points


    def solve_two_circle(self, coef1, coef2):
        if coef1 == coef2:
            raise Exception("Circles cannot overlap each other in the same surface.")
    
        x1, y1, r1 = coef1
        x2, y2, r2 = coef2

        dx = x2 - x1
        dy = y2 - y1
        d = math.hypot(dx, dy)

        # Brak punktów wspólnych
        if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
            return []

        # Punkt przecięcia środkowy między przecięciami
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = math.sqrt(r1**2 - a**2)

        # Punkt P2 (środek przecięcia)
        x3 = x1 + a * dx / d
        y3 = y1 + a * dy / d

        # Punkty przecięcia
        rx = -dy * (h / d)
        ry = dx * (h / d)

        point1 = (round(x3 + rx, 2), round(y3 + ry, 2))
        point2 = (round(x3 - rx, 2), round(y3 - ry, 2))

        if point1 == point2:
            return [point1]  # styczne
        else:
            return [point1, point2]


    def add_point(self, point):
        if self.intersection_counter.get(point) is not None:
            self.intersection_counter[point] += 1
        else: 
            self.intersection_counter[point] = 1


    def count_intersections(self, coef2, type):
        points = []
        for coef1 in self.coefficient_matrix["line"]:
            if type == "line":
                points = self.solve_linear_equasion(coef1, coef2)
                for point in points:
                    self.add_point(point)
            elif type == "circle":
                points = self.solve_linear_circle(coef1, coef2)
                for point in points:
                    self.add_point(point)
            points = []
        for coef1 in self.coefficient_matrix["circle"]:
            if type == "line":
                points = self.solve_linear_circle(coef2, coef1)
                for point in points:
                    self.add_point(point)
            if type == "circle":
                points = self.solve_two_circle(coef1, coef2)
                for point in points:
                    self.add_point(point)
            points = []

        for value in self.intersection_counter.values():
            if value >= self.intersections_limit:
                raise Exception("Too many intersections.")