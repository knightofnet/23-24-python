class Point :

    def __init__(self,nom,x, y):
        self.x = x
        self.y = y
        self.nom = nom

    def __str__(self):
        return f"Point {self.nom} : x = {self.x}, y = {self.y}"
    
    def __eq__(self, obj) :
        return self.x == obj.x and self.y == obj.y

    def __add__(self, o) :
        nvoX = self.x + o.x
        nvoY = self.y + o.y
        nvoNom = f"{self.nom} + {o.nom}"
        return Point(nvoNom, nvoX, nvoY)

p1 = Point("p1", 2, 5)
p2 = Point("p2", 2, 5)
p3 = p1 + p2
print(p1 == p2)
print(p3)

print(p1.x, p1.nom)