__author__ = 'Anthony Lozano'
def center(points, epsilon=.1):
    """
    Given a set of points, this averages the circumcenters for each set of 3 unaligned points, which should result in a
    decent center estimation. Note this function is quite slow, running in O(n^3) time, however it produces decent
    results with just a few points.
    :param points: A list of points, a list [ (x0, y0), (x1, y1), ... (xn, yx)]
    :param epsilon: A floating point value, if abs(delta) between a set of three points is less than this value, the set will
        be considered aligned and be omitted from the fit.
    :return: the center of the circle, a tuple (x,y)
    :raise ValueError: If all the points lie on a line, a circumcenter for the points can not be calculated. In this
    case, you are looking at a line of points, not a circle. For our purposes this means the robot's steering value is ~0.
    """
    total_x = 0
    total_y = 0
    set_count = 0
    # Run algorithm 1 in "Finding the circle that best fits a set of points" (2007) by L Maisonbobe, found at
    # http://www.spaceroots.org/documents/circle/circle-fitting.pdf
    for i in points:
        for j in points[1:]:
            for k in points[2:]:
                delta = (k[0] - j[0]) * (j[1] - i[1]) - (j[0] - i[0]) * (k[1] - j[1])
                if abs(delta) > epsilon:
                    ii = i[0] ** 2 + i[1] ** 2
                    jj = j[0] ** 2 + j[1] ** 2
                    kk = k[0] ** 2 + k[1] ** 2
                    Cx = ( (k[1] - j[1]) * ii + (i[1] - k[1]) * jj + (j[1] - i[1]) * kk ) / (2 * delta)
                    Cy = -( (k[0] - j[0]) * ii + (i[0] - k[0]) * jj + (j[0] - i[0]) * kk ) / (2 * delta)
                    total_x += Cx
                    total_y += Cy
                    set_count += 1
    if set_count == 0:
        raise ValueError("all points are aligned")
    return (total_x / set_count), (total_y / set_count)

def radius(center, points):
    """
    This function estimates the radius of a circle given its center and a list of points by averaging the distance to
    center from each of those points
    :param center: The center of the circle, a tuple (x, y)
    :param points: A list of points, a list [ (x0, y0), (x1, y1), ... (xn, yx)]
    :return: The radius of the circle, a positive float or int
    """
    total = 0
    for point in points:
        total += distance_between(point, center)
    return abs(total / len(points))


def fit_circle(points, epsilon=.1):
    """
    Given a set of points, this averages the circumcenters for each set of 3 unaligned points, which should result in a
    decent center estimation, and then returns the center and radius of the circle. Note this function is quite slow,
    running in O(n^3) time, however it produces decent results with just a few points.
    :param points: A list of points, a list [ (x0, y0), (x1, y1), ... (xn, yx)]
    :param epsilon: A floating point value, if abs(delta) between a set of three points is less than this value, the set
        will be considered aligned and be omitted from the fit.
    :return: the center of the circle and the radius, a tuple ((x,y), R)
    :raise ValueError: If all the points lie on a line, a circumcenter for the points can not be calculated. In this
    case, you are looking at a line of points, not a circle. For our purposes this means the robot's steering value is ~0.
    """
    fitted_center = center(points, epsilon)
    return fitted_center, radius(fitted_center, points)