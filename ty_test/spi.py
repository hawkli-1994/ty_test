import spidev
from .base import BaseTest


class SpiTest(BaseTest):
    """SPI测试"""

    devobj = spidev.SpiDev()
    default_device = 1

    def read(self, length, timeout):
        data = self.devobj.readbytes(length)
        return data

    def write(self, data):
        self.devobj.xfer(data)


if __name__ == "__main__":
    SpiTest.cmd()
