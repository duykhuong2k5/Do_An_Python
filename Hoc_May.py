import pandas as pd
df = pd.read_csv("chipotle.tsv", sep="\t")
#print(df.head(5))
print(df.info())
# CREATE Tạo một bản ghi mới
new_row = {
    'order_id': 9999,
    'quantity': 1,
    'item_name': 'New Item',
    'choice_description': '[Fresh]',
    'item_price': '$10.99'
}

# Thêm bản ghi mới vào dataset sử dụng loc
df.loc[len(df)] = new_row

print("Dữ liệu sau khi thêm bản ghi mới:\n", df.tail())
print(df.info())
#READ
# Đọc toàn bộ dataset
print(df.head())

# Tìm kiếm một bản ghi với item_name cụ thể
search_result = df[df['item_name'] == 'New Item']
print("Kết quả tìm kiếm cho 'New Item':\n", search_result)
#UPDATE
# Cập nhật giá của 'New Item'
df.loc[df['item_name'] == 'New Item', 'item_price'] = '$12.99'
print("Dữ liệu sau khi cập nhật:\n", df[df['item_name'] == 'New Item'])
#DELETE
# Xóa bản ghi với item_name là 'New Item'
df = df[df['item_name'] != 'New Item']
print("Dữ liệu sau khi xóa:\n", df.tail())