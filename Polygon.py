class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []

    def inputSides(self):
        for i in range(self.n):
            side = float(input(f"Enter the length of side {i + 1}: "))
            self.sides.append(side)

    def dispSides(self):
        for i in range(self.n):
            print(f"Length of side {i + 1} is {self.sides[i]}")

    def findArea(self):
        pass

    def calculatePerimeter(self):
        return sum(self.sides)


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides

        # Check for validity of triangle
        if a + b <= c or a + c <= b or b + c <= a:
            print("Invalid sides: Cannot form a triangle")
        else:
            s = self.calculatePerimeter() / 2  # semi-perimeter
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            print(f"The area of the triangle is {area:.2f}")


# Driver code
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
