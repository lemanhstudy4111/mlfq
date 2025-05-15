from Process import Process
class Utils:
    def read_workload(filename):
        """
        workload file format:
        arrive duration
        """
        res = []
        with open(filename, "r") as f:
            for line in f:
                arrive, duration = line.split()
                new_proc = Process(time_arrive=arrive, duration=duration)
                res.append(new_proc)
        return res