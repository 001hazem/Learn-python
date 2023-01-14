# total= int(input("Enter the Total :"))

# discount1 = int(input ("Enter the discount1 :"))
# discount2 = int(input ("Enter the discount2 :"))

# if total >100 and total < 200:
   
#     print(f"The {total} is greater than 100!")
#     Count_discount= total - discount1
#     print("The total is", Count_discount)

# elif total > 200:

#     print(f"The {total} is greater than 100!")
#     Count_discount= total - discount2
#     print("The total is", Count_discount)
    
# else:
#     print (f"the {total}is less than 100")


total_price =int(input("The total price is :"))
loyalty_customer = bool(input("???"))

if total_price > 100 and loyalty_customer == True:

    first_discount= total_price - (float(total_price)/ 100) * 20
    print(f"The customer gets the first discount {first_discount}")

elif total_price > 100 and loyalty_customer == False:

    second_discount= total_price - (float(total_price)/ 100) * 10
    print(f"The customer gets a second discount {second_discount}")

else:
    print('Sorry, no discount ...')


