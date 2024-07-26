import math  # Importieren der math-Bibliothek
import random  # Importieren der random-Bibliothek

# Eine Konstante
PI = math.pi

# Funktion zur Berechnung der Fläche eines Kreises
def circle_area(radius):
    """Berechnet die Fläche eines Kreises mit gegebenem Radius."""
    if radius <= 0:
        raise ValueError("Radius muss positiv sein.")
    return PI * (radius ** 2)


# Klasse für einen einfachen Punkt
class Point:
    def __init__(self, x, y):
        """Initialisiert einen Punkt mit x- und y-Koordinaten."""
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        """Berechnet die Distanz zu einem anderen Punkt."""
        if not isinstance(other_point, Point):
            raise TypeError("Der andere Punkt muss ein Point-Objekt sein.")
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def __str__(self):
        """Gibt eine lesbare Darstellung des Punktes zurück."""
        return f"Point({self.x}, {self.y})"

# Hauptteil des Programms
def main():
    try:
        # Erstellen von Punkten
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        
        # Berechnen und Ausgeben der Distanz zwischen den Punkten
        distance = p1.distance_to(p2)
        print(f"Distanz zwischen {p1} und {p2} ist {distance:.2f}")

        # Berechnung und Ausgabe der Fläche eines Kreises
        radius = 5
        area = circle_area(radius)
        print(f"Die Fläche eines Kreises mit Radius {radius} ist {area:.2f}")

        # Berechnung und Ausgabe der Quadratwurzel
        value = 16
        sqrt_value = sqrt(value)
        print(f"Die Quadratwurzel von {value} ist {sqrt_value:.2f}")

        # Zufällige Ganzzahl zwischen 1 und 10
        rand_int = random.randint(1, 10)
        print(f"Zufällige Ganzzahl zwischen 1 und 10: {rand_int}")

    except (ValueError, TypeError) as e:
        print(f"Fehler: {e}")

# Ausführen des Hauptteils des Programms
if __name__ == "__main__":
    main()
