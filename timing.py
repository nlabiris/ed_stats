import time

class Timing:
    start_time: int
    stop_time:int
    elapsed_time: int

    def startTimingExecution(self):
        self.start_time = time.time()

    def stopTimingExecution(self, prefix="###"):
        self.stop_time = time.time()
        elapsed_seconds = self.stop_time - self.start_time

        mins = elapsed_seconds // 60
        elapsed_seconds = elapsed_seconds % 60
        hours = mins // 60
        mins = mins % 60
        print("{0} - Time elapsed: {1} hour(s), {2} minute(s), {3} second(s)".format(prefix, int(hours), int(mins), elapsed_seconds))

