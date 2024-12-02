from datetime import date, datetime

# class goal
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

def create_goal_from_user_input():
    print("\nNhập thông tin mục tiêu:")
    
    while True:
        try:
            goal_id = int(input("Nhập mã mục tiêu (số nguyên): "))
            break
        except ValueError:
            print("Mã mục tiêu phải là số nguyên! Vui lòng nhập lại.")
    
    goal_name = input("Nhập tên mục tiêu: ")
    
    while True:
        try:
            goal_amount = float(input("Nhập số tiền mục tiêu (VNĐ): "))
            if goal_amount <= 0:
                raise ValueError("Số tiền mục tiêu phải lớn hơn 0!")
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            accumulated_amount = float(input("Nhập số tiền đã tích lũy (VNĐ): "))
            if accumulated_amount < 0:
                raise ValueError("Số tiền tích lũy không được nhỏ hơn 0!")
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            target_date_str = input("Nhập ngày hoàn thành mục tiêu (định dạng YYYY-MM-DD): ")
            target_date = datetime.strptime(target_date_str, "%Y-%m-%Y").date()
            break
        except ValueError:
            print("Định dạng ngày không hợp lệ! Vui lòng nhập lại.")
    
    return Goal(goal_id, goal_name, goal_amount, accumulated_amount, target_date)


print("Quản lý mục tiêu tài chính")    
goal = create_goal_from_user_input()
print("\nThông tin mục tiêu đã tạo:")
goal.display_goal()
    
while True:
    try:
        update_amount = float(input("\nNhập số tiền bạn muốn thêm vào tích lũy (hoặc nhập 0 để thoát): "))
        if update_amount == 0:
            break
        goal.update_accumulated_amount(update_amount)
        goal.display_goal()
    except ValueError:
        print("Vui lòng nhập một số hợp lệ")
