import pifacecad
cad = pifacecad.PiFaceCAD()
listener = pifacecad.InputEventListener(chip=cad)
listener.register(0, pifacecad.IODIR_RISING_EDGE, print)
listener.activate()