from functools import partial
from multiprocessing.pool import Pool


class Parallel:
    """This class has methods for executing functions in parallel
    using threads for concurrency, or a multiprocessing pool for
    true parallel execution."""

    def __init__(self, num_processes=8):
        self.num_processes = num_processes

    def execute_parallel(self, function, targets, *args, **kwargs):
        with Pool(self.num_processes) as p:
            p.map(partial(function, *args, **kwargs), targets)
