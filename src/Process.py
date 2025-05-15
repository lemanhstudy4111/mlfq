class Process:
    def __init__(self, time_arrive, duration):
        self.time_arrive = time_arrive
        self.first_run = -1
        self.duration = duration
        self.finish = -1
        self.priority = -1
    
    def set_first_run(self, first_run):
        self.first_run = first_run
        return
    
    def set_finish(self, finish):
        self.finish = finish
        return
    
    def set_priority(self, priority):
        self.priority = priority
        return