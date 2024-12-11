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

    def markPercentage():
        markList = []
        for i in range(5):
            mark = int(input(f"Enter the mark of subject {i + 1}: "))
            markList.append(mark)
            
        for mr in markList:
            numberSum = sum(markList)
            avg = numberSum/len(markList)
        print("Total:", numberSum)
        print("Percentage:", avg)

    def aiSubList():
        aiSubList = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for sub in aiSubList:
            print(sub)