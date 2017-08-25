import fauxmo
import sys

class onkyo_command_handler(object):
    def __init__(self, device):
        self.device = device
        self.onkyo_command_path = '/home/pi/onkyo-remote/onkyo-iscp/onkyo-iscp'
        self.onkyo_ip = '10.0.0.29'
        
    def on(self):
        status = 0
        if self.device == "Playstation":
            status += subprocess.call([self.onkyo_command_path, self.onkyo_ip, "SLI", "10"])
            status += subprocess.call([self.onkyo_command_path, self.onkyo_ip, "MVL", "0F"])
        elif self.device == "X1":
            status += subprocess.call([self.onkyo_command_path, self.onkyo_ip, "SLI", "01"])
            status += subprocess.call([self.onkyo_command_path, self.onkyo_ip, "MVL", "0F"])
        elif self.device == "turntable":
            status += subprocess.call([self.onkyo_command_path, self.onkyo_ip, "SLI", "23"])
            status += subprocess.call([self.onkyo_command_path, self.onkyo_ip, "MVL", "1E"])
        return True

    def off(self):
        status = subprocess.call([self.onkyo_command_path, self.onkyo_ip, "PWR", "00"])
        return True

debug = False

if len(sys.argv) > 1 and sys.argv[1] == '-d':
    debug = True

fauxmos = [
    ['playstation', onkyo_command_handler("Playstation"), 9091],
    ['x1', onkyo_command_handler("X1"), 9092],
    ['turntable', onkyo_command_handler("turntable"), 9093]
]

fauxmo.start_fauxmo(fauxmos, debug)
