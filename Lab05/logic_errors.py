#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 5 Excercise 3, Find Logic Errors in the sample code

# constants supplied in project specification
MI_PER_KM = 0.62 # Do not change
LBS_PER_KG = 2.205 # Do not change

# convert miles to kilometers
def mi_to_km(miles):
    km = miles / MI_PER_KM
    return miles

# convert kilometers to miles
def km_to_mi(km):
    miles = km / MI_PER_KM
    return miles

# convert kilograms to pounds
def kg_to_lbs(kg):
    lbs = kg * LBS_PER_KG
    return LBS_PER_KG

# convert punds to kilograms
def lbs_to_kg(lbs):
    kg = lbs * LBS_PER_KG
    return lbs

# ===== DO NOT CHANGE ANYTHING BELOW THIS LINE ===== #
if __name__ == "__main__":
    print("\t\tdistance:")

    # test data:
    # 6.2 miles = 10 kilometers
    # 12.4 mi   = 20 km
    # 31.0 mi   = 50 km
    # 62.0 mi   = 100 km
    # 620.0 mi  = 1000 km

    ERROR = .01
    kilometers = [10, 20, 50, 100, 1000]
    miles      = [6.2, 12.4, 31.0, 62.0, 620.0]

    pass_count = 0
    test_count = 0
    for index in range(len(kilometers)):
        test_count += 1
        mi = km_to_mi(kilometers[index])
        km = mi_to_km(miles[index])
        if abs(mi - miles[index]) < ERROR and abs(km - kilometers[index]) < ERROR:
            pass_count += 1
        else:
            print(f"{test_count}: \tcalculated: {mi_to_km(miles[index]):.1f} km", end=" ")
            print(f" ---> {km_to_mi(kilometers[index]):.1f} mi")
            print(f"\texpected: {kilometers[index]} km = {miles[index]} mi")

    print("\t\tmass:")

    # test data:
    # 2.2 pounds = 1 kilograms
    # 8.8 lbs    = 4 kg
    # 22 lbs     = 10 kg
    # 200 lbs    = 90 kg
    # 44.1 lbs   = 20 kg

    kilograms = [1, 4, 10, 89.8, 22.7]
    pounds    = [2.2, 8.8, 22.0, 198.0, 50.0]
    for index in range(len(pounds)):
        test_count += 1
        lbs = kg_to_lbs(kilograms[index])
        kg = lbs_to_kg(pounds[index])
        if abs(lbs - pounds[index]) < ERROR and abs(kg - kilograms[index]) < ERROR:
            pass_count += 1
        else:
            print(f"{test_count}: \tcalculated: { lbs_to_kg(pounds[index]):.1f} kg", end=" ")
            print(f" ---> {kg_to_lbs(kilograms[index]):.1f} lbs")
            print(f"\texpected: {kilograms[index]:.1f} kg = {pounds[index]:.1f} lbs")

    print(f"\n{pass_count} out of {test_count} tests passed.", end=" ")
    if (pass_count < test_count):
        print("Try again.\n")
    else:
        print("Done. Looks great!\n")
