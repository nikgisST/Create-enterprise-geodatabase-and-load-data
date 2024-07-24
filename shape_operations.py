import itertools
import math

import arcpy


def polygon_to_line(polygon: arcpy.Polygon) -> arcpy.Polyline:
    """Creates a line between the vertices in the polygon that are farthest apart"""
    # Extract all vertices from the polygon and find the 4 points with min/max X/Y.
    vertices = tuple(itertools.chain.from_iterable(polygon.getPart()))
    a = max(vertices, key=lambda p: p.X)
    b = max(vertices, key=lambda p: p.Y)
    c = min(vertices, key=lambda p: p.X)
    d = min(vertices, key=lambda p: p.Y)

    # Find the pair of points that are farthest apart.
    lengths = {}
    # a b c d are not always going to be different points, so we only need to visit the set.
    for start, end in itertools.combinations({a, b, c, d}, r=2):
        length = math.hypot(start.X - end.X, start.Y - end.Y)
        lengths[length] = (start, end)

    # inputs, spatial_reference, has_z, has_m
    return arcpy.Polyline(
        arcpy.Array(lengths[max(lengths)]), polygon.spatialReference, a.Z is not None, a.M is not None
    )


def buffer(shape: arcpy.Geometry, distance: float) -> arcpy.Polygon:
    """Buffers shape by specified distance"""
    return shape.buffer(distance)


def shift_point_coordinate(
    point: arcpy.PointGeometry, x: float = 0, y: float = 0, z: float = 0, m: float = 0
) -> arcpy.PointGeometry:
    """Shifts the X,Y,Z,M coordinates of a point by a constant value."""

    first_point = point.firstPoint
    if x:
        first_point.X += x
    if y:
        first_point.Y += y
    # Z and M can be None, ensure they have a value
    if z and first_point.Z is not None:
        first_point.Z += z
    if m and first_point.M is not None:
        first_point.M += m

    # inputs, spatial_reference, has_z, has_m
    return arcpy.PointGeometry(
        first_point, point.spatialReference, first_point.Z is not None, first_point.M is not None
    )
