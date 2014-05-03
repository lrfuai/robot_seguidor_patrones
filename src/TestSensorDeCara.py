from SensorDeCara import SensorDeCara
sensorCara = SensorDeCara()
exit = True
while exit : 
    sensorCara.capturar()
    exit = sensorCara.showInWindow()