class PriorityQueue:

    def __init__(self):
        self.queue = list()
        pass

    def is_empty(self):
        if self.queue == None:
            print(False)
        else :
            print(True)

    # push 기능
    def put(self, data):
        if self.queue == []:
            self.queue.append(data)
        else:
            current = 0
            for i in self.queue:
                if data[0] > i[0]:
                    current+=1
            self.queue.insert(current,data)

    # pop 기능
    def get(self):
        if self.queue == []:
            return None
        else:
            return self.queue.pop()

    # Priority Queue 데이터 출력
    def peek(self):
        if self.queue == []:
            print(None)
        else:
            print(self.queue)


pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())