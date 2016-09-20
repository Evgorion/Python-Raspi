import subprocess
import pifacecad
import sys

PY3 = sys.version_info[0] >= 3
if not PY3:
    print("Weather only works with `python3`.")
    sys.exit(1)

GET_LIST_CMD = "ls -la"
GET_IP_CMD = "hostname --all-ip-addresses"
GET_TEMP_CMD = "/opt/vc/bin/vcgencmd measure_temp"
TEMP_SYMBOL = pifacecad.LCDBitmap([0x4, 0x4, 0x4, 0x4, 0xe, 0xe, 0xe, 0x0])
WIND_SYMBOL = pifacecad.LCDBitmap([0x0, 0xf, 0x3, 0x5, 0x9, 0x10, 0x0])
TEMP_SYMBOL_INDEX, WIND_SYMBOL_INDEX = 0, 1

cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.write("Hello Raspi!\n")


def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

def get_my_ip():
    return run_cmd(GET_IP_CMD) #[:-1]

def get_my_temp():
    return run_cmd(GET_TEMP_CMD)[5:9]

list = run_cmd(GET_LIST_CMD)
print(list)

#cad.lcd.write("IP:{}\n".format(get_my_ip()))
#cad.lcd.write(":{}C ".format(get_my_temp()))
cad.lcd.store_custom_bitmap(TEMP_SYMBOL_INDEX, TEMP_SYMBOL)

cad.lcd.blink_off()
cad.lcd.cursor_off()


