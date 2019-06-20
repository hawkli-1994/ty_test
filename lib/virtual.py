from .base import BaseTest

class Virtual(BaseTest):
    """虚拟的测试，用于流程测试"""

    def __init__(self, channel, data, timeout):
        return super().__init__(channel, data, timeout)

    def read(self):
        return bytes.






if __name__ == "__main__":
    pass