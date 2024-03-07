shadows = ["alpha", "beta", "delta", "gamma", "epsilon", "zeta", "eta"]

for shadow in shadows:

    # len(shadow) gives the length of the string contained by the 'shadow' variable
    if len(shadow) > 5:
        print(shadow)


colors = ["black", "pink", "white", "brown"]

for color in colors:

    # 'break' stops the execution of the current loop
    if color == "white":
        break

    print(color)
