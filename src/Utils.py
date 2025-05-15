from Process import Process
class Utils:
    def read_workload(filename):
        """
        workload file format:
        arrive duration priority
        """
        res = []
        with open(filename, "r") as f:
            for line in f:
                arrive, duration, priority = line.split()
                new_proc = Process(time_arrive=arrive, duration=duration, priority=priority)
                res.append(new_proc)
        return res