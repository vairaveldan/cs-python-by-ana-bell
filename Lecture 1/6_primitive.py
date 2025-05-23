print("""
      1) Move Left
      2) Move Right
      3) Print (Write)
      4) Scan (Read)
      5) Erase (Delete)
      6) No operation (Exit from the loop)
      """)
data =[0,1,2,3,4,5]
index = 0
while (True) :
    choice = int(input("Enter your choice: "))
    match choice :
        case 1 :
            if index == 0 : 
                print("I am at zero index")
            else :
                index -= 1
        case 2 :
            if index == len(data) - 1 :
                print("I am at last index")
            else :
                index += 1
        case 3 :
            data[index] = int(input("enter a integer to Write in the Data :"))
        case 4:
            print(data[index])
        case 5 :
            data.remove(data[index])
        case 6 :
            print("Exit from the loop")
            break
        case _:
            print("Invalid choice")
print("final data: ",data)