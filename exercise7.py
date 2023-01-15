bill= float(input("Enter Bill ?"))
tax_rate= float(input("Enter tax rate ?"))


def total_tex(bill , tax_rate):
     
    return(bill * tax_rate) / 100.00

print("Total tax" , total_tex(bill , tax_rate))


my_gloable=10

def Function1():
    global my_local 
    my_local=7
    print("the gloable Number ", my_gloable)

Function1()

print("the Local Number is", my_local)
