#Que 3

def convert_to_centimeters(height_inches):
    return height_inches * 2.54
while True:
    try:
        num_customers = int(input("Enter the number of customers: "))
        if num_customers <= 0:
            raise ValueError("Invalid.")
        break
    except ValueError as error_msg:
        print(f"Error: {error}")
heights_inches = []
for i in range(num_customers):
    while True:
        try:
            customers_height = float(input(f"Enter height in inches for customers {i + 1}: "))
            if customers_height <= 0:
                raise ValueError("Invalid.")
            heights_inches.append(customers_height)
            break
        except ValueError as error_msg:
            print(f"Error: {error}")
heights_centimeters = [convert_to_centimeters(height) for height in heights_inches]
average_height_inches = sum(heights_inches) / num_customers
average_height_centimeters = sum(heights_centimeters) / num_customers
print("\nHeights in inches)ches:", heights_inches)
print("Heights in centimeters:", heights_centimeters)
print(f"\nAverage Height (in inches): {average_height_inches:.2f} inches")
print(f"Average Height (in centimeters): {average_height_centimeters:.2f} cm")


customer_heights_inches = []

while True:
    try:
        num_of_customers = int(input("Enter the number of customers: "))
        if num_of_customers > 0:
            break
        else:
            print("Invalid.")
    except ValueError:
        print("Invalid.")

for i in range(1, num_of_customers + 1):
    while True:
        try:
            height_inches = float(input("Enter height in inches for customer {}: ".format(i)))
            customer_heights_inches.append(height_inches)
            break
        except ValueError:
            print("Invalid.")

heights_in_centimeters = [height * 2.54 for height in customer_heights_inches]

print("Heights in centimeters:", heights_in_centimeters)
