import numbers
import math

class Polygon:
    def __init__(self, edges, circumradius):
        if isinstance(edges, numbers.Real) and isinstance(circumradius, numbers.Real):
            if edges < 3:
                raise TypeError("Polygon need at least 3 sides")
            else:
                self._edges = edges
                self._circumradius = circumradius
        else:
            raise TypeError("Edges and vertices must be real numbers")

    def __repr__(self):
        return f'Polygon(edges={self._edges}, circumradius={self._circumradius})'

    def __eq__(self, other):
        if isinstance(other, self.__clas__):
            return self._edges == other._edges and self._circumradius == other._circumradius
        else:
            return NotImplemented

    def __str__(self):
        return f'Polygon with {self._edges} edges and circumradius {self._circumradius}'

    def __gt__(self, other):
        return self.count_vertices > other.count_vertices

    @property
    def count_vertices(self):
        return self._edges

    @property
    def count_edges(self):
        return self._edges

    @property
    def interior_angle(self):
        return (self._edges - 2) * (180 / math.pi)

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def side_length(self):
        return 2 * self._circumradius * math.sin(math.pi / self._edges)

    @property
    def apothem(self):
        return self._circumradius * math.cos(math.pi / self._edges)

    @property
    def area(self):
        return self._edges / 2 * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._edges * self.side_length



class Polygons:
    def __init__ (self, m, R):
        if m < 3:
            raise ValueError("must have at least 3 edges")

        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m + 1)]

    def __len__(self):
        return self._m - 2

    def __rer__(self):
        return f'Polygons (m = {self._m,}, R = {self._R})'

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency(self):
        sorted_polygons = sorted(self._polygons,
                                key = lambda p: p.area / p.perimeter,
                                reverse = True)

        return sorted_polygons[0]

polygons = Polygons(10,1)
print(polygons.max_efficiency)









