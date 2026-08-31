import os
import shutil

sortedSomething = False

#sorting function
def sort(type, extension):
    os.chdir("C:/Users/ryend/Downloads")

    alreadyExists = False

    for file in os.listdir():
        if file == type:
            alreadyExists = True

    if alreadyExists == False:
        os.mkdir(type)

    for file in os.listdir():
        name, ext = os.path.splitext(file)
        if ext == extension:
            shutil.move(file, type)


#Ask to sort applications
while True:
    sortApplications = input("Sort Applications? y/n: ")

    if sortApplications == "y":
        sort("Applications", ".exe")
        sortedSomething = True
        break
    elif sortApplications == "n":
        break
    else:
        print("Invalid Input")

#Ask to sort images
while True: 
    sortImages = input("Sort Images? y/n ")

    if sortImages == "y":
        sort("Images", ".jpg")
        sortedSomething = True
        break
    elif sortImages == "n":
        break
    else:
        print("Invalid Input")


#Don't worry about this part 😈
if sortedSomething == False:
    while True:
        if input("You didn't sort anything, why did you run this? \nAre you an idiot? y/n: ") == "y":
            print("good boy")
            break
        else:
            print("Invalid Input")
else:
    nty = 0
    while True:
        if nty == 0:
            message = "All sorted \nAren't you going to say thank you?: "
        elif nty == 1:
            message = "Aren't you going to say thank you?"
        elif nty == 2:
            message = "AREN'T YOU GOING TO SAY THANK YOU?!" 
        elif nty == 3: 
            message = "I'M NOT ASKING ANYMORE!!!"
        else:
            message = ''
            count = 0
            while count < 100:
                message += 'SAY IT! '
                count += 1

        nty += 1

        if input(message) == "thank you":
            print("good boy")
            break
    