example_list = [10, 20, 35, 45, 50, 60, 75, 80, 90, 100]
def slice_list(list):
    start_index = int(input("enter start index"))
    end_index = int(input("enter end index"))
    sliced_list = list[start_index:end_index]
    print("sliced list is ",sliced_list)
slice_list(example_list)