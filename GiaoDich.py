from datetime import datetime
class GiaoDich:
    _sotudong=0
    def __init__(self,loai,sotien,ghichu):
        GiaoDich._sotudong+=1
        self.magiaodich=self.TaoMaGD()
        self.LoaiGD=loai
        self.sotien=sotien
        self.ngaygiaodich=datetime.now().strftime('%d-%m-%Y')
        self.ghichu=ghichu
    @classmethod
    def TaoMaGD(cls):
        ngay=datetime.now().strftime("%d%m%Y")
        return f"GD-{ngay}-{cls._sotudong:04d}"
    def Xuat(self):
        return (f"Mã giao dịch: {self.magiaodich}\n"
                f"Loại giao dịch: {self.LoaiGD}\n"
                f"Ngày giao dịch: {self.ngaygiaodich}\n"
                f"Số tiền: {self.sotien}\n"
                f"Ghi chú: {self.ghichu}\n")
