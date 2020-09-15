"""

    共享内存通信

"""

from multiprocessing import Array,Process
from random import randint
import time


val = Array('i', 5)
