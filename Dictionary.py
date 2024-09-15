dictionary ={
    "sun" : "the star that shines in the sky during the day",
    "moon": "the round object that moves around the earth",
    "deborah" : "bee"
}


print(dictionary)


print(dictionary["deborah"])
print(dictionary["sun"])


phonebook = {
    "Akash" : "9566089884",
    "Deborah" : "08077366677",
    "Bello": "08055144455"

}



print(phonebook)


print(phonebook["Akash"])
print(phonebook["Deborah"])
print(phonebook["Bello"])


dict = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
}

dict["key1"] = "value-------1"

print(dict)

dict["key4"] = "value4"
print(dict)

for key, value in dict.items():
    print("the key is",key,"the value is", value)

