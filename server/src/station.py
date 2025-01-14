from ble import BLE
from beacon import Beacon
from location import Location


class Station(BLE):
    def __init__(self, name: str, mac: str, manufecturer: str,
                 location: Location):
        super().__init__(name, mac, manufecturer)
        self._beacons_found: dict = {}
        self._location = location

    @staticmethod
    def parse(msg: dict):
        if msg is None:
            raise NotImplementedError()

        station_attributes = list(vars(BLE).keys()) + \
            list(vars(Station).keys())
        msg_attributes = msg.keys()

        is_station = True
        for atrribute in msg_attributes:
            if atrribute not in station_attributes:
                is_station = False
                break

        if is_station:
            station = Station(msg['name'], 
                         msg['mac'],
                         msg['manufacturer'],
                         Location(msg['location']['x'], msg['location']['y']))

            for item in msg['beacons_found']:
                if (item['name'].startswith('ESP32')):
                    continue
                
                station.add_beacon(Beacon(
                    item['name'], 
                    item['mac'], 
                    item['manufacturer'],
                    item['rssi'], 
                    item['tx_power']))

            return station
        else:
            return None

    def add_beacon(self, beacon: Beacon):
        self._beacons_found[beacon.mac] = beacon

    @property
    def beacons_found(self):
        return self._beacons_found

    @property
    def location(self) -> Location:
        return self._location

    def __str__(self):
        # return f'Station: {self._name} MAC: {self._mac} Location: {self._location}'
        return f'Station: {self._name} Location: {self._location}'
