# Inheritance
class Device:
    def __init__(self):
        self.switchedOn = False

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self): 
        if self.switchedOn == True:
            return 'ON'
        else:
            return 'OFF'
        
    def __str__(self):
        return f'Switch: {self.getSwitchedOn()}'
# Task 1
class SmartPlug(Device):
    def __init__(self, consumptionRate:int):
        super().__init__()
        if consumptionRate in range(0, 151):
            self.consumptionRate = consumptionRate
        else:
            print('Incorrect consumption rate, set default rate 0.')
            self.consumptionRate = 0
    
    def toggleSwitch(self):
        super().toggleSwitch()

    def getSwitchedOn(self):
        return super().getSwitchedOn()

    def getConsumptionRate(self):
        # if self.switchedOn == True:
        return self.consumptionRate
        # else:
        #     return 0
        
    def setConsumptionRate(self, newRate:int):
        if 0 <= newRate <= 150:
            self.consumptionRate = newRate
        else:
            print('ERROR! Please enter a consumption rate between 0 to 150')
            self.consumptionRate = 0 #change

    def __str__(self):
        return f'Plug: {self.getSwitchedOn()}, Consumption: {self.getConsumptionRate()} '
# Test Task 1
def testSmartPlug():
    plug = SmartPlug(45) # Create an instance of the SmartPlug class with a consumption rate of 45
    #plug.toggleSwitch() # Toggle the status of this plug by calling its toggleSwitch method
    print(f'Switch status: {plug.getSwitchedOn()}') # Print the value of switchedOn using the appropriate accessor method
    print(f'Current Consumption Rate: {plug.getConsumptionRate()}') # Print the value of consumptionRate, set it to a new valid value (of your choice), and then print it again
    plug.setConsumptionRate(60)
    print(f'Consumption Rate Now: {plug.getConsumptionRate()}')
    print(plug) # Print the SmartPlug object

#testSmartPlug()  # -> For test Task 1

# Task 2
class SmartLight(Device):
    def __init__(self):
        super().__init__()
        self.brightness = 0
    
    def toggleSwitch(self):
        super().toggleSwitch()

    def getSwitchedOn(self):
        return super().getSwitchedOn()
    
    def getBrightness(self):
        return self.brightness
    
    def setBrightness(self, newBrightness:int):
        if 0 <= newBrightness <= 100:
            self.brightness = newBrightness
        else:
            print('Incorrect brightess value, set default brightness 0.')
            self.brightness = self.brightness
    
    def __str__(self):
        return f'Light: {self.getSwitchedOn()}, Brightness: {self.getBrightness()} '
# Test Task 2   
def testSmartLight():
    device = SmartLight() # Create an instance of your CustomDevice class
    device.toggleSwitch() # Toggle the status of this device using the toggleSwitch method
    print(f'Switch status: {device.getSwitchedOn()}') # Print the switchedOn instance variable using the appropriate accessor method
    print(f'Brightness: {device.getBrightness()}') # Print the current value of the option instance variable (from table 1). Then set it to a new value (of your choice). Next, print it again 
    device.setBrightness(100)
    print(f'Brightness: {device.getBrightness()}')
    print(device) # Print the CustomDevice object

#testSmartLight() # -> For test Task 2
# Task 3
class SmartHome:
    def __init__(self):
        self.devices = []
    
    def getDevices(self):
        return self.devices
    
    def getDeviceAt(self, index:int):
        if 0 <= index <= len(self.devices):
            device = self.devices[index]
            return device
    
    def removeDeviceAt(self, index:int):
        if 0 <= index <= len(self.devices):
           #self.devices.remove(self.devices[index])
           del self.devices[index]
           
    def addDevice(self, device:object):
        self.devices.append(device)

    def toggleSwitch(self, index:int):
        if 0 <= index <= len(self.devices):
            #self.devices[index] = not self.devices[index]
            if self.devices[index].getSwitchedOn() == 'OFF': # Here the change
                self.devices[index].toggleSwitch()
            else:
                self.devices[index].toggleSwitch()

    def turnOnAll(self):
        for index in range(len(self.devices)):
            if self.devices[index].getSwitchedOn() == 'OFF': # Here the change
                self.devices[index].toggleSwitch()

    def turnOffAll(self):
        for index in range(len(self.devices)):
            if self.devices[index].getSwitchedOn() == 'ON': # Here the change
                self.devices[index].toggleSwitch()

    def __str__(self):
        output = '\nThe devices status:'
        for index, device in enumerate(self.devices, start= 1):
            output += f'\n\nDevice {index} '
            output += f'\n{index}. {device} '
        return output

def testSmartHome():
    smartHome = SmartHome() # Create an instance of the SmartHome class and two instances of the SmartPlug class with consumption rates of 45. Additionally, create an instance of your custom device
    smartPlug_1 = SmartPlug(45)
    smartPlug_2 = SmartPlug(45)
    smartLight = SmartLight()
    smartPlug_1.toggleSwitch() # Toggle the first plug, hence turning it on. Then set its consumption rate to 150. Then, set the consumptionRate of the second plug to 25. Lastly, set the option of the custom device to a value of your choice
    smartPlug_1.setConsumptionRate(150)
    smartPlug_2.setConsumptionRate(25)
    smartLight.setBrightness(100)
    smartHome.addDevice(smartPlug_1) # Add both plugs and the custom device to the smart home object
    smartHome.addDevice(smartPlug_2)
    smartHome.addDevice(smartLight)
    smartHome.toggleSwitch(1) # Toggle the status of the second plug using the appropriate method of the smart home object
    print(smartHome) # Print the smart home object
    smartHome.turnOnAll() # Turn on all devices in the smart home and print the smart home object again
    print(smartHome)
    smartHome.removeDeviceAt(0) # Remove the first device and print the smart home
    print(smartHome)
    
#testSmartHome() # -> For test Task 3