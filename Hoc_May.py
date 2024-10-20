import pandas as pd

# Đọc file CSV hoặc TXT (nếu là file có cấu trúc bảng)
df = pd.read_csv('Diabetes-Data.csv')  # thay thế 'data-70.csv' bằng tên file cụ thể
print(df.head())
