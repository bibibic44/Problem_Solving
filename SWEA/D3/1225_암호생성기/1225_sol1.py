import sys
sys.stdin = open('input.txt')


class Queue:
    def __init__(self):
        self.data = []

    def q_enqueue(self, item):
        self.data.append(item)

    def is_empty(self):
        return not bool(self.data)

    def q_dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.data.pop(0)

    def q_rear(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

    def q_string(self):
        if self.is_empty():
            return None
        else:
            return ' '.join(map(str, self.data))

while True:
    try:
        tc = int(input())
        nums = list(map(int, input().split()))
    except:
        break

    q = Queue()
    for i in range(8):
        q.q_enqueue(nums[i])

    num = 1
    while q.q_rear() != 0:
        if num > 5:
            num = 1
        tmp = q.q_dequeue()
        tmp -= num
        num += 1
        if tmp < 0:
            tmp = 0
        q.q_enqueue(tmp)

    print('#{} {}'.format(tc, q.q_string()))
