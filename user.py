from datetime import date
from typing import List

# Class user
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.account_list = []
        self.transaction_list = []
        self.report_list = []
        self.goal_list = []

    def create_account(self):
        account_name = input("Nhập tên tài khoản mới: ")
        self.account_list.append(account_name)
        print(f"Tài khoản '{account_name}' đã tạo thành công")

    def delete_account(self):
        print("Danh sách tài khoản hiện tại:", self.account_list)
        account_name = input("Nhập tên tài khoản cần xóa: ")
        if account_name in self.account_list:
            self.account_list.remove(account_name)
            print(f"Tài khoản '{account_name}' đã được xóa")
        else:
            print("Tài khoản không tồn tại")

    def create_report(self):
        report_id = int(input("Nhập ID báo cáo: "))
        report_type = input("Nhập loại báo cáo: ")
        creation_date = date.today()
        new_report = {"id": report_id, "type": report_type, "date": creation_date}
        self.report_list.append(new_report)
        print("Báo cáo mới đã được tạo")

    def view_balance(self):
        print("Số dư hiện tại của các tài khoản:")
        for i, account_name in enumerate(self.account_list, start=1):
            print(f"{i}. {account_name} - Số dư: 0đ (vd)")

    def display_menu(self):
        while True:
            print("\n--- Menu Quản Lý Tài Chính Cá Nhân ---")
            print("1. Tạo tài khoản")
            print("2. Xóa tài khoản")
            print("3. Tạo báo cáo")
            print("4. Xem số dư")
            print("5. Thoát")
            luaChon = input("Nhập lựa chọn của bạn: ")

            if luaChon == "1":
                self.create_account()
            elif luaChon == "2":
                self.delete_account()
            elif luaChon == "3":
                self.create_report()
            elif luaChon == "4":
                self.view_balance()
            elif luaChon == "5":
                print("Thoát chương trình")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại")


print("Chào mừng bạn đến với ứng dụng quản lý tài chính cá nhân")
user_id = int(input("Nhập ID người dùng: "))
name = input("Nhập tên người dùng: ")
email = input("Nhập email người dùng: ")

while True:
    email = input("Nhập email người dùng (phải là @gmail.com): ")
    if email.endswith("@gmail.com"):
        break
    else:
        print("Email không hợp lệ. Vui lòng nhập lại")

user = User(user_id, name, email)
user.display_menu()
