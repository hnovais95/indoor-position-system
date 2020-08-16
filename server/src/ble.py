class BLE:
    def __init__(self, name: str, mac: str, manufecturer: str,
                 rssi: int = None, tx_power: int = None):
        self._name = name
        self._mac = mac
        self._manufecturer = manufecturer
        self._rssi = rssi
        self._tx_power = tx_power

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value

    @property
    def manufecturer(self):
        return self._manufecturer

    @manufecturer.setter
    def manufecturer(self, value):
        self._manufecturer = value

    @property
    def rssi(self):
        return self._rssi

    @rssi.setter
    def rssi(self, value):
        self._rssi = value

    @property
    def tx_power(self):
        return self._tx_power

    @tx_power.setter
    def tx_power(self, value):
        self._tx_power = value

    def __str__(self):
        return f'Name: {self._name}\nMAC: {self._mac}\nManufecturer: {self._manufecturer}'
