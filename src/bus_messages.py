
import ctypes
import random


class AIRCRAFT_1_HT_ESCM_DAC(ctypes.Structure):
    _fields_ = [
        ("dyntag", ctypes.c_uint, 1),
        ("pulse_width", ctypes.c_uint, 10), # bits
        ("amplitude", ctypes.c_uint, 8),
        ("PRI", ctypes.c_uint, 6),
        ("frequency", ctypes.c_uint, 7),
    ]
    def randomize(self):
        """Assigns random positive values to each field within their allowed ranges."""
        for field_name, field_type, field_bits in self._fields_:
            max_value = (2**field_bits) - 1  # Calculate max value based on bit width
            setattr(self, field_name, random.randint(0, max_value))
