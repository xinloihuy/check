# hàm này để tộng hợp code nha
import json
from datetime import date, datetime
from typing import List

# Class Goal
class Goal:
    def __init__(self, goal_id: int, goal_name: str, goal_amount: float, accumulated_amount: float, target_date: date):
        self.goal_id = goal_id
        self.goal_name = goal_name
        self.goal_amount = goal_amount
        self.accumulated_amount = accumulated_amount
        self.target_date = target_date

    def track_progress(self) -> float:
        if self.goal_amount == 0:
            return 0.0  # Tránh chia cho 0
        return (self.accumulated_amount / self.goal_amount) * 100

    def update_accumulated_amount(self, amount: float) -> None:
        self.accumulated_amount += amount
        print(f"Số tiền tích lũy đã được cập nhật. Tổng mới: {self.accumulated_amount}")

    def display_goal(self) -> None:
        progress = self.track_progress()
        print(f"Mã mục tiêu: {self.goal_id}")
        print(f"Tên mục tiêu: {self.goal_name}")
        print(f"Số tiền mục tiêu: {self.goal_amount}")
        print(f"Số tiền đã tích lũy: {self.accumulated_amount}")
        print(f"Ngày hoàn thành mục tiêu: {self.target_date}")
        print(f"Tiến độ: {progress:.2f}%")

# Class User
class User:
    def __init__(self, user_id: int, name: str, email: str, data_file: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.account_list = []
        self.transaction_list = []
        self.report_list = []
        self.goal_list = []
        self.data_file = data_file

    def save_to_file(self):
        """Lưu thông tin người dùng vào file JSON"""
        data = {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "account_list": self.account_list,
            "transaction_list": self.transaction_list,
            "report_list": self.report_list,
            "goal_list": [
                {
                    "goal_id": goal.goal_id,
                    "goal_name": goal.goal_name,
                    "goal_amount": goal.goal_amount,
                    "accumulated_amount": goal.accumulated_amount,
                    "target_date": goal.target_date.strftime("%Y-%m-%d"),
                }
                for goal in self.goal_list
            ],
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f)
        print("Thông tin đã được lưu")

    @staticmethod
    def load_from_file(file_path: str):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                user = User(
                    user_id=data["user_id"],
                    name=data["name"],
                    email=data["email"],
                    data_file=file_path,
                )
                user.account_list = data.get("account_list", [])
                user.transaction_list = data.get("transaction_list", [])
                user.report_list = data.get("report_list", [])
                for goal_data in data.get("goal_list", []):
                    target_date = datetime.strptime(goal_data["target_date"], "%Y-%m-%d").date()
                    goal = Goal(
                        goal_id=goal_data["goal_id"],
                        goal_name=goal_data["goal_name"],
                        goal_amount=goal_data["goal_amount"],
                        accumulated_amount=goal_data["accumulated_amount"],
                        target_date=target_date,
                    )
                    user.goal_list.append(goal)
                return user
        except FileNotFoundError:
            return None

    def create_account(self):
        account_name = input("Nhập tên tài khoản mới: ")
        self.account_list.append(account_name)
        self.save_to_file()
        print(f"Tài khoản '{account_name}' đã tạo thành công")

    def delete_account(self):
        print("Danh sách tài khoản hiện tại:", self.account_list)
        account_name = input("Nhập tên tài khoản cần xóa: ")
        if account_name in self.account_list:
            self.account_list.remove(account_name)
            self.save_to_file()
            print(f"Tài khoản '{account_name}' đã được xóa")
        else:
            print("Tài khoản không tồn tại")

    def create_goal(self):
        print("\nNhập thông tin mục tiêu:")
        goal_id = int(input("Nhập mã mục tiêu (số nguyên): "))
        goal_name = input("Nhập tên mục tiêu: ")
        goal_amount = float(input("Nhập số tiền mục tiêu (VNĐ): "))
        accumulated_amount = float(input("Nhập số tiền đã tích lũy (VNĐ): "))
        target_date_str = input("Nhập ngày hoàn thành mục tiêu (định dạng YYYY-MM-DD): ")
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()

        new_goal = Goal(goal_id, goal_name, goal_amount, accumulated_amount, target_date)
        self.goal_list.append(new_goal)
        self.save_to_file()
        print("Mục tiêu tài chính đã được tạo thành công")

    def view_goals(self):
        if not self.goal_list:
            print("Chưa có mục tiêu nào")
        else:
            for goal in self.goal_list:
                goal.display_goal()

    def update_goal(self):
        if not self.goal_list:
            print("Chưa có mục tiêu nào để cập nhật")
            return

        goal_id = int(input("Nhập mã mục tiêu cần cập nhật: "))
        for goal in self.goal_list:
            if goal.goal_id == goal_id:
                update_amount = float(input("Nhập số tiền bạn muốn thêm vào tích lũy: "))
                goal.update_accumulated_amount(update_amount)
                self.save_to_file()
                goal.display_goal()
                return
        print("Mục tiêu không tồn tại")

    def display_menu(self):
        while True:
            print("\n--- Menu Quản Lý Tài Chính Cá Nhân ---")
            print("1. Tạo tài khoản")
            print("2. Xóa tài khoản")
            print("3. Tạo mục tiêu tài chính")
            print("4. Xem danh sách mục tiêu")
            print("5. Cập nhật mục tiêu tài chính")
            print("6. Thoát")
            luaChon = input("Nhập lựa chọn của bạn: ")

            if luaChon == "1":
                self.create_account()
            elif luaChon == "2":
                self.delete_account()
            elif luaChon == "3":
                self.create_goal()
            elif luaChon == "4":
                self.view_goals()
            elif luaChon == "5":
                self.update_goal()
            elif luaChon == "6":
                print("Thoát chương trình")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại")


print("Chào mừng bạn đến với ứng dụng quản lý tài chính cá nhân")
data_file = "data.json"

user = User.load_from_file(data_file)
if not user:
    user_id = int(input("Nhập ID người dùng: "))
    name = input("Nhập tên người dùng: ")

    while True:
        email = input("Nhập email người dùng (phải là @gmail.com): ")
        if email.endswith("@gmail.com"):
            break
        else:
            print("Email không hợp lệ. Vui lòng nhập lại")

    user = User(user_id, name, email, data_file)
    user.save_to_file()

user.display_menu()
