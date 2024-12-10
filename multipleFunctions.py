class multipleFunctions():
    def oddEven():
        num = int(input("Enter any number:"))
        if (num%2 == 0):
            print("The given number", num, "Even")
        else:
            print("The given number", num, "Odd")

    def triangle():
        height = int(input("Enter the Height:"))
        breadth = int(input("Enter the Breadth:"))
        print('Area formula: (Height*Breadth)/2')
        area = (height*breadth)/2
        print('Area of Triangle:', area)

        height1 = int(input("Enter the Height1:"))
        height2 = int(input("Enter the Height2:"))
        breadth = int(input("Enter the Breadth:"))
        print('Perimeter formula: Height1+Height2+Breadth')
        perimeter = height1 + height2 + breadth
        print('Perimeter of Triangle:', perimeter)

    def elegible():
        gender = input("Enter your gender")
        age = int(input("Enter your age"))
        if (((gender == 'male') and (age >= 21)) or ((gender == 'female') and (age >= 18))):
            print('Eligible')
        else:
            print('Not Eligible')