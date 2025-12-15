# ở đây mới chỉ thử code nhập tên và id
# chưa có điểm của sinh viên và hệ thống nhập in id, tên, điểm
# chưa có sửa xóa id, tên, điểm
# chưa có hiểm thị cả bảng điểm
# hi

def add():
    print("\n============= Add new student ==============")
    type_id()
    print("=================== Done ===================\n")

def type_name(id):
    global dic
    name = input("Full name (press Enter to go back): ").strip()
    if name == '': return type_id()
    for i in name:
        if not ('a'<=i<='z' or 'A'<=i<='Z' or i==' '):
            print("#. Invalid name, please try again!!!\n")
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
    return

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