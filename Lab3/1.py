class student:
    def __init__(self, input_string) -> None:
        info = input_string.split()
        self.name = info[0]
        self.final_grade = int(info[1])
        self.evaluate_grade = int(info[2])
        self.is_leader = True if info[3] == "Y" else False
        self.is_westStu = True if info[4] == "Y" else False
        self.paper = int(info[5])
        self.scholarship = 0
    def cal_scholarship(self):
        if self.final_grade > 80 and self.paper >= 1:
            self.scholarship += 8000
        if self.final_grade > 85 and self.evaluate_grade > 80:
            self.scholarship += 4000
        if self.final_grade > 90:
            self.scholarship += 2000
        if self.final_grade > 85 and self.is_westStu:
            self.scholarship += 1000
        if self.evaluate_grade > 80 and self.is_leader:
            self.scholarship += 850

n = int(input())
arr = []
total = 0
for i in range(n):
    stu = student(input())
    stu.cal_scholarship()
    total += stu.scholarship
    arr.append(stu)

arr.sort(key=lambda x: x.scholarship,reverse=True)

print(arr[0].name)
print(arr[0].scholarship)
print(total)