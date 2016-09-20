import subprocess
import threading
import pifacecad
import sys

DATATIME = "date +%Y-%m-%d_%H.%M.%S"

BASEPATH = "/media/pi/boot/video"

COPYPATH='/home/pi/google_drive'

CAM1 = "cam1"
CAM2 = "cam2"
CAM3 = "cam3"
CAM4 = "cam4"

cam1_name = ""
cam2_name = ""
cam3_name = ""
cam4_name = ""

CAM1_PATH = BASEPATH + "/" + CAM1
CAM2_PATH = BASEPATH + "/" + CAM2
CAM3_PATH = BASEPATH + "/" + CAM3
CAM4_PATH = BASEPATH + "/" + CAM4

CAM1_IP = "rtsp://10.0.0.204:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream"
CAM2_IP = "rtsp://10.0.0.202:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream"
CAM3_IP = "rtsp://10.0.0.200:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream"
CAM4_IP = "rtsp://10.0.0.201:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream"

OPEN_RTSP = "openRTSP -D 1 -B 10000000 -b 10000000 -4 -d 60 "

CAM1_COMMAND = OPEN_RTSP + CAM1_IP + " > " + CAM1_PATH
CAM2_COMMAND = OPEN_RTSP + CAM2_IP + " > " + CAM2_PATH
CAM3_COMMAND = OPEN_RTSP + CAM3_IP + " > " + CAM3_PATH
CAM4_COMMAND = OPEN_RTSP + CAM4_IP + " > " + CAM4_PATH

cam1_com_path = ""
cam2_com_path = ""
cam3_com_path = ""
cam4_com_path = ""

cam1_com_path_new = ""
cam2_com_path_new = ""
cam3_com_path_new = ""
cam4_com_path_new = ""



def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')


def file_name():
    global cam1_name
    global cam2_name
    global cam3_name
    global cam4_name
    global cam1_com_path
    global cam2_com_path
    global cam3_com_path
    global cam4_com_path
    global cam1_com_path_new
    global cam2_com_path_new
    global cam3_com_path_new
    global cam4_com_path_new
    date = run_cmd(DATATIME)
    cam1_name = CAM1 + "-" + date.strip() + ".avi"
    cam2_name = CAM2 + "-" + date.strip() + ".avi"
    cam3_name = CAM3 + "-" + date.strip() + ".avi"
    cam4_name = CAM4 + "-" + date.strip() + ".avi"

    cam1_com_path = CAM1_COMMAND + "/" + cam1_name
    cam2_com_path = CAM2_COMMAND + "/" + cam2_name
    cam3_com_path = CAM3_COMMAND + "/" + cam3_name
    cam4_com_path = CAM4_COMMAND + "/" + cam4_name
    #cam1_com_path_new = "/home/user/work/save-cam1-all.sh &"
    #cam2_com_path_new = "/home/user/work/save-cam2-all.sh &"
    #cam3_com_path_new = "/home/user/work/save-cam3-all.sh &"
    #cam4_com_path_new = "/home/user/work/save-cam4-all.sh &"

def show_sysinfo(text):
    cad = pifacecad.PiFaceCAD()  # create PiFace Control and Display object
    cad.lcd.clear()
    cad.lcd.blink_off()
    cad.lcd.cursor_off()
    cad.lcd.backlight_on()  # turns the backlight on
    cad.lcd.write(text)  # writes hello world on to the LCD


def video_save():
    #t1 = threading.Thread(target=run_cmd, args=(cam1_com_path_new,))
    #t2 = threading.Thread(target=run_cmd, args=(cam2_com_path_new,))
    #t3 = threading.Thread(target=run_cmd, args=(cam3_com_path_new,))
    #t4 = threading.Thread(target=run_cmd, args=(cam4_com_path_new,))

    t1 = threading.Thread(target=run_cmd, args=(cam1_com_path,))
    t2 = threading.Thread(target=run_cmd, args=(cam2_com_path,))
    t3 = threading.Thread(target=run_cmd, args=(cam3_com_path,))
    t4 = threading.Thread(target=run_cmd, args=(cam4_com_path,))
    show_sysinfo("File save START!")
    t1.start()
    #show_sysinfo("CAM1 save file")
    t2.start()
    #show_sysinfo("CAM2 save file")
    t3.start()
    #show_sysinfo("CAM3 save file")
    t4.start()
    #show_sysinfo("CAM4 save file")
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    show_sysinfo("File save end!")

    #run_cmd(cam1_com_path)
    #run_cmd(cam2_com_path)
    #run_cmd(cam3_com_path)
    #run_cmd(cam4_com_path)


def update_pin_text(event):
    event.chip.lcd.set_cursor(13, 0)
    event.chip.lcd.write(str(event.pin_num))
    if event.pin_num == 0:
        video_save()
    #elif event.pin_num == 1:

    #print(event.pin_num)

def start_button():
    cad = pifacecad.PiFaceCAD()
    cad.lcd.write("You pressed: ")
    listener = pifacecad.SwitchEventListener(chip=cad)
    for i in range(8):
        # print(i)
        listener.register(i, pifacecad.IODIR_FALLING_EDGE, update_pin_text)
    listener.activate()



def main():
    file_name()
    show_sysinfo("FOR START push BUTTON")
    start_button()
    #video_save()
    #show_sysinfo("Start save file")
    #print(cam1_name)
    #print(cam2_name)
    #print(cam3_name)
    #print(cam4_name)
    #print(CAM1_PATH)
    #print(CAM2_PATH)
    #print(CAM3_PATH)
    #print(CAM4_PATH)
    #print(cam1_com_path)
    #print(cam2_com_path)
    #print(cam3_com_path)
    #print(cam4_com_path)


if __name__ == '__main__':
    main()

