import time

from Complex import Complex

def prompt_number(option = ""):
    real_part_one = int(input("Please input the real part of the first complex number... "))
    img_part_one = int(input("Please input the imaginary part of the first complex number... "))
    c1 = Complex(real_part_one, img_part_one)

    if len(option) == 0:
        real_part_two = int(input("Please input the real part of the second complex number... "))
        img_part_two = int(input("Please input the imaginary part of the second complex number... "))
        c2 = Complex(real_part_two, img_part_two)
        return [c1, c2]

    return c1


if __name__ == "__main__":
    while True:
        print("========================COMPLEX NUMBER CALCULATOR==================")
        print("------->1.Add")
        print("------->2.Substract")
        print("------->3.Multiply")
        print("------->4.Conjugate")
        print("------->5.Modulus")
        print("------->6.Exit")
        option = input("------->Choose an option:")
        if option == "1":
            c1, c2 = prompt_number()
            print(f'The result is: {c1 + c2}')
        elif option == "2":
            c1, c2 = prompt_number()
            print(f'The result is: {c1 - c2}')
        elif option == "3":
            c1, c2 = prompt_number()
            print(f'The result is: {c1 * c2}')
        elif option == "4":
            c1 = prompt_number("restrict")
            print(f'The result is: {c1.calculate_conjugate()}')
        elif option == "5":
            c1 = prompt_number("restrict")
            print("The result is: " + "{:.2f}".format(c1.calculate_modulus()))
        elif option == "6":
            break
        else: 
            print(">>>>>>>>>>>ERROR: Option introduced does not exist. Please insert a valid option <<<<<<<<<<<<<<<")
            time.sleep(1.5)