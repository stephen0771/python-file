def calculate_surface_area(base,height):
    surface_area=1/2*base*height
    print(surface_area)

base=input("input base:")
height=input("input height:")
print("user entered base: ",base," and height: ",height,)
calculate_surface_area(int(base),int(height)*1/2)


def calculate_product_sum(number_1,number_2,number_3):
    product=number_1*number_2*number_3
    if product<=1000:
        print(product)
    else:
        print(number_1+number_2+number_3)




num_1=input("Input num 1:")
num_2=input("Input num 2:")
num_3=input("input num_3:")
print("User entered Number 1: ",num_1," and Number 2: ",num_2,"  and number 3: ",num_3)
calculate_product_sum(int(num_1),int(num_2),int(num_3))
breakpoint

def surface_area(base,height):
    surface_area=3/4*22/7*base*height
base=input("input base:")
height=input("input height:")
print("user entered base: ",base,"  and height: ",height)
calculate_surface_area(int(base),int(height)*3/4*22/7)
