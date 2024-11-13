import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from data_visualization import *
from file_handler import FileHandler
from data_cleaner import data_clean


class CSVEditorGUI:
    def __init__(self, root, handler_file_path):
        # Khởi tạo giao diện và thiết lập các thành phần
        self.root = root
        self.csv_handler = FileHandler(handler_file_path)
        self.root.title("Python Data Analysis")
        self.root.configure(bg="#f0ffff")
        

        self.sorting_order = {
            'ApplicantIncome': False,
            'CoapplicantIncome': False,
            'LoanAmount': False,
            'Loan_Amount_Term': False,
            'Credit_History': False
        }
        # Cấu hình phân trang
        self.items_per_page = 20  # Số dòng hiển thị trên mỗi trang
        self.current_page = 0  # Trang hiện tại


        # Cấu hình bảng dữ liệu Treeview và các nút chức năng
        self.tree = ttk.Treeview(root, columns=list(self.csv_handler.data_frame.columns), show='headings', height=20)
        self.tree.pack(pady=10)
        self.configure_treeview()

        self.entry_frame = tk.Frame(root, bg="#f3f4f6")
        self.entry_frame.pack(pady=10)
        self.entries = self.create_entry_widgets()

        self.create_button_frame()
        self.create_pagination_buttons()

        self.populate_tree()

    def configure_treeview(self):
        # Thiết lập cấu hình và kiểu hiển thị cho Treeview (bảng dữ liệu)
        style = ttk.Style()
        style.configure("Treeview", background="lightgrey", foreground="black", rowheight=25)
        style.map("Treeview", background=[("selected", "#4caf50")], foreground=[("selected", "white")])

        for col in self.csv_handler.data_frame.columns:
            # Thêm tính năng sắp xếp theo cột
            self.tree.heading(col, text=col, command=lambda _col=col: self.sort_column(_col))
            self.tree.column(col, width=100)

        for index, row in self.csv_handler.data_frame.iterrows():
            print(f"Index {index}: {list(row)}") 

    def sort_column(self, col):
        # Sắp xếp DataFrame theo cột được chọn
        ascending = self.sorting_order[col]
        self.csv_handler.data_frame.sort_values(by=col, ascending=ascending, inplace=True)
        self.sorting_order[col] = not ascending
        self.populate_tree()

    def create_entry_widgets(self):
        # Tạo các ô nhập liệu cho mỗi cột
        entries = {}
        for col in self.csv_handler.data_frame.columns:
            label = tk.Label(self.entry_frame, text=col, bg="#f3f4f6")
            label.grid(row=0, column=len(entries), padx=5, pady=5)

            entry = tk.Entry(self.entry_frame, width=15)
            entry.grid(row=1, column=len(entries), padx=5, pady=5)
            entries[col] = entry
        return entries

    def create_button_frame(self):
        button_frame = tk.Frame(self.root, bg="#f0f4f8")
        button_frame.pack(pady=15)
        
        actions = [("Thêm", self.add_data, "#4caf50", "white"),
                   ("Xóa", self.delete_data, "#f44336", "white"),
                   ("Cập Nhật", self.update_data, "#ffc107", "black"),
                   ("Làm Sạch Dữ Liệu", self.clean_data_button, "#2196f3", "white"),
                   ("Trực Quan Hóa", self.visualization_data, "#00FFFF", "black")]
        
        for i, (text, cmd, bg, fg) in enumerate(actions):
            tk.Button(button_frame, text=text, command=cmd, bg=bg, fg=fg, font=("Arial", 10), width=12, height=2).grid(row=0, column=i, padx=5)
        
    def create_pagination_buttons(self):
        # Tạo các nút phân trang
        pagination_frame = tk.Frame(self.root, bg="#f3f4f6")
        pagination_frame.pack(pady=10)

        self.prev_button = tk.Button(pagination_frame, text="Trang trước", command=self.prev_page, state="disabled")
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(pagination_frame, text="Trang sau", command=self.next_page)
        self.next_button.grid(row=0, column=1, padx=5)
    def populate_tree(self):
        # Xóa dữ liệu cũ trong Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Lấy dữ liệu của trang hiện tại
        start_index = self.current_page * self.items_per_page
        end_index = start_index + self.items_per_page
        page_data = self.csv_handler.data_frame.iloc[start_index:end_index]

        for index, row in page_data.iterrows():
            self.tree.insert("", "end", iid=index, values=list(row))

        # Cập nhật trạng thái của các nút phân trang
        self.update_pagination_buttons()
    def update_pagination_buttons(self):
        # Cập nhật trạng thái của các nút "Trang trước" và "Trang sau"
        total_items = len(self.csv_handler.data_frame)
        total_pages = (total_items // self.items_per_page) + (1 if total_items % self.items_per_page != 0 else 0)

        if self.current_page <= 0:
            self.prev_button.config(state="disabled")
        else:
            self.prev_button.config(state="normal")

        if self.current_page >= total_pages - 1:
            self.next_button.config(state="disabled")
        else:
            self.next_button.config(state="normal")

    def next_page(self):
        # Chuyển đến trang tiếp theo
        self.current_page += 1
        self.populate_tree()

    def prev_page(self):
        # Chuyển đến trang trước
        self.current_page -= 1
        self.populate_tree()

    def add_data(self):
        # Thêm dữ liệu từ các ô nhập vào DataFrame và cập nhật Treeview
        new_data = {}
        for col, entry in self.entries.items():
            value = entry.get()
            if value == "" and col in ["LoanAmount", "Credit_History"]:
                new_data[col] = None
            else:
                try:
                    if col in ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term"]:
                        new_data[col] = int(value)
                    elif col == "Credit_History":
                        new_data[col] = float(value)
                    else:
                        new_data[col] = value
                except ValueError:
                    messagebox.showwarning("Error", f"Giá trị '{value}' không hợp lệ cho cột '{col}'.")
                    return              
        if any(not v for k, v in new_data.items() if k not in ["LoanAmount", "Credit_History"]):
            messagebox.showwarning("Error", "Tất cả các ô nhập liệu phải được điền dữ liệu.")
            return

        self.csv_handler.add_row(new_data)
        self.populate_tree()
        self.clear_entries()
        print('Da them')

    def delete_data(self):
        # Xóa dòng được chọn khỏi DataFrame và Treeview
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Error", "Vui lòng chọn một dòng để xóa.")
            return

        for item in selected_item:
            index = int(item)
            self.csv_handler.data_frame.drop(index=index, inplace=True)
        
        self.csv_handler.data_frame.reset_index(drop=True, inplace=True)
        self.csv_handler.save_data()
        self.populate_tree()

    def update_data(self):
        # Cập nhật dòng dữ liệu đã chọn với các giá trị từ ô nhập liệu
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Error", "Vui lòng chọn một dòng để cập nhật.")
            return

        item_index = int(selected_item[0])
        updated_data = {}

        for col, entry in self.entries.items():
            value = entry.get()
            if value == "" and col in ["LoanAmount", "Credit_History"]:
                updated_data[col] = None
            else:
                try:
                    if col in ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term"]:
                        updated_data[col] = int(value)
                    elif col == "Credit_History":
                        updated_data[col] = float(value)
                    else:
                        updated_data[col] = value
                except ValueError:
                    messagebox.showwarning("Error", f"Giá trị '{value}' không hợp lệ cho cột '{col}'.")
                    return

        self.csv_handler.update_row(item_index, updated_data)
        self.populate_tree()
        self.clear_entries()
    def clean_data_button(self):
        # Kiểm tra nếu dữ liệu chưa được nạp
        if self.csv_handler.data_frame is None or self.csv_handler.data_frame.empty:
            messagebox.showwarning("No Data", "Please load a data file first.")
            return
    
        # Thực hiện làm sạch dữ liệu bằng cách gọi hàm data_clean
        self.csv_handler.data_frame = data_clean(self.csv_handler.data_frame)

        # Lưu lại dữ liệu đã làm sạch vào tệp
        self.csv_handler.save_data()

        # Làm mới Treeview với dữ liệu đã làm sạch
        self.populate_tree()

        # Thông báo cho người dùng quá trình làm sạch thành công
        messagebox.showinfo("Data Cleaned", "Data cleaning process completed.")



    def visualization_data(self):


        def histogram():
            new_histogram = tk.Toplevel(new_window)
            new_histogram.title("Nội dung biểu đồ")
            window_width = 580
            window_height = 490

            # Lấy kích thước màn hình
            screen_width =new_histogram.winfo_screenwidth()
            screen_height = new_histogram.winfo_screenheight()

            # Tính toán vị trí để cửa sổ nằm ở giữa màn hình
            x_position = (screen_width - window_width) // 2
            y_position = (screen_height - window_height) // 2

            # Đặt kích thước và vị trí cửa sổ mới
            new_histogram.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
            education = tk.Button(new_histogram, font = ("Times New Roman", 15), text = "Trình độ giáo dục đến cơ hội vay", width=50, height = 3, bg = "#00FF00", fg = "black", command=lambda: plot_histogram(self.csv_handler.data_frame, 1))
            education.place(x = 10,y = 15)
            married = tk.Button(new_histogram, font = ("Times New Roman", 15), text = "Cơ hội vay trước và sau kết hôn", width=50, height = 3, bg = "#00FF00", fg = "black", command=lambda: plot_histogram(self.csv_handler.data_frame, 2))
            married.place(x = 10, y = 110)
            gender = tk.Button(new_histogram, font = ("Times New Roman", 15), text = "Giới tính với cơ hội vay", bg = "#00FF00", fg = "black", width=50, height = 3, command=lambda: plot_histogram(self.csv_handler.data_frame, 3))
            gender.place(x = 10, y = 205 )
            property_area = tk.Button(new_histogram, font = ("Times New Roman", 15), text = "Khu vực ảnh hưởng đến cơ hội vay", width=50, height = 3, bg = "#00FF00", fg = "black", command=lambda: plot_histogram(self.csv_handler.data_frame, 4))
            property_area.place(x = 10,y = 300)          
            self_employed = tk.Button(new_histogram, font = ("Times New Roman", 15), text = "Thu nhập cá nhân với cơ hội vay", width=50, height = 3, bg = "#00FF00", fg = "black", command=lambda: plot_histogram(self.csv_handler.data_frame, 5))
            self_employed.place(x = 10,y =395)

        def scatter():
            new_scatter = tk.Toplevel(new_window)
            new_scatter.title("Nội dung biểu đồ")
            window_width = 580
            window_height = 300
            screen_width =new_scatter.winfo_screenwidth()
            screen_height =new_scatter.winfo_screenheight()
            x_position = (screen_width - window_width) // 2
            y_position = (screen_height - window_height) // 2
            new_scatter.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

            coapplicantIncome = tk.Button(new_scatter, font = ("Times New Roman", 15), text = "Ảnh hưởng của thu nhập người đồng vay đến số tiền vay", width=50, height = 3, bg = "#00FF00", fg = "black", command=lambda: plot_scatter(self.csv_handler.data_frame, 1))
            coapplicantIncome.place(x = 10,y = 15)
            applicantIncome = tk.Button(new_scatter, font = ("Times New Roman", 15), text = "Ảnh hưởng của thu nhập người vay chính đến số tiền vay", width=50, height = 3, bg = "#00FF00", fg = "black", command=lambda: plot_scatter(self.csv_handler.data_frame, 2))
            applicantIncome.place(x = 10, y = 110)
            loan_amount_term = tk.Button(new_scatter, font = ("Times New Roman", 15), text = "Ảnh hưởng của thu nhập người vay chính đến thời hạn vay", bg = "#00FF00", fg = "black", width=50, height = 3, command=lambda: plot_scatter(self.csv_handler.data_frame, 3))
            loan_amount_term.place(x = 10, y = 205 )


        selected_item = self.tree.selection()
        new_window = tk.Toplevel(self.root)
        new_window.title("Loại đồ thị")
        window_width = 360
        window_height = 200
        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        new_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        histogram_but = tk.Button(new_window, font = ("Times New Roman", 15), text = "Đồ thị Histogram (Đồ thị tần suất)", width=30, height = 3, bg = "yellow", fg = "black", command=histogram)
        histogram_but.place(x = 10,y = 15)
        scatter_but = tk.Button(new_window, font = ("Times New Roman", 15), text = "Đồ thị Scatter (Đồ thị phân tán)", width=30, height = 3, bg = "yellow", fg = "black", command=scatter)
        scatter_but.place(x = 10, y = 110)
        # exit_but = tk.Button(new_window, font = ("Times New Roman", 15), text = "EXIT", bg = "red", fg = "black", width=20, height = 2, command=lambda: exit(new_window))
        # exit_but.place(x = 10, y = 205 )


    def clear_entries(self):
        # Xóa dữ liệu trong tất cả các ô nhập
        for entry in self.entries.values():
            entry.delete(0, tk.END)