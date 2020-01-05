__author__ = "Michael E Miles"

fruit = {"orange": "A sweet, orange, citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yello citrus fruit",
         "grape": "A small, sweet fruit growing in bunches",
         "lime": "A sour, green citrus fruit"}
# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "An odd shaped apple"
# print(fruit)
# fruit["lime"] = "Great with tequila"
# print(fruit)
# # del fruit["lemon"]
# # fruit.clear()
# # print(fruit)
# print(fruit["tomato"]
print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)
