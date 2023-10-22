def get_data_fixed_n():
    n = int(input("Input number of data (n): "))
    n =list(n)# กำหนดค่าเริ่มต้นให้กับตัวแปร data ที่อยู่ในรูปแบบ list
    
    for i in range(n):# for loop
        print("Input x[%d]: " %(i), end="")
        x = float(input())
    # เพิ่มข้อมูลเข้าไปในตัวแปร data return data

input_data = get_data_fixed_n()
print("Input data using get_data_fixed_n(): ", input_data)

