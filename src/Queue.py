import queue

class ProcessQueue:
    def __init__(self, priority, scheduling_algorithm):
        self.priority = priority
        self.scheduling_algorithm = scheduling_algorithm
        self.waiting_processes = queue.PriorityQueue()
        self.completed = []
        
    def fifo(self):
        pqueue = queue.PriorityQueue()
        curr_time = 0
        while True:
            curr_proc = self.waiting_processes[0]
            curr_proc.set_first_run(curr_time)
            curr_time += 1
            