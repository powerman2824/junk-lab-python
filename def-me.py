def print_points(name, age, total_points):
    print('{} is {}'.format(name, age))
    print('{} made {} points'.format(name, total_points))

user_name = 'May'
user_age = 23
regular_time_points = 26
overtime_points = 4

print_points(user_name, user_age, regular_time_points + overtime_points)