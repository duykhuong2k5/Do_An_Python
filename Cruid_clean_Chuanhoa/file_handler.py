import pandas as pd
import os

class FileHandler:
    def __init__(self, file_path):
        """Khởi tạo FileHandler với đường dẫn tệp."""
        self.file_path = file_path

    def load_data(self):
        """Tải dữ liệu từ tệp CSV nếu nó tồn tại; nếu không, tạo một DataFrame mới với các cột mặc định."""
        if os.path.exists(self.file_path):
            # Đọc tệp CSV và trả về DataFrame
            return pd.read_csv(self.file_path, low_memory=False)
        else:
            # Nếu tệp không tồn tại, tạo DataFrame rỗng với các cột mặc định
            return pd.DataFrame(columns=["Loan_ID", "Gender", "Married", "Dependents",
                                          "Education", "Self_Employed", "ApplicantIncome",
                                          "CoapplicantIncome", "LoanAmount",
                                          "Loan_Amount_Term", "Credit_History",
                                          "Property_Area", "Loan_Status"])

    def save_data(self, data_frame):
        """Lưu DataFrame trở lại tệp CSV."""
        data_frame.to_csv(self.file_path, index=False)
