from zeroconf import Zeroconf, ServiceBrowser
import time
import sys
import os

devices_num = 0
devices = {}
part2 = False
zeroconf = None
device = None
cur_name = None

class ds:
    def remove_service(self, zeroconf, type, name):
        global devices_num
        global part2
        global device
        global devices
        global cur_name
        if device is not None:
            if name == cur_name:
                sys.stdout.write(f"\rDevice status: ⡢⡂ offline ")
                sys.stdout.flush()
            return
        if part2:

            if any(name in sublist for sublist in devices.values()):
                part2 = False
                foundDevice(name)
    def add_service(self, zeroconf, type, name):
        global devices_num
        global device
        global cur_name        
        info = zeroconf.get_service_info(type, name)
        if info:
            ip = info.parsed_addresses()[0]
            if ip not in devices.keys():
                devices[ip] = [name]
            else:
                devices[ip].append(name)
                devices_num += 1
            if device:
                if info.parsed_addresses()[0] == device: 
                    cur_name = name
                    sys.stdout.write(f"\rDevice status: ⢄⠔ online ")
                    sys.stdout.flush()
    def update_service(self, zeroconf, type, name):
        pass

class ts:
    def __init__(self, zc):
        self.zc = zc
        self.svc = {}
    def remove_service(self, zeroconf, type, name):
        if name in self.svc:
            self.svc[name].cancel()
            del self.svc[name]
    def add_service(self, zeroconf, type, name):
        if name not in self.svc:
            self.svc[name] = ServiceBrowser(self.zc, name, ds())
    def update_service(self, zeroconf, type, name):
        pass

def start_zc():
    global devices_num
    global zeroconf
    global part2
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    zeroconf = Zeroconf()
    type_listener = ts(zeroconf)
    browser = ServiceBrowser(zeroconf, "_services._dns-sd._udp.local.", type_listener)
    spinner = [
        "⣏⣸","⣏⣱","⣏⣩","⣏⣙","⣏⡹","⣏⢹",
        "⡏⣹","⢏⣹","⣋⣹","⣍⣹","⣎⣹","⣇⣹"
        ]
    spinner.extend(spinner)
    spinner.extend(spinner)
    for i in spinner:
        sys.stdout.write(f"\r{i} Searching for your device. Make sure it is open/unlocked. {devices_num} devices found")
        sys.stdout.flush()
        time.sleep(0.2)
    if devices_num > 0:
        sys.stdout.write("\rNow close/lock your device.                                                               ")
        sys.stdout.flush()
    part2 = True
    while True:
        time.sleep(20)
def foundDevice(d):
    global device
    global devices
    for i, j in devices.items():
        if d in j:
            device = i
    sys.stdout.write(f"\rFound device: {d} (IP {device})\n")
    sys.stdout.flush()
    sys.stdout.write(f"\rDevice status: ⡢⡂ offline ")
    sys.stdout.flush()

start_zc()
