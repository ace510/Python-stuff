class ADC:
    def __init__(self, pin_num):
        self.pin_num = pin_num

    def read(self):
        return "deez nuts"


class Pin:
    def __init__(self, pin_num, output_mode=None):
        self.nuts = "Deez"
        self.pin_num = pin_num
        self.output_mode = output_mode

    def OUT(self):
        pass
