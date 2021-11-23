def printList():
 for i in range(len(names)):
   print(names[i] + ', ' + ipaddress[i] + ', ' + networkaddress[i] + ', ' + gateway[i] + ', ' + devices[i] + ', ' + models[i] + ', ')

names = ['Thomas', 'Geraldine']
ipaddress = ['192.168.48.22', '192.168.48.44']
networkaddress= ['192.168.48.00/24', '192.168.48.00/24']
gateway = ['192.168.48.1', '192.168.48.1']
devices= ['Dell', 'Hp']
models = ['optiplex5050', 'pc7900']

printList()

newName = input('Enter a Name:')
names.append(newName)
newIpAddress= input('Enter a Ip Address:')
ipaddress.append(newIpAddress)
newNetworkaddress = input('Enter a Networkaddress:')
networkaddress.append(newNetworkaddress)
newGateway = input('Enter a Gateway:')
gateway.append(newGateway)
newDevices = input('Enter a Device:')
devices.append(newDevices)
newModels = input('Enter a Model:')
models.append(newModels)
printList()
printList()
