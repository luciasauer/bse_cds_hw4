##### Try to use map and reduce in the next 3 exercises
from functools import reduce
import pandas as pd
from datetime import date
from geopy.distance import geodesic

# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

#Using the reduce function
def count_simba(string_list: list) -> int:
    return reduce(lambda count, s: count + s.lower().count("simba"), string_list, 0)

#Not using the reduce function (simpler and easier)
# def count_simba(string_list: list) -> int:
#     return sum([s.lower().count("simba") for s in string_list])

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.

def get_day_month_year(values: list) -> pd.DataFrame:
    results = list(map(lambda value: (value.day, value.month, value.year), values))
    return pd.DataFrame(results, columns=["day", "month", "year"])


# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance


def compute_distance(coords_list: list) -> list:
    return list(map(lambda coord: geodesic(coord[0], coord[1]).kilometers, coords_list))
 

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

def sum_general_int_list(nested_list) -> int:
    return sum(map(lambda x: sum_general_int_list(x) if isinstance(x, list) else x, nested_list))
