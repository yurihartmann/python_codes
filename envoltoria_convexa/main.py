class Point:
    name: str
    x: int
    y: int

    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def __str__(self):
        return f"Point({self.name}, x={self.x}, y={self.y})"


LIST_OF_POINT = [
    Point("p1", x=3, y=6),
    Point("p2", x=0, y=5),
    Point("p3", x=3, y=3),
    Point("p4", x=1, y=1),
    Point("p5", x=3, y=2),
    Point("p6", x=3, y=4),
    Point("p7", x=5, y=2),
    Point("p8", x=6, y=5),
    Point("p9", x=4, y=4),
    # Point("p10", x=10, y=9),
    # Point("p11", x=11, y=3)
]

LIST_OF_POINT = sorted(LIST_OF_POINT, key=Point.get_x)


def print_list_of_points(list_of_point: list):
    print("[" + ",".join([str(point) for point in list_of_point]) + "]")


def CCW(p1: Point, p2: Point, p3: Point) -> bool:
    value = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    if value < 0.000001:
        return True

    return False


L_SUP = [LIST_OF_POINT[0], LIST_OF_POINT[1]]

for i in range(2, len(LIST_OF_POINT)):
    L_SUP.append(LIST_OF_POINT[i])

    while len(L_SUP) > 2 and CCW(L_SUP[-3], L_SUP[-2], L_SUP[-1]):
        L_SUP.pop(len(L_SUP) - 2)


L_INF = [LIST_OF_POINT[-1], LIST_OF_POINT[-2]]

for i in reversed(range(0, len(LIST_OF_POINT) - 2)):
    L_INF.append(LIST_OF_POINT[i])

    while len(L_INF) > 2 and CCW(L_INF[-3], L_INF[-2], L_INF[-1]):
        L_INF.pop(len(L_INF) - 2)


L_SUP.pop(-1)
L_INF.pop(-1)

ENVOLTORIA_CONVEXA = L_SUP + L_INF
print("ENVOLTÓRIA CONVEXA: ")
print_list_of_points(ENVOLTORIA_CONVEXA)
