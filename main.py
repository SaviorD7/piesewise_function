



class PieseWiseFunction():
    def __init__(self):
        self.points_list = []


    def add_points(self, *points):
        if len(points) % 2 != 0:
            print('Number of points must be even')
            return
        for i in range(0, int(len(points))-1, 2):
            if not self.check_existence(points[i], points[i+1]):
                 self.points_list.append(list(points[i:i+2]))
        return self.points_list

    def check_existence(self, point_x: int, point_y: int):
        for point in self.points_list:
            if point_x == point[0]:
               self.points_list[self.points_list.index(point)] = [point_x, point_y]
            if point_x < self.points_list[-1][0]:
                print('Skip point with X less then last X')
                return True
        return False

    def find_coeffs(self, point_x1: int, point_y1: int, point_x2: int, point_y2: int):
        k = (point_y1 - point_y2) / (point_x1 - point_x2)
        b = point_y2 - k*point_x2
        return k, b


    def find_interval(self, point_x: int):
        for point in self.points_list:
            try:
                if point_x >= point[0] and point_x <= self.points_list[self.points_list.index(point)+1][0]:
                    return point[0], point[1], \
                        self.points_list[self.points_list.index(point)+1][0],  \
                        self.points_list[self.points_list.index(point)+1][1]
            except:
                print('No interval found!')
                return None


    def find_value(self, point_x: int):
        try:
            x1, y1, x2, y2 = self.find_interval(point_x)
            k, b = self.find_coeffs(x1, y1, x2, y2)
            y = k*point_x + b
            return round(y, 1)
        except:
            print('Something went wrong!')

    def print_table(self):
        print('-' * 20)
        print('| x1  | x2     | k      | b    |')
        for i in range(len(self.points_list) - 1):
            k, b = self.find_coeffs(self.points_list[i][0],self.points_list[i][1], self.points_list[i+1][0], self.points_list[i+1][1])
            print('|',self.points_list[i][0] ,'  | ', self.points_list[i+1][0], '  |',round(k, 2) ,'   |', round(b,2), '|')

        


a = PieseWiseFunction()
a.add_points(0,100,10,12,20,23,30,45,40,80,50,1)
print(a.find_value(33))
a.print_table()