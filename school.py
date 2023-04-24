condition=True
while(condition):
    student_info = input("enter student information following format(Name age ocntact_number E-mail.ID:")
    print("entered information:"+student_info)
condition_check = input("enter (yes/no) if u want to enter for another :")
    if condition_check == "yes":
        condition = True
    elif condition_check=="no":
        condition = False
