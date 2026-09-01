import os
import shutil

sorted_something = False

#sorting function
def sort(type, extension):
    os.chdir("C:/Users/ryend/Downloads")

    already_exists = False

    for file in os.listdir():
        if file == type:
            already_exists = True

    if already_exists == False:
        os.mkdir(type)

    for file in os.listdir():
        name, ext = os.path.splitext(file)
        if ext == extension:
            shutil.move(file, type)



#Ask to sort applications
def ask_if_sort(type, extenstion):
    global sorted_something
    while True:
        sort_type = input(f"Sort {type}? y/n: ")

        if sort_type == "y":
            sorted_something = True
            sort(type, extenstion)
            break
        elif sort_type == "n":
            break
        else:
            print("Invalid Input")


ask_if_sort('Images', '.jpg')
ask_if_sort('Applications' '.exe')
ask_if_sort('Documents' '.pdf')


#Don't worry about this part 😈
if sorted_something == False:
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

        if input(message).upper() == "THANK YOU":
            print("good boy")
            break
    
