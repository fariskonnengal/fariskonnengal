fruit_list = ["apple","banana","mango","orange"]
print("my favourite fruits are ",fruit_list)
print(f"my favourite fruits are {fruit_list}")

number_tuple = (1,2,3,7,10,21,33,50,99,100)
print(number_tuple)
print("my favourite numbers are ",number_tuple)

book_dict = {"Title":"IT END WITH US","Author":"Colleen Hoover","Year Published":2016}
print("my favourite book is ",book_dict)

# add an item into list
fruit_list.append("strawberry")
print("fruit list after adding an item",fruit_list)

# modify item in dictionary
book_dict ["Title"] = "Ugly love"
book_dict ["Year Published"] = 2014
print(book_dict)


# modify  number tuple
temp_list = list(number_tuple)
temp_list[6]=44
modified_tuple = tuple(temp_list)
print(modified_tuple)


