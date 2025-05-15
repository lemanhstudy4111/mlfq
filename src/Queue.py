import queue

class MyQueue:
    def __init__(self, type):
        self.type = type
        self.queue = None
        if type == "duration" or type == "arrival":
            self.queue = queue.PriorityQueue()
        else:
            self.queue = queue.Queue()
    
        
    def enqueue(self, process):
        if self.type == "duration":
            self.queue.put((process.duration, process))
        elif self.type == "arrival":
            self.queue.put((process.arrival, process))
        else:
            self.queue.put(process)
        return

    def peek(self):
        return self.queue.queue[0]

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop()[1]
    
    def isEmpty(self):
        if len(self.queue.queue) == 0:
            return True
        return False

    def init_queue(self, workload):
        for work in workload:
            self.enqueue(work)
        return
            
class ProcessQueue:
    def __init__(self, priority, scheduling_algorithm):
        self.priority = priority
        self.scheduling_algorithm = scheduling_algorithm
        self.waiting_processes = []
        self.completed = []
        
    def fifo(self):
        completed = []
        curr_time = 0
        for process in self.waiting_processes:
            process.set_first_run(curr_time)
            process.set_finish(curr_time + process.duration)
            completed.append(process)
        return completed
    
    def sjf(self):
        completed = []
        temp_workload = MyQueue("arrival")
        temp_workload.init_queue(self.waiting_processes)
        arrived = MyQueue("duration")
        curr_time = 0
        curr_proc = None
        while not temp_workload.isEmpty() or not arrived.isEmpty():
            while not temp_workload.isEmpty() and temp_workload.peek().get_arrival() <= curr_time:
                p = temp_workload.dequeue()
                arrived.enqueue(p)
            if not arrived.isEmpty():
                curr_proc = arrived.dequeue()
                curr_proc.set_first_run(curr_time)
                curr_time += curr_proc.get_duration()
                curr_proc.set_finish(curr_time)
                completed.append(curr_proc)
            else:
                if not temp_workload.isEmpty():
                    curr_time = temp_workload.peek().get_arrival()
        return completed

    def stcf(self):
        completed = []
        all_workload = MyQueue("arrival")
        arrived = MyQueue("duration")
        curr_proc = None
        curr_time = 0
        while not all_workload.isEmpty() or not arrived.isEmpty():
            while not all_workload.isEmpty() and curr_time == all_workload.peek().get_arrival():
                p = all_workload.dequeue()
                arrived.enqueue(p)
            curr_proc = arrived.dequeue()
            if curr_proc.get_first_run() == -1:
                curr_proc.set_first_run(curr_time)
            if curr_proc.get_duration() <= 0:
                curr_proc.set_finish(curr_time)
                completed.append(curr_proc)
                continue
            curr_proc.set_duration(curr_proc.get_duration() - 1)
            curr_time += 1
            arrived.enqueue(curr_proc)
        return completed
    
    def rr(self):
        completed = []
        all_workload = MyQueue("arrival")
        arrived = MyQueue()
        curr_time = 0
        curr_proc = None
        while not all_workload.isEmpty() or not arrived.isEmpty():
            while not all_workload.isEmpty() and all_workload.peek().get_arrival() == curr_time:
                p = all_workload.dequeue()
                arrived.enqueue(p)
            if not arrived.isEmpty():
                curr_proc = arrived.dequeue()
                if curr_proc.get_first_run() == -1:
                    curr_proc.set_first_run(curr_time)
                curr_proc.set_duration(curr_proc.get_duration() - 1)
                if curr_proc.get_duration() <= 0:
                    curr_time += 1
                    curr_proc.set_finish(curr_time)
                    completed.append(curr_proc)
                    continue
                else:
                    arrived.enqueue(curr_proc)
            curr_time += 1
        return completed