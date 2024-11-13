import tkinter as tk
from user_interface import CSVEditorGUI

def main():
    # file_path = "C:/Users/dinht/OneDrive/Documents/spkt_nam_2/PYTHON/DoAnPython/Do_An_Python/Cruid_clean_Chuanhoa/train_u6lujuX_CVtuZ9i.csv"
    file_path = "D:/Temp/DoAn/python_doan/train_u6lujuX_CVtuZ9i.csv"
    root = tk.Tk()
    app = CSVEditorGUI(root, file_path)

    root.mainloop()

if __name__ == "__main__":
    main()
