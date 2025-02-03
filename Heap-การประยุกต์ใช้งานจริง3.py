import heapq
from datetime import datetime
import time

class BankCustomer:
    def __init__(self, service_type, is_premium=False):
        self.service_type = service_type
        self.is_premium = is_premium
        self.arrival_time = datetime.now()
        
        # กำหนดลำดับความสำคัญตาม service_type และสถานะลูกค้า
        self.priority = self._calculate_priority()
        
    def _calculate_priority(self):
        # ลำดับความสำคัญ (ยิ่งน้อยยิ่งสำคัญ)
        priority = {
            'ฝาก-ถอน': 3,
            'ชำระค่าบริการ': 2,
            'เปิดบัญชี': 1,
            'สินเชื่อ': 0
        }
        
        # ลูกค้า Premium จะได้ priority สูงกว่าปกติ 1 ระดับ
        base_priority = priority.get(self.service_type, 4)
        if self.is_premium:
            base_priority -= 0.5
            
        return base_priority
        
    def __lt__(self, other):
        # เปรียบเทียบลำดับความสำคัญ
        if self.priority == other.priority:
            # ถ้าความสำคัญเท่ากัน ใช้เวลามาก่อน-หลัง
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority
        
class BankQueue:
    def __init__(self):
        self.queue = []  # heap queue
        self.waiting_count = 0
        self.customer_counter = 1  # ตัวนับคิว
        
    def add_customer(self, customer):
        heapq.heappush(self.queue, (customer.priority, self.customer_counter, customer))
        self.customer_counter += 1
        self.waiting_count += 1
        
    def serve_next_customer(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return None
            
        _, _, customer = heapq.heappop(self.queue)
        self.waiting_count -= 1
        
        wait_time = datetime.now() - customer.arrival_time
        print(f"\nเรียกคิว: {self.waiting_count + 1}")
        print(f"บริการ: {customer.service_type}")
        print(f"เวลารอ: {wait_time.seconds} วินาที")
        print(f"จำนวนคิวรอ: {self.waiting_count}")
        print("-" * 30)
        
        return customer
        
    def display_queue(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return
            
        print("\nรายการคิวที่รอ:")
        # สร้าง copy ของคิวเพื่อไม่ให้กระทบคิวจริง
        temp_queue = self.queue.copy()
        position = 1
        
        while temp_queue:
            _, _, customer = heapq.heappop(temp_queue)
            print(f"{position}. {customer.service_type}")
            position += 1
        print("-" * 30)

# ตัวอย่างการใช้งาน
def demo_bank_queue():
    bank = BankQueue()
    
    # เพิ่มลูกค้าเข้าคิว
    customers = [
        BankCustomer("ฝาก-ถอน"),
        BankCustomer("สินเชื่อ", is_premium=True),
        BankCustomer("ชำระค่าบริการ"),
        BankCustomer("เปิดบัญชี"),
        BankCustomer("สินเชื่อ")
    ]
    
    for customer in customers:
        bank.add_customer(customer)
        time.sleep(1)  # จำลองการมาถึงต่างเวลากัน
        
    print("\nแสดงลำดับคิว:")
    bank.display_queue()
    
    # จำลองการเรียกลูกค้าเข้ารับบริการ
    print("\nเริ่มเรียกลูกค้า:")
    for _ in range(len(customers)):
        bank.serve_next_customer()
        time.sleep(1)

if __name__ == "__main__":
    demo_bank_queue()

