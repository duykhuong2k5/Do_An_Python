import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Tải dữ liệu
df = pd.read_csv('processed_data.csv')

print(df.isnull().sum())

def fill_numerical_na(data, column, method='median'):
    """Điền giá trị thiếu cho các cột số bằng giá trị trung vị (median) hoặc trung bình (mean)."""
    if method == 'median':
        fill_value = data[column].median()
    elif method == 'mean':
        fill_value = data[column].mean()
    data[column].fillna(fill_value, inplace=True)
    #print(f"Đã điền giá trị thiếu cho {column} bằng {method}.")

def fill_categorical_na(data, column):
    """Điền giá trị thiếu cho các cột chuỗi bằng mode (giá trị phổ biến nhất)."""
    fill_value = data[column].mode()[0]
    data[column].fillna(fill_value, inplace=True)
    #print(f"Đã điền giá trị thiếu cho {column} bằng giá trị phổ biến nhất.")

# Làm sạch các giá trị thiếu
fill_numerical_na(df, 'LoanAmount', method='median')
fill_numerical_na(df, 'Loan_Amount_Term', method='median')
fill_numerical_na(df, 'Credit_History', method='median')

fill_categorical_na(df, 'Gender')
fill_categorical_na(df, 'Dependents')
fill_categorical_na(df, 'Self_Employed')