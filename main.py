from data_handling import load_data, save_data
from data_cleaning import clean_data
from data_normalization import normalize_data
from data_visualization import plot_histogram, plot_scatter

def main():
    # Đường dẫn tới tệp dữ liệu
    file_path = "test_Y3wMUE5_7gLdaTN.csv"  
    data = load_data(file_path)  # Đọc dữ liệu từ tệp
    if data is None:
        print("Lỗi: Không thể tiếp tục vì không có dữ liệu hợp lệ.")
        return  # Thoát nếu không có dữ liệu hợp lệ

    # Làm sạch dữ liệu
    data = clean_data(data)  # Loại bỏ trùng lặp
    #data = fill_missing(data, "LoanAmount", 0)  # Điền giá trị cho ô trống trong cột "LoanAmount"

    # Chuẩn hóa dữ liệu
    data = normalize_data(data, ["ApplicantIncome", "CoapplicantIncome", "LoanAmount"])  # Chuẩn hóa các cột

    # Trực quan hóa dữ liệu
    plot_histogram(data, "LoanAmount")  # Vẽ histogram của cột "LoanAmount"
    plot_scatter(data, "ApplicantIncome", "LoanAmount")  # Vẽ biểu đồ scatter giữa "ApplicantIncome" và "LoanAmount"

    # Lưu lại dữ liệu đã xử lý
    save_data(data, "processed_data.csv")  # Lưu vào tệp CSV mới

if __name__ == "__main__":
    main() 
