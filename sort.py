
def dict_sort_by_last_name(dict):
    # Time complexity is O(n log n) because the sort() function uses TimSort
    # lambda can be used to initialise anonymous functions which are just functions without a name
    dict.sort(key=lambda x: x['Last Name'])

    return dict