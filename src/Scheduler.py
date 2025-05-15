class Scheduler:
    def __init__(self, num_queues=3, sched_algs=[("rr", 16), ("rr", 16), ("fifo", None)]):
        self.num_queues = num_queues
        self.sched_algs = sched_algs
        pass