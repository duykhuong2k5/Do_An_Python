from sklearn.preprocessing import MinMaxScaler

# Chuẩn hóa dữ liệu với MinMaxScaler
def normalize_data(data, columns):
    scaler = MinMaxScaler()  # Khởi tạo scaler( bộ chuẩn hóa)
    data[columns] = scaler.fit_transform(data[columns])  # Chuẩn hóa các cột được chỉ định
    
    print("Dữ liệu đã được chuẩn hóa.")
    return data
