import random

def random_students(MAX=30):
    students = []
    for _ in range(MAX):
        name = chr(random.randint(65,90)) + chr(random.randint(65,90))
        age= random.randint(18,22)
        score = random.randint(0,100)
        students.append({"이름": name, "나이": age, "성적": score})

    with open("random_students.txt", "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}\n")

    return students

# 정렬 알고리즘 구현
def selection_sort(student_data, key):
    n = len(student_data)
    for i in range(0, n-1, 1):
        least = i
        for j in range(i+1, n):
            if student_data[j][key] < student_data[least][key]:
               least = j
        student_data[i], student_data[least] = student_data[least], student_data[i]

def insertion_sort(student_data, key):
    n = len(student_data)
    for i in range(1, n):
        now = student_data[i] 
        j = i - 1
        while j>=0 and student_data[j][key]>now[key]:
            student_data[j+1]=student_data[j]
            j -= 1
        student_data[j+1] = now

#quick_sort
def quick_sort(student_data, left, right, key):
    if left<right:
            q = partition(student_data, left, right, key)
            quick_sort(student_data, left, q-1, key)
            quick_sort(student_data, q+1, right, key)

def partition(student_data, left, right, key):
    low = left + 1
    high = right
    pivot = student_data[left][key]
    while low <= high:
        while low <= right and student_data[low][key]<=pivot:
            low += 1
        while high >= left and student_data[high][key]> pivot:
            high -= 1
        if low < high:
            student_data[low], student_data[high] = student_data[high], student_data[low]
    student_data[left], student_data[right] = student_data[high], student_data[left]
    return high 

#radix_sort
class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self,item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            print("Queue is full. Cannot enqueue.")

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            item = self.array[self.front]
            self.array[self.front] = None
            return item
        else:
          print("Queue is empty. Cannot dequeue.")
          return None
            
def radix_sort(student_data, key):
    Buckets = 10
    Digit = len(str(max(student[key] for student in student_data)))

    queues = [ArrayQueue(len(student_data)) for _ in range(Buckets)]
    factor = 1

    for d in range(Digit):
        for student in student_data:
            digit = (student[key] // factor)%Buckets
            queues[digit].enqueue(student)
        
        i = 0
        for b in range(Buckets):
            while not queues[b].is_empty():
                student_data[i] = queues[b].dequeue()
                i += 1
                
        factor *= Buckets
            

#counting_sort
def counting_sort(student_data, key=None):
    if key is not None:
        student_data = [student[key] for student in student_data]

    max_val = max(student_data)
    count = [0] * (max_val+1)
    
    for num in student_data:
        count[num] += 1

    for i in range(1, len(count)):
        count[1] += count[i-1]
        
    output = [0] * len(student_data)

    for num in reversed(student_data):
        output[count[num]-1] = num
        count[num] -= 1

    return output

#정렬/원본 학생 출력
def print_students(students):
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

def main():
    students = random_students()
    print("생성된 학생 정보:")
    print_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")

        select = input("정렬 기준을 선택하세요 (1,2,3,4): ")

        if select == '4':
            print("프로그램을 종료합니다. 20231329_서원후")
            break
            
        #입력예외처리
        key_field = {'1':'이름', '2':'나이', '3':'성적'}
        if select not in key_field:
            print("해당 사항이 없습니다. 다시 입력하세요.")
            continue

        key = key_field[select]
        print("정렬 알고리즘 선택:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        if key == '성적':
            print("4. 기수 정렬")

        select_algo = input("알고리즘을 선택하세요 (1,2,3,4): ")

        if select_algo == '1':
            selection_sort(students, key)
        elif select_algo == '2':
            insertion_sort(students, key)
        elif select_algo == '3':
            students = quick_sort(students, key)
        elif select_algo == '4' and key == '성적':
            radix_sort(students, key)
        #입력예외처리
        else:
            print("해당 사항이 없습니다. 다시 입력하세요.")
            continue

        print("\n 정렬된 학생 정보")
        print_students(students)

if __name__ == "__main__":
    main()
