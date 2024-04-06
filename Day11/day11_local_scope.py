def reverse(s):

    r = s[::-1]

    # 'r' is a local variable since
    # it is defined within the scope of this function
    print(r)


reverse("django")

# This will raise an Exception because 'r' is not defined in this scope
print(r)
