from tkinter import *
from backend import *

def setUpHome():
    smartHome = SmartHome()
    print('\nWelcome to Smart Home Setup!!!')
    for i in range(5):
        option = int(input('\nPlease enter 1 to add SmartPlug device or 2 to add SmartLight device: '))
        while option != 1 and option != 2:
            option = int(input('ERROR! Enter 1 or 2 to add SmartPlug or SmartLight: '))
        if option == 1:
            consumptionRate = int(input('Enter a consumption Rate (0 - 150 included): '))
            plugDevice = SmartPlug(consumptionRate)
            smartHome.addDevice(plugDevice)
            print('Smart Plug ADDED!!!')
        else:
            brightness = int(input('Enter a brightness (0 - 100 included): '))
            lightDevice = SmartLight()
            lightDevice.setBrightness(brightness)
            smartHome.addDevice(lightDevice)
            print('Smart Light ADDED!!!')
    return smartHome
#setUpHome() -> To check if my setUpHome is workin

class SmartHomeSystem:
    def __init__(self, smartHome):
        self.smartHome = smartHome
        self.devices = self.smartHome.getDevices()
        self.win = Tk()
        self.win.title('Smart Home System')
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(column = 0, row = 0, padx = 10, pady = 10)
        self.listDevices = [] # List all the devices
    def run(self):
        self.createWidget()
        self.win.mainloop()
    ######### Main Window #########
    def createWidget(self):
        self.deleteAllWidgets()
        ######### TURN ON ALL #########
        turnOnAll = Button(
            self.mainFrame,
            width = 10,
            text = 'Turn On all',
            command = self.turnOnAll
        )
        turnOnAll.grid(column = 0, row = 0, sticky = 'W')
        ######### TURN OFF ALL #########        
        turnOffAll = Button(
            self.mainFrame,
            width = 10,
            text = 'Turn Off all',
            command = self.turnOffAll
        )
        turnOffAll.grid(column = 1, row = 0)

        for index in range(len(self.devices)):
            ######### Label for each device inside the list #########
            smartDevices = Label(
                self.mainFrame,
                text = self.smartHome.getDeviceAt(index)
            )
            smartDevices.grid(column= 0, row = 10 + index, pady = 2, sticky = 'W')
            self.listDevices.append(smartDevices)
            ######### Toggle Button #########
            toggleDevice = Button(
                self.mainFrame,
                text = 'Toggle',
                command = lambda idx = index: self.switchToggle(idx)
            )
            toggleDevice.grid(column = 1, row = 10 + index)
            self.listDevices.append(toggleDevice)
            ######### Edit Button #########
            editDevice = Button(
                self.mainFrame,
                text = 'Edit',
                command = lambda idx = index: self.newWinEdit(idx)
            )
            editDevice.grid(column = 2, row = 10 + index)
            self.listDevices.append(editDevice)
            ######### Delete Buto #########
            deleteDevice = Button(
                self.mainFrame,
                text = 'Delete',
                command = lambda idx = index: self.deleteDevice(idx)
            )
            deleteDevice.grid(column = 3, row= 10 + index, padx = 5)
            self.listDevices.append(deleteDevice)
        ######### Add Button #########
        add = Button(
            self.mainFrame,
            width = 10,
            text = 'Add',
            command = lambda: self.newWinAdd()
        )
        add.grid(column = 0, row = 60)

    def deleteAllWidgets(self): # Update the list
        for device in self.listDevices:
            device.destroy()
        self.listDevices = []
   
    def deleteDevice(self, index): # Remove the devise to the list
        self.smartHome.removeDeviceAt(index)
        self.createWidget()
     
    def switchToggle(self, index):
        self.smartHome.toggleSwitch(index)
        self.createWidget()

    def turnOnAll(self):
        self.smartHome.turnOnAll()
        self.createWidget()

    def turnOffAll(self):
        self.smartHome.turnOffAll()
        self.createWidget()
    ######### Edit Window #########
    def newWinEdit(self, index):
        newWin = Toplevel(self.win)
        newWin.geometry('400x120')
        newWin.title(f'Edit Your Device {index + 1}')
        newWinFrame = Frame(newWin)
        newWinFrame.grid(padx = 10, pady = 10)
        self.editConsumption = IntVar()
        self.editBright = IntVar()
        self.editConsumption.set(0)
        self.editBright.set(0)

        textEdit = Label(
            newWinFrame,
            text = 'Edit the Device:'
        )
        textEdit.grid(column = 0, row = 0, sticky = 'W')

        smartPlug = Button(
            newWinFrame,
            text = 'Smart Plug',
            command = lambda idx = index: self.updateSmartPlug(idx, newWin)
        )
        smartPlug.grid(column = 0, row = 1)

        smartLight = Button(
            newWinFrame,
            text = 'Smart Light',
            command = lambda idx = index: self.updateSmartLight(idx, newWin)
        )
        smartLight.grid(column = 0, row = 2)

        textConsumption = Label(
            newWinFrame,
            text = 'Consumption:'
        )
        textConsumption.grid(column = 1, row = 1)

        enterConsumption = Entry(
            newWinFrame,
            width = 15,
            text = self.editConsumption
        )
        enterConsumption.grid(column = 2, row = 1)

        textBright = Label(
            newWinFrame,
            text = 'Brightess:'
        )
        textBright.grid(column = 1, row = 2, sticky = 'E')

        enterBright = Entry(
            newWinFrame,
            width = 15,
            text = self.editBright
        )
        enterBright.grid(column = 2, row = 2)

        cancelButton = Button(
            newWinFrame,
            text = 'Cancel',
            command = lambda: self.cancelWin(newWin)
        )
        cancelButton.grid(column = 2, row = 3)

    def cancelWin(self, newWin):
        newWin.destroy()

    def updateSmartPlug(self, index, newWin):
        device = self.smartHome.getDeviceAt(index)
        newConsumptionRate = self.editConsumption.get()

        if not isinstance(device, SmartPlug): # If is NOT a smartPlug
            if newConsumptionRate: # Check if there is a value inside the entry
                if not 0 <= newConsumptionRate <= 150:
                    newConsumptionRate = 0
            updateDevice = SmartPlug(newConsumptionRate)
            self.smartHome.getDevices()[index] = updateDevice  
        else:
            if newConsumptionRate:
                if not 0 <= newConsumptionRate <= 150:
                    newConsumptionRate = 0
            device.setConsumptionRate(newConsumptionRate)
        newWin.destroy()  # Close the editing window
        self.createWidget()  # Update the widget to reflect the changes

    def updateSmartLight(self, index, newWin):
        device = self.smartHome.getDeviceAt(index)
        newBrightness = self.editBright.get()

        if not isinstance(device, SmartLight):
            if newBrightness:
                if not 0 <= newBrightness <= 100:
                    newBrightness = 0
            updateDevice = SmartLight()
            updateDevice.setBrightness(newBrightness)
            self.smartHome.getDevices()[index] = updateDevice
        else:
            if newBrightness:
                if not 0 <= newBrightness <= 100:
                    newBrightness = 0 # change
            device.setBrightness(newBrightness)
        newWin.destroy()  # Close the editing window
        self.createWidget()  # Update the widget to reflect the changes
    ######### Add window #########
    def newWinAdd(self):
        newWin = Toplevel(self.win)
        newWin.geometry('400x120')
        newWin.title('Add Your Device')
        newWinFrame = Frame(newWin)
        newWinFrame.grid(padx = 10, pady = 10)
        self.addConsumption = IntVar()
        self.addBright = IntVar()
        self.addConsumption.set(0)
        self.addBright.set(0)

        textEdit = Label(
            newWinFrame,
            text = 'Add a Device:'
        )
        textEdit.grid(column = 0, row = 0, sticky = 'W')

        smartPlug = Button(
            newWinFrame,
            text = 'SmartPlug',
            command = lambda: self.addDevice(SmartPlug(self.addConsumption.get()), newWin) 
        )
        smartPlug.grid(column = 0, row = 1)

        smartLight = Button(
            newWinFrame,
            text = 'Smart Light',
             command=lambda: self.addDeviceLight(newWin)
        )
        smartLight.grid(column = 0, row = 2)

        textConsumption = Label(
            newWinFrame,
            text = 'Consumption:'
        )
        textConsumption.grid(column = 1, row = 1)

        enterConsumption = Entry(
            newWinFrame,
            width = 15,
            text = self.addConsumption
        )
        enterConsumption.grid(column = 2, row = 1)

        textBright = Label(
            newWinFrame,
            text = 'Brightess:'
        )
        textBright.grid(column = 1, row = 2, sticky = 'E')

        enterBright = Entry(
            newWinFrame,
            width = 15,
            text = self.addBright,
        )
        enterBright.grid(column = 2, row = 2)

        cancelButton = Button(
            newWinFrame,
            text = 'Cancel',
            command = lambda: self.cancelWin(newWin)
        )
        cancelButton.grid(column = 2, row = 3)

    def addDevice(self, newdevice, newWin): # For the smartPlug only
        self.smartHome.addDevice(newdevice)
        newWin.destroy()
        self.createWidget()
    
    def addDeviceLight(self, newWin): # For the smartLight only
        newDevice = SmartLight()
        newDevice.setBrightness(self.addBright.get())
        self.smartHome.addDevice(newDevice)
        newWin.destroy()  # Close the add window
        self.createWidget()  # Update the widget to reflect the changes

def main():
    smartHome = setUpHome()
    smartHomeSystem = SmartHomeSystem(smartHome)
    smartHomeSystem.run()

main()