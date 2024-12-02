from datetime import datetime
class GiaoDich:
    _sotudong=0
    def __init__(self,loai):
        GiaoDich._sotudong+=1
        self.magiaodich=self.TaoMaGD()
        self.LoaiGD=loai
        self.sotien=float(input("Nhập số tiền:"))
        self.ngaygiaodich=datetime.now().strftime('%d-%m-%Y')
        self.ghichu=input("Ghi chú( nếu không có ghi chú chỉ cần nhập /):")
    @classmethod
    def TaoMaGD(cls):
        ngay=datetime.now().strftime("%Y%m%d")
        return f"GD-{ngay}-{cls._sotudong:04d}"
    def Xuat(self):
        return (f"Mã giao dịch: {self.magiaodich}\n"
                f"Loại giao dịch: {self.LoaiGD}\n"
                f"Ngày giao dịch: {self.ngaygiaodich}\n"
                f"Số tiền: {self.sotien}\n"
                f"Ghi chú: {self.ghichu}\n")

