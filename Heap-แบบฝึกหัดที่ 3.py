def is_max_heap(arr):
    n = len(arr)
    
    # ตรวจสอบทุก node ที่มีลูก
    for i in range(n // 2):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        # ตรวจสอบลูกซ้าย
        if left_child < n and arr[i] < arr[left_child]:
            return False
        
        # ตรวจสอบลูกขวา
        if right_child < n and arr[i] < arr[right_child]:
            return False
    
    return True

arr = [8, 4, 7, 3, 2, 5, 6, 1]
if is_max_heap(arr):
    print(f"The array {arr} is a valid Max Heap")  # ผลลัพธ์: True
else:
    print(f"The array {arr} is NOT a valid Max Heap")  # ผลลัพธ์: False
