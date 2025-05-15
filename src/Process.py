class Process:
    def __init__(self, time_arrive, duration, priority):
        self.time_arrive = time_arrive
        self.first_run = -1
        self.duration = duration
        self.finish = -1
        self.priority = priority
    
    def get_arrival(self):
        return self.time_arrive
    
    def get_first_run(self):
        return self.first_run
    
    def get_duration(self):
        return self.duration
    
    def get_finish(self):
        return self.finish
    
    def set_first_run(self, first_run):
        self.first_run = first_run
        return
    
    def set_duration(self, duration):
        self.duration = duration
        return
    
    def set_finish(self, finish):
        self.finish = finish
        return
    
    def set_priority(self, priority):
        self.priority = priority
        return