class Goal:
    def __init__(self, goal_name, target_amount, current_amount=0):
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.current_amount = current_amount

    def add_savings(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền phải lớn hơn 0")
        self.current_amount += amount

    def progress(self):
        """Trả về tiến độ đạt được của mục tiêu (phần trăm)"""
        return (self.current_amount / self.target_amount) * 100

    def is_completed(self):
        """Kiểm tra xem mục tiêu đã hoàn thành hay chưa"""
        return self.current_amount >= self.target_amount
