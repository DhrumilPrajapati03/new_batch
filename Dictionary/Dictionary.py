# dict = {"key1": "value1", "key2": "value2"}

dict = {"name": "Alice", 
        "age": 30, 
        "city": "New York",
        2 : ["reading", "traveling", "cooking"],
        "is_student": False,
        "address": {"street": "123 Main St", "zip": "10001"},
        "phone_numbers": ("123-456-7890", "987-654-3210")}

update_dict = {"age": 31, "city": "Los Angeles", "country": "USA"}
update_dict.update(dict)
print(update_dict)

print(dict["name"])  # Output: Alice
print(dict.get("age"))  # Output: 30
print(dict.keys(),"\n")
print(dict.values(),"\n")
print(dict.items(),"\n")
print(type(dict))