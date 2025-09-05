def find_duplicates(l: list) -> list:
    tracker = {}
    new_list = []

    for num in l:
        if num in tracker:
            tracker [num] += 1
        else: 
            tracker[num] = 1

    for num, count in tracker.items():
        if count > 1:
            new_list.append(num)
    print(f"Found these duplicates {new_list}")
    return new_list

# In Python, if __name__ == "__main__" is a conditional check that determines whether 
# a Python file is being run as the main program or imported as a module into another 
# script.
if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]
    
    print("Sample 1:", find_duplicates(sample1))
    print("Sample 2:", find_duplicates(sample2))
    print("Sample 3:", find_duplicates(sample3))
    print("Sample 4:", find_duplicates(sample4))


    # pseudo code 
    # we want to return a new list that only contains duplicates
    # make a new empty list
    # new_list = [] (python)
    # new_list.append(5) (python)
    # ya gotta loop through the list ....
    # for num in my_list: 
    # print(num)
    # there's a duplicate, add it to the empty list
    # after you're done iwht the looping, return the list
    # return new list
    # make a dictionary in python
    # tracker = {}
    # for num in my)list: 
    # tracker [num] = 0
    # return new list
    # return null;
