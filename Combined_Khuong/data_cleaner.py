import pandas as pd

def data_clean(data_frame):
    # Xóa các bản ghi trùng lặp trong DataFrame
    data_frame.drop_duplicates()


    # Điền giá trị mặc định cho các cột có giá trị thiếu
    # Sử dụng trung vị hoặc trung bình cho số, mode cho các giá trị phân loại
    data_frame['LoanAmount'] = data_frame['LoanAmount'].fillna(data_frame['LoanAmount'].median())
    data_frame['Loan_Amount_Term'] = data_frame['Loan_Amount_Term'].fillna(data_frame['Loan_Amount_Term'].mean())
    data_frame['Credit_History'] = data_frame['Credit_History'].fillna(data_frame['Credit_History'].mean())

    data_frame['Gender'] = data_frame['Gender'].fillna(data_frame['Gender'].mode()[0])
    data_frame['Married'] = data_frame['Married'].fillna(data_frame['Married'].mode()[0])
    data_frame['Dependents'] = data_frame['Dependents'].fillna(data_frame['Dependents'].mode()[0])
    data_frame['Self_Employed'] = data_frame['Self_Employed'].fillna(data_frame['Self_Employed'].mode()[0])

    """Encode Loan_Status values from 'Y'/'N' to 1/0."""
    data_frame.replace({"Loan_Status": {"N": 0, "Y": 1}}, inplace=True)

    """Replace '3+' in Dependents with 4 to standardize values."""
    data_frame['Dependents'] = data_frame['Dependents'].replace(to_replace='3+', value=4)
    
    return data_frame
