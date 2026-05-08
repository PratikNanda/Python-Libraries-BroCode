import numpy as np

# Filtering = Refers to the process of selecting elements from an array that match a given condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages [ages < 18]
    # output
    # [17 16 15]

# adults = ages [(ages >= 18) & (ages < 65)]
    # output
    # [21 19 20 30 18 39 22 18 19 20 21]

seniors = ages [ages >= 65]
    # output
    # [65 99]

evens = ages [ages % 2 == 0]
    # output
    # [20 16 30 18 22 18 20]

odds = ages [ages %2!=0]
    # output
    # [21 17 19 65 39 15 99 19 21]

# print("# output",f"# {odds}", sep="\n")    

# -------------------Using Where function

adults = np.where(ages >= 18, ages, 0)
    # output
    # [[21  0 19 20  0 30 18 65]
    #  [39 22  0 99 18 19 20 21]]

adults = np.where(ages >= 18, ages, np.nan)
    # output
    # [[21. nan 19. 20. nan 30. 18. 65.]
    #  [39. 22. nan 99. 18. 19. 20. 21.]]

print(adults)

