response = input("Gender: ")


# | (or) is used to combine several literals
match response:
    case "Male" | "male" | "M":
        gender = "male"
    case "Female" | "female" | "F":
        gender = "female"
    case _:
        gender = "others"

print(gender)
