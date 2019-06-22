import abc
import argparse


class AbcTest(metaclass=abc.ABCMeta):

    channel = 0
    interval = None
    send_times = 1
    timeout = 0

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def set_parameters(self, **kwargs):
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

    default_length = 10
    default_device = 0

    def __init__(self, passage, device=None):
        self.passage = passage
        self.device = device
        if self.device is None:
            self.device = self.default_device

    def loop(self):
        pass

    def report(self):
        pass

    @classmethod
    def get_args(self):
        return None

    @classmethod
    def run(cls, parser_args, times=1):
        testdev = cls(parser_args.passage)
        data = bytes.fromhex(parser_args.data)
        return testdev.runner(data=data, timeout=parser_args.timeout, times=times)


    def runner(self, *args, **kwargs):
        try:
            return self.tester(*args, **kwargs)
        finally:
            self.close()

    def tester(self, data, timeout, times):
        print(self.passage, self.device)
        print('timeout: ', timeout, 'ms')
        print('times: ', times)
        self.open()
        self.write(data)
        print('send: ', data)
        data = self.read(self.default_length, timeout)
        print('read:', data)
        return data

    @classmethod
    def cmd(cls):
        parser = argparse.ArgumentParser()
        parser.description = cls.__doc__
        parser.add_argument('-p', '--passage', help="待控制通道", type=int)
        parser.add_argument('-d', '--data', help="待发送数据", type=str)
        parser.add_argument('-t', '--timeout', help="返回超时时间", type=int)
        parser.add_argument('-f', '--file', help="文件名", type=int)

        args = parser.parse_args()
        # print((args.data, args.file))
        if args.passage is not None and (args.data is not None
                                         or args.file is not None):
            cls.run(args)
        else:
            parser.print_help()


    def close(self):
        self.devobj.close()

    def open(self):
        self.devobj.open(self.passage, self.device)

    def set_parameters(self, **kwargs):
        pass