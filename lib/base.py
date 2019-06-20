import abc


class AbcTest(metaclass=abc.ABCMeta):

    channel = 0
    interval = None
    send_times = 1
    timeout = 0

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def set_parameters(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass


    @abc.abstractmethod
    def report(self):
        pass

    @abc.abstractmethod
    def loop(self):
        pass

class BaseTest(AbcTest):
    """测试基类"""
    
    device = None

    def __init__(self, channel, data, timeout):
        self.channel = channel
        self.data = data
        self.timeout = timeout
        

