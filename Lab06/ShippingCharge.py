#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 6 Excercise 3, Calculate Shipping Charge Based on City Given

# Layout the list for cities and costs
zips   = [91901,91976,92020,92040,92065,92069,92071]
cities = ["Alpine", "Spring Valley", "El Cajon", "Lakeside", "Ramona", "San Marcos", "Santee"]
express = [5.00, 10.00, 8.00, 7.00, 6.00, 8.00, 7.00] 
ground = [3.00, 5.00, 5.00, 4.00, 3.00, 5.00, 4.00]

# Variables needed
zip_code = 0
city = "Not Found"
ship_cost = 0
found = False
i = 0
list_len_zip = len(zips)

# Get Zip Code and Shipping method
zip_code = int(input("Enter Zip Code: "))
shipping_method = input("Enter the shipment method you would like, Ground or Express: ")



# search the array
while i < list_len_zip and not found:  # don't forget the colon (:) on a loop condition
    # test for a ZIP code match and indent the if(True) block
    if zip_code == zips[i] and shipping_method == "Ground": # Don't forget the colon (:) on the if block
        # found a match for zip code and ground shipping !
        city = cities[i]
        ship_cost = ground[i]
        found = True
    elif zip_code == zips[i] and shipping_method == "Express":
        # found a match for zip code and express shipping !
        city = cities[i]
        ship_cost = express[i]
        found = True
    
    i = i + 1 # be sure to increment the loop counter




# output
print(f"The ZIP code is {zip_code}")
print(f"The City is {city}")
print(f"The shipping cost is ${ship_cost:.2f}")