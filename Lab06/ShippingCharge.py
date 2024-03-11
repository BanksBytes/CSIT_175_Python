#!/user/bin/env python3

#Jordan Banks
#Palomar College CSIT 175
#Lab 6 Excercise 3, Calculate Shipping Charge Based on City Given

# Layout the list for cities and costs
zips   = [91901,91976,92020,92040,92065,92069,92071]
cities = ["Alpine", "Spring Valley", "El Cajon", "Lakeside", "Ramona", "San Marcos", "Santee"]
express_shipping = [5.00, 10.00, 8.00, 7.00, 6.00, 8.00, 7.00] 
groound_shipping = [3.00, 5.00, 5.00, 4.00, 3.00, 5.00, 4.00]

# WIll come back to define this later
zip_code = 0
shipping_method = 0
city = "Not Found"
found = False
i = 0
list_len = len(zips)

# Get Zip Code and Shipping method
zip_code = int(input("Enter Zip Code: "))
