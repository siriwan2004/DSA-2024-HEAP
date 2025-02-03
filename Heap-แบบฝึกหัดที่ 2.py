class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def left_child(self, i):
        return 2 * i + 1
        
    def right_child(self, i):
        return 2 * i + 2
        
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)

    def _sift_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != i:
            self.swap(i, largest)
            self._sift_down(largest)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_value

    def get_heap(self):
        return self.heap

# สร้าง Max Heap
max_heap = MaxHeap()

# รายการค่าที่ต้องเพิ่ม
values = [5, 3, 8, 1, 2, 7, 6, 4]

# เพิ่มค่าลงใน Max Heap
for value in values:
    max_heap.insert(value)

# แสดงค่าใน Max Heap หลังจากแทรกข้อมูลครบ
print("Max Heap:", max_heap.get_heap())

# ลบค่าสูงสุด 3 ครั้ง และแสดงค่า Heap หลังจากลบแต่ละครั้ง
for _ in range(3):
    removed = max_heap.extract_max()
    print(f"Removed: {removed}, Heap: {max_heap.get_heap()}")
