""" My Simpy Extension """

import simpy

# MonitoredResource
# Extend Simpy's resource with queue length and utilization monitoring
class MonitoredResource(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super(MonitoredResource, self).__init__(*args, **kwargs)
        self.data = []

    def checkBusy(self, q0, u0, q1, u1):
        busy = u1
        if q0 > 0 or q1 > 0:
            busy = u0
        return busy

    def request(self, *args, **kwargs):
        now = self._env.now
        q0 = len(self.queue)
        u0 = self.count
        r = super(MonitoredResource, self).request(*args, **kwargs)
        q1 = len(self.queue)
        u1 = self.count
        self.data.append((now, self.checkBusy(q0, u0, q1, u1), q1))
        return r

    def release(self, *args, **kwargs):
        now = self._env.now
        q0 = len(self.queue)
        u0 = self.count
        r = super(MonitoredResource, self).release(*args, **kwargs)
        q1 = len(self.queue)
        u1 = self.count
        if q0 == q1 > 0:
            q1 -= 1
        self.data.append((now, self.checkBusy(q0, u0, q1, u1), q1))
        return r

"""
    @property
    def currentStats


class SamplingMonitor(simpy.Process):
    def __init__(self, res, frequency):
        self.resource = res
        self.freq = frequency
        self.data = []

    def on(self):
        res.data
"""