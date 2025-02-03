import heapq

class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority  # ระดับความรุนแรง 1-5 (1 = ฉุกเฉินมาก)
    
    def __lt__(self, other):
        return self.priority < other.priority

class ERQueue:
    def __init__(self):
        self.queue = []  # Min Heap เพื่อให้ผู้ป่วยที่มี priority ต่ำ (อาการหนัก) ได้รับการรักษาก่อน
    
    def add_patient(self, patient):
        heapq.heappush(self.queue, patient)
    
    def treat_next_patient(self):
        if self.queue:
            return heapq.heappop(self.queue)
        return None

# ตัวอย่างการใช้งาน
er = ERQueue()
er.add_patient(Patient("คนไข้ A", 1))  # หัวใจวาย
er.add_patient(Patient("คนไข้ B", 3))  # ปวดท้อง
er.add_patient(Patient("คนไข้ C", 2))  # กระดูกหัก

# ทดสอบการรักษาผู้ป่วย
while patient := er.treat_next_patient():
    print(f"รักษาผู้ป่วย:{patient.name} ระดับความรุนแรง:{patient.priority}")
