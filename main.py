from sort import dict_sort_by_last_name
from assign import assign_modules_to_hackathon_members
from top5 import top_five_students
from grade import grade_plot
from getData import getData

import matplotlib.pyplot as plt
import time
import pandas as pd

def main():
    data = getData()
    
    # Part A: Sort data by last name
    sort_time_start = time.perf_counter()
    data = dict_sort_by_last_name(data)
    sort_time_end = time.perf_counter()
    # Used perf_counter to measure performance as it has better accuracy than time.time()
    sort_time = sort_time_end - sort_time_start
    
    # print("Sorted data", data)
    
    # Part B
    assign_modules_to_hackathon_members(data)
    
    # Part C
    search_start = time.perf_counter()
    top_five_students(data, "CS4222")
    top_five_students(data, "CS4221")
    top_five_students(data, "CS4141")
    search_end = time.perf_counter()
    search_time = search_end - search_start
    
    # Part D
    x = ['Sort Time', 'Search Time(all modules']
    y = [sort_time, search_time]
    colours = [0, 10]
    plt.scatter(x, y, c=colours, cmap="viridis")
    plt.title('Time in seconds')
    plt.show()  # display plot
    
    # Part E
    df = pd.DataFrame({
    'Module': ["CS4222", "C4221", "CS4141"],
    'Leo': [70, 80, 90],
    'Daniel': [40, 50, 60],
    'Ilias': [10, 20, 30],
    'Sam': [100, 110, 120],
    })

    grade_plot(df)
    
if __name__ == "__main__":
    main()