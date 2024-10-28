import pandas as pd
import numpy as np


class DataCleaner:
    def __init__(self, data_frame):
        self.data_frame = data_frame
    #Xóa các dòng trùng lặp trong DataFrame.
    def remove_duplicates(self):
        self.data_frame = self.data_frame.drop_duplicates()
    #Kiem tra gia trị bị thiếu trong mỗi tính năng
    def check_missing_values(self):
        missing = self.data_frame.isnull().sum()
        missing = missing[missing > 0]  # Filter to only include columns with missing values

        if missing.empty:
            print("No missing values in the DataFrame.")
        else:
            print("Missing values found in the following columns:")
            print(missing)

    def fill_missing_values(self):
        # Fill the null values of numerical datatype
        self.data_frame['LoanAmount'] = self.data_frame['LoanAmount'].fillna(self.data_frame['LoanAmount'].median())
        self.data_frame['Loan_Amount_Term'] = self.data_frame['Loan_Amount_Term'].fillna(self.data_frame['Loan_Amount_Term'].mean())
        self.data_frame['Credit_History'] = self.data_frame['Credit_History'].fillna(self.data_frame['Credit_History'].mean())

        # Fill the null values of object datatype
        self.data_frame['Gender'] = self.data_frame['Gender'].fillna(self.data_frame['Gender'].mode()[0])
        self.data_frame['Married'] = self.data_frame['Married'].fillna(self.data_frame['Married'].mode()[0])
        self.data_frame['Dependents'] = self.data_frame['Dependents'].fillna(self.data_frame['Dependents'].mode()[0])
        self.data_frame['Self_Employed'] = self.data_frame['Self_Employed'].fillna(self.data_frame['Self_Employed'].mode()[0])
    #Sửa chữa nhãn không chính xác
    def fix_incorrect_labels(self):
        valid_dependents = ['0', '1', '2', '3+']
        self.data_frame['Dependents'] = self.data_frame['Dependents'].where(
            self.data_frame['Dependents'].isin(valid_dependents), '0')  # Replace invalid with '0'
    #Chuẩn hóa dữ liệu
    def encode_loan_status(self):
        """Encode Loan_Status values from 'Y'/'N' to 1/0."""
        self.data_frame.replace({"Loan_Status": {"N": 0, "Y": 1}}, inplace=True)

    def normalize_dependents(self):
        """Replace '3+' in Dependents with 4 to standardize values."""
        self.data_frame['Dependents'] = self.data_frame['Dependents'].replace(to_replace='3+', value=4)