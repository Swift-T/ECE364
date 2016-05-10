import os
import math
import operator
class PointND:

    def __init__(self, *args):
        self.n = len(args)
        self.t = args
        for item in self.t:
            if type(item ) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")
    def __str__(self):
        s = '(' + str('%.2f' %self.t[0])
        for i in range(1, len(self.t)):
            a = str('%.2f' %self.t[i])
            s += ', ' + a
        s += ')'
        return s

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if other.n != self.n:
             raise ValueError("Cannot calculate distance between points of different cardinality.")
        s = 0
        for i in range(0,self.n):
            s += (other.t[i] - self.t[i]) ** 2
        s = math.sqrt(s)
        return s

    def nearestPoint(self, points):
        if (len(points) == 0):
            raise ValueError("Input cannot be empty.")
        min = 100000000
        p = None
        for point in points:
            d = self.distanceFrom(point)
            if min > d:
                min = d
                p = point
        return p

    def clone(self):
        return PointND(*self.t)

    def __add__(self, other):
        if isinstance(other, PointND):
            if (self.n != other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
            point = PointND(*tuple(map(operator.add, other.t, self.t)))
            return point
        if isinstance(other, float):
            t = []
            for i in range(0, self.n):
                t.append(self.t[i] + other)
            point = PointND(*tuple(t))
            return point
    def __radd__(self, other):
        if isinstance(other, float):
            l = []
            for i in range(0, self.n):
                l.append(self.t[i] + other)
            point = PointND(*tuple(l))
            return point
    def __sub__(self, other):
         if isinstance(other, self.__class__):
            if (self.n != other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
            t=[]
            for i in range(0, other.n):
                t.append(-other.t[i] + self.t[i])
            point = PointND(*tuple(t))
            return point
         if isinstance(other, float):
            t = []
            for i in range(0, self.n):
                t.append(self.t[i] - other)
            point = PointND(*tuple(t))
            return point

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if (self.n != other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
            l=[]
            for i in range(0, other.n):
                l.append(other.t[i] * self.t[i])
            point = PointND(*tuple(l))
            return point
        if isinstance(other, float):
            l = []
            for i in range(0, self.n):
                l.append(self.t[i] * other)
            point = PointND(*tuple(l))
            return point
    def __rmul__(self, other):
        if isinstance(other, float):
            l = []
            for i in range(0, self.n):
                l.append(self.t[i] * other)
            point = PointND(*tuple(l))
            return point
    def __truediv__(self, other):
        if isinstance(other, float):
            t = []
            for i in range(0, self.n):
                t.append(self.t[i] / other)
            point = PointND(*tuple(t))
            return point

    def __neg__(self):
        return PointND(*tuple(map(operator.neg, self.t)))

    def __getitem__(self, item):
        return self.t[item]

    def __eq__(self, other):
        if (self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        if isinstance(other, self.__class__):
            if (self.n != other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
            for i in range(0, other.n):
                if other.t[i] is not self.t[i]:
                    return False
            return True

    def __ne__(self, other):
        if (self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        if isinstance(other, self.__class__):
            if (self.n != other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
            for i in range(0, other.n):
                if other.t[i] is self.t[i]:
                    return False
            return True

    def __gt__(self, other):
        if (self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        t = []
        for i in range(0,self.n):
            t.append(0.00)
        origin = PointND(*tuple(t))
        if(self.distanceFrom(origin) > other.distanceFrom(origin)):
            return True
        return False

    def __ge__(self, other):
        if (self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        t = []
        for i in range(0,self.n):
            t.append(0.00)
        origin = PointND(*tuple(t))
        if(self.distanceFrom(origin) >= other.distanceFrom(origin)):
            return True
        return False

    def __lt__(self, other):
        if (self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        t = []
        for i in range(0,self.n):
            t.append(0.00)
        origin = PointND(*tuple(t))
        if(self.distanceFrom(origin) < other.distanceFrom(origin)):
            return True
        return False

    def __le__(self, other):
        if (self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        t = []
        for i in range(0,self.n):
            t.append(0.00)
        origin = PointND(*tuple(t))
        if(self.distanceFrom(origin) <= other.distanceFrom(origin)):
            return True
        return False

class Point3D(PointND):
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        PointND.__init__(self,x,y,z)
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, o):
        if isinstance(o, Point3D):
            point = PointND(*tuple(map(operator.add, o.t, self.t)))
            return point
        if isinstance(o, PointND):
            if (self.n != o.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
        if isinstance(o, float):
            l = []
            for i in range(0, self.n):
                l.append(self.t[i] + o)
            point = PointND(*tuple(l))
            return point

    def __sub__(self, o):
        if isinstance(o, self.__class__):
            if (self.n != o.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
            l=[]
            for i in range(0, o.n):
                l.append(-o.t[i] + self.t[i])
            point = PointND(*tuple(l))
            return point
        if isinstance(o, PointND):
            if (self.n != o.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
        if isinstance(o, float):
            l = []
            for i in range(0, self.n):
                l.append(self.t[i] - o)
            point = PointND(*tuple(l))
            return point
class PointSet:
    def __init__(self, **kwargs):
        if kwargs == None:
            self.points = ()
            self.n = 0
        elif 'pointList' not in kwargs.keys():
            raise KeyError("'pointList' input parameter not found")
        else:
            self.points = set(kwargs['pointList'])
            if len(self.points) == 0:
                raise ValueError("'pointList' input parameter cannot be empty.")
            else:
                self.n = kwargs['pointList'][0].n
                for i in self.points:
                    if self.n != i.n:
                        raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
    def addPoint(self, p):
        if p.n == self.n:
            self.points.add(p)
        else:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))

    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        min=[]
        max=[]
        for i in range(0,self.n):
            min.append(100000000)
            max.append(0)
        for i in range(0,self.n):
            for point in list(self.points):
                    if min[i] > point.t[i]:
                        min[i] = point.t[i]
                    if max[i] < point.t[i]:
                        max[i] = point.t[i]
        return (PointND(*tuple(min)), PointND(*tuple(max)))

    def computeNearestNeighbors(self,otherPointSet):
        neig = []
        for point in self.points:
            nearest = point.nearestPoint(otherPointSet.points)
            neig.append(tuple([point,nearest]))
        return neig

    def __add__(self, other):
        if other.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        else:
            self.points.add(other)
            return self

    def __sub__(self,other):
        if other in self.points:
            self.points.remove(other)
        return self

    def __contains__(self, item):
        if item in self.points:
            return True
        else:
            return False
if __name__ == '__main__':
    pass
