##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
def count_simba(lines):
    count = 0
    for line in lines:
        count += line.count("Simba")
    return count

# Example usage:
example_lines = [
    "Simba and Nala are lions.",
    "I laugh in the face of danger.",
    "Hakuna matata",
    "Timon, Pumba and Simba are friends, but Simba could eat the other two."
]

print(count_simba(example_lines))  # Output: 3

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 
import pandas as pd

def get_day_month_year(date_list):
    data = {
        "day": [date.day for date in date_list],
        "month": [date.month for date in date_list],
        "year": [date.year for date in date_list]
    }
    return pd.DataFrame(data)

# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

from geopy.distance import geodesic

def compute_distance(coord_pairs):
    distances = []
    for pair in coord_pairs:
        point1, point2 = pair
        distance = geodesic(point1, point2).kilometers
        distances.append(distance)
    return distances

coords = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
print(compute_distance(coords))

#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#
def sum_general_int_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += sum_general_int_list(item)
    return total

list_1 = [[2], 3, [[1, 2], 5]]
print(sum_general_int_list(list_1))  # Output: 13

list_2 = [[2], 4, 5, [1, [2], [3, 5, [7, 8]], 10], 1]
print(sum_general_int_list(list_2))  # Output: 48