# ở đây mới chỉ thử code nhập tên và id
# chưa có điểm của sinh viên và hệ thống nhập in id, tên, điểm
# chưa có sửa xóa id, tên, điểm
# chưa có hiển thị cả bảng điểm
# hi
# hello

def add():
    print("\n============= Add new student ==============")
    type_id()
    print("=================== Done ===================\n")
from unicodedata import category
def type_name(id):
    global dic
    name = input("Full name (press Enter to go back): ").strip() 
    for i in name:
        if not category(i).startswith(("L", "Zs")):
            print("#. Invalid Name, please try again!!!\n")
            return type_name(id)
    dic[id]=name

def type_id():
    id = input("ID number (press Enter to go back): ").strip()
    if id == '': return
    for i in id:
        if not '0'<=i<='9':
            print("#. Invalid ID, please try again!!!\n")
            return type_id()
    type_name(id)

def search():
    global dic
    print("\n================ Search ====================")
    information_to_fin = input("Input ID (press Enter to go back): ").strip()
    if information_to_fin == '': return
    if information_to_fin in dic.keys():
        print("The student's name is:", dic[information_to_fin], "\n")
        return
    else:
        print("#. No student has this ID number, or this ID number does not exist.")
        print("#. Please try again!!!")
        return search()

def menu():
    print("========== Classroom Data Manager ==========")
    print("1. Add new student")
    print("2. Search by student ID")
    print("3. Display all scores")
    print("4. Exit")
    print("Choose an option: ", end = "")
    a = input().strip()
    if a == '1': 
        add()
    elif a == '2':
        search()
    elif a == '4': 
        print("=================== Exit ===================")
        return
    else: 
        print("#. Invalid choise, please try again!!!\n")
    menu()

dic = {}
menu()
