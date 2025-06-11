#promting user for a number 
number = int(input("enter a number to see its multiplication table: "))
#gererate and print the multiplication table

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}.")
