import pandas as pd
from file_handler import FileHandler

class DataManager:
    def __init__(self, file_path):
        """Khởi tạo DataManager với FileHandler để quản lý tệp dữ liệu."""
        self.file_handler = FileHandler(file_path)
        self.data_frame = self.file_handler.load_data()

    def create_entry(self, new_data):
        """Thêm một bản ghi mới vào DataFrame và lưu lại."""
        new_row_df = pd.DataFrame([new_data])
        self.data_frame = pd.concat([self.data_frame, new_row_df], ignore_index=True)
        self.file_handler.save_data(self.data_frame)

    def read_data(self):
        """Trả về DataFrame hiện tại."""
        return self.data_frame

    def update_entry(self, row_index, updated_data):
        """Cập nhật một bản ghi cụ thể trong DataFrame theo chỉ mục."""
        for col, value in updated_data.items():
            if col in self.data_frame.columns:
                self.data_frame.at[row_index, col] = value
        self.file_handler.save_data(self.data_frame)

    def delete_entry(self, row_index):
        """Xóa một bản ghi khỏi DataFrame theo chỉ mục."""
        if 0 <= row_index < len(self.data_frame):
            self.data_frame = self.data_frame.drop(row_index).reset_index(drop=True)
            self.file_handler.save_data(self.data_frame)
        else:
            raise IndexError("Chỉ mục không hợp lệ. Không có bản ghi nào được xóa.")
