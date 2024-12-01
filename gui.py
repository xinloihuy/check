import tkinter
from tkinter import *
from datetime import datetime
from tkinter import messagebox

# Tạo danh sách người dùng
users = []

class Account:
    def __init__(self, name="", account_type="", balance=0):
        self.name = name
        self.type = account_type  # Ví dụ: "Ngân hàng", "Tiền mặt","BIDV","Vietcombank", "Ví điện tử"
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền phải lớn hơn 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Số dư không đủ")
        self.balance -= amount

    def transfer(self, target_account, amount):
        if amount > self.balance:
            raise ValueError("Số dư không đủ")
        self.withdraw(amount)
        target_account.deposit(amount)

class User:
    def __init__(self, name="", email=""):
        self.name = name
        self.email = email
        self.accounts = []  # Danh sách các tài khoản ngân hàng
        self.transactions = []  # Lịch sử giao dịch
        self.total_balance = 0  # Tổng số dư từ tất cả tài khoản
        self.total_loan = 0
    def add_account(self, account):
        self.accounts.append(account)
        self.update_balance()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        # Tìm tài khoản liên quan để cập nhật
        for account in self.accounts:
            if account.account_name == transaction.account_name:
                account.add_transaction(transaction)
                break
        self.update_balance()

    def update_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts)

    def __eq__(self, other):
        # So sánh dựa trên tên và email
        if isinstance(other, User):
            return self.name == other.name and self.email == other.email
        return False


class FinancialApp():
    def __init__(self):
        self.window = Tk()
        self.window.title("Ứng dụng Quản lý Tài chính Cá Nhân")
        self.window.geometry("800x600")
        # Nút thêm người dùng
        Button(self.window, text="Thêm Người Dùng", command=self.add_user).pack(pady=10)
        Button(self.window, text="Xem Người Dùng", command=self.view_users).pack(pady=10)
        Button(self.window, text="Register User",command=self.register_user).pack(pady=10)
    def add_user(self):
        add_user_window = Toplevel(self.window)
        add_user_window.title("Thêm Người Dùng")
        add_user_window.geometry("400x300")

        Label(add_user_window, text="Tên:").pack(pady=5)
        name_entry = Entry(add_user_window)
        name_entry.pack(pady=5)

        Label(add_user_window, text="Email:").pack(pady=5)
        email_entry = Entry(add_user_window)
        email_entry.pack(pady=5)

        def save_user():
            name = name_entry.get()
            email = email_entry.get()
            if name and email:
                user = User(name, email)
                users.append(user)
                messagebox.showinfo("Thành công", "Người dùng đã được thêm!")
                add_user_window.destroy()
            else:
                messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")

        Button(add_user_window, text="Lưu", command=save_user).pack(pady=10)

    def view_users(self):
        view_users_window = Toplevel(self.window)
        view_users_window.title("Danh Sách Người Dùng")
        view_users_window.geometry("400x400")

        for user in users:
            user_info = f"Tên: {user.name}, Email: {user.email}, Số dư: {user.total_balance}"
            Label(view_users_window, text=user_info).pack(pady=5)

    def register_user(self):
        register_window = Toplevel(self.window)
        register_window.title('Register User')
        register_window.geometry('400x400')
        Label(register_window,text="Nhập tên:").grid(row=1,column=0)
        name = Entry(register_window)
        name.grid(row=1,column=1)
        Label(register_window, text="Nhập email:").grid(row=2, column=0)
        email = Entry(register_window)
        email.grid(row=2, column=1)
        Button(register_window, text="Đăng nhập", command=lambda:Register()).grid(row=3, column=0)
        USER = User()

        def Register():
            nonlocal USER
            name_input = name.get()
            email_input = email.get()

            if not name_input or not email_input:
                messagebox.showerror('Lỗi', 'Vui lòng nhập đầy đủ thông tin!')
                return

            # Kiểm tra xem người dùng đã tồn tại hay chưa
            existing_user = next((u for u in users if u.name == name_input and u.email == email_input), None)

            if existing_user:
                USER = existing_user  # Dùng lại user cũ
                messagebox.showinfo('Thông báo', 'User đã tồn tại! Đăng nhập thành công.')
            else:
                # Tạo mới user nếu chưa tồn tại
                USER = User(name_input, email_input)
                users.append(USER)
                messagebox.showinfo('Thành công', 'User đã được đăng ký!')

            register_window.destroy()
            After_Register()

        def After_Register():
            nonlocal USER
            AfterRegister_window = Toplevel(self.window)
            AfterRegister_window.title('Menu')
            AfterRegister_window.geometry('400x600')
            self.window.withdraw()

            def ChuyenTien():
                pass

            def SoDu():
                nonlocal USER
                messagebox.showinfo('Số Dư', f'Số dư của user {USER.name} là: {USER.total_balance}đ')

            def Vay():
                nonlocal USER
                messagebox.showinfo('Khoản Vay Cá Nhân', f'Số tiền đã vay: {USER.total_loan}đ')

            def LichSu():
                pass

            def XoaLichSu():
                pass

            def TaoAccount():
                TaoAccount_window = Toplevel(AfterRegister_window)
                TaoAccount_window.title('Tạo Account')
                TaoAccount_window.geometry("400x400")

                def Tao():
                    # Lấy giá trị từ các Entry
                    account_name = name_entry.get()
                    account_type = type_entry.get()
                    account_balance = balance_entry.get()

                    # Kiểm tra dữ liệu nhập vào
                    if not account_name or not account_type or not account_balance.isdigit():
                        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ và đúng thông tin!")
                        return

                    # Chuyển đổi balance thành số
                    balance = int(account_balance)

                    # Giả sử USER.add_account là một hàm hợp lệ
                    USER.add_account(Account(account_name, account_type, balance))
                    messagebox.showinfo("Thành công", "Account đã được tạo!")
                    TaoAccount_window.destroy()  # Đóng cửa sổ sau khi tạo xong

                # Tạo các nhãn và ô nhập liệu
                Label(TaoAccount_window, text="Tên:").grid(row=0, column=0)
                name_entry = Entry(TaoAccount_window)
                name_entry.grid(row=0, column=1)

                Label(TaoAccount_window, text="Type:").grid(row=1, column=0)
                type_entry = Entry(TaoAccount_window)
                type_entry.grid(row=1, column=1)

                Label(TaoAccount_window, text="Số Dư:").grid(row=2, column=0)
                balance_entry = Entry(TaoAccount_window)
                balance_entry.grid(row=2, column=1)

                # Nút bấm "Tạo"
                Button(TaoAccount_window, text="Tạo", command=Tao).grid(row=3, column=0)

            def XoaAccount():
                pass

            def SuaAccount():
                pass

            def ShowAccount():
                ShowAccount_window = Toplevel(AfterRegister_window)
                ShowAccount_window.title('Thông tin các tài khoản')
                ShowAccount_window.geometry('400x400')

                for account in USER.accounts:
                    user_info = f"Tên: {account.name}, Loại: {account.type}, Số dư: {account.balance}"
                    Label(ShowAccount_window, text=user_info).pack(pady=5)

            def Login():
                AfterRegister_window.withdraw()
                Login_window = Toplevel(AfterRegister_window)
                Login_window.geometry("400x400")
                Login_window.title("Login Account")

                Label(Login_window,text="Tên").grid(row=1,column=0)
                account_name = Entry(Login_window)
                account_name.grid(row=1,column=1)

                Label(Login_window, text="Type:").grid(row=2, column=0)
                account_type = Entry(Login_window)
                account_type.grid(row=2, column=1)

                Button(Login_window,text="Login",command=lambda : check_login()).grid(row=3,column=0)
                ACCOUNT = Account()
                def check_login():
                    nonlocal ACCOUNT
                    name_entry = account_name.get()
                    type_entry = account_type.get()

                    if not name_entry or not type_entry:
                        messagebox.showerror('Lỗi', 'Vui lòng nhập đầy đủ thông tin!')
                        return

                    # Kiểm tra xem account đã tồn tại hay chưa
                    for user in users:
                        existing_account = next((a for a in user.accounts if a.name == name_entry and a.email == type_entry), None)
                        if existing_account:
                            break

                    if existing_account:
                        ACCOUNT = existing_account  # Dùng lại user cũ
                        messagebox.showinfo('Thông báo', 'Account đã tồn tại! Đăng nhập thành công.')
                    else:
                        # Tạo mới account nếu chưa tồn tại
                        ACCOUNT = Account(name_entry, type_entry)
                        for i in range(len(users)):
                            if users[i].name == USER.name and users[i].email == USER.email:
                                users[i].accounts.append(ACCOUNT)
                                break
                        messagebox.showinfo('Thành công', 'Account đã được đăng ký!')

                    Login_window.destroy()
                    TrangChu()


                def TrangChu():
                    nonlocal ACCOUNT
                    Home_window = Toplevel(AfterRegister_window)
                    Home_window.title("Home")
                    Home_window.geometry("400x400")

                    def ChuyenTien():
                        pass

                    def NapTien():
                        pass

                    def SoDu():
                        pass

                    def Vay():
                        pass

                    def ChoVay():
                        pass

                    def XemKhoanVay():
                        pass

                    def DatMucTieu():
                        pass

                    def XemTienDoHoanThanh():
                        pass

                    def LichSu():
                        pass
                    def Exit():
                        nonlocal ACCOUNT
                        # Cập nhật thông tin user trong danh sách
                        for i in range(len(users)):
                            for j in range(len(users[i].accounts)):
                                if users[i].accounts[j].name == ACCOUNT.name and users[i].accounts[j].type == ACCOUNT.type:
                                    users[i].accounts[j] = ACCOUNT  # Lưu lại thông tin account hiện tại
                                    break
                        Home_window.destroy()
                        AfterRegister_window.deiconify()


                    Button(Home_window,text="Chuyển tiền").pack(pady=5)
                    Button(Home_window,text="Nạp tiền",command=NapTien).pack(pady=5)
                    Button(Home_window, text="Số Dư", command=SoDu).pack(pady=5)
                    Button(Home_window,text="Vay",command=Vay).pack(pady=5)
                    Button(Home_window, text="Cho Vay", command=ChoVay).pack(pady=5)
                    Button(Home_window, text="Xem Thời Hạn Trả Khoản Vay", command=XemKhoanVay).pack(pady=5)
                    Button(Home_window, text="Đặt Mục Tiêu Tiết Kiệm", command=DatMucTieu).pack(pady=5)
                    Button(Home_window, text="Xem Tiến Độ Hoàn Thành Mục Tiêu", command=XemTienDoHoanThanh).pack(pady=5)
                    Button(Home_window, text="Lịch Sử Giao Dịch", command=LichSu).pack(pady=5)
                    Button(Home_window, text="Log out",command=Exit).pack(pady=5)



            def Exit():
                nonlocal USER
                # Cập nhật thông tin user trong danh sách
                for i in range(len(users)):
                    if users[i].name == USER.name and users[i].email == USER.email:
                        users[i] = USER  # Lưu lại thông tin user hiện tại
                        break
                AfterRegister_window.destroy()
                self.window.deiconify()

            Button(AfterRegister_window, text="Tạo Account", command=TaoAccount).pack(pady=5)
            Button(AfterRegister_window, text="Sửa Account", command=SuaAccount).pack(pady=5)
            Button(AfterRegister_window, text="Xóa Account", command=SuaAccount).pack(pady=5)
            Button(AfterRegister_window, text="Show Accounts", command=ShowAccount).pack(pady=5)
            Button(AfterRegister_window, text="Tổng Số Dư", command=SoDu).pack(pady=5)
            Button(AfterRegister_window, text="Show Vay", command=Vay).pack(pady=5)
            Button(AfterRegister_window, text="Lịch Sử", command=LichSu).pack(pady=5)
            Button(AfterRegister_window, text="Xóa Lịch Sử", command=XoaLichSu).pack(pady=5)
            Button(AfterRegister_window, text="Báo cáo thu nhập và chi tiêu", command=XoaLichSu).pack(pady=5)
            Button(AfterRegister_window, text="Báo cáo khoản vay và cho vay", command=XoaLichSu).pack(pady=5)
            Button(AfterRegister_window, text="Login Account", command=Login).pack(pady=5)
            Button(AfterRegister_window, text="Exit", command=Exit).pack(pady=5)
            AfterRegister_window.mainloop()




    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    app = FinancialApp()
    app.run()