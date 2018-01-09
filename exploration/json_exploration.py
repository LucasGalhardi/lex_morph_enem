import json

#class definition for vm object
class vm:
    def __init__(self,name,state):
        self.disk=[]
        self.name=name
        self.state=state
    def addDisk(self,d):
        self.disk.append(d)

#function to create a vm object from serialized dictionary data
def as_vm(vmdict):
    newvm=vm(vmdict['name'],vmdict['state'])
    for d in vmdict['disk']:
        newvm.addDisk(d)
    return newvm

#create some VMs and add them to a list
vmlist= []
myvm=vm('server1','running')
myvm.addDisk(1000)
myvm.addDisk(2500)
vmlist.append(myvm)

myvm=vm('server2','stopped')
myvm.addDisk(500)
myvm.addDisk(2000)
vmlist.append(myvm)

#show vm info
for myvm in vmlist:
    print (myvm.name + " - " + myvm.state + " - disks: " + str(myvm.disk))

#create list of vm dictionaries
vmdictlist= []
for myvm in vmlist:
    vmdictlist.append(myvm.__dict__)

#convert dictionary list to json
jsondata=json.dumps(vmdictlist)
print ("objects serialized: " + jsondata)

#later - convert json into vm objects again
newvmlist=json.loads(jsondata, object_hook=as_vm)

#show vm info
for myvm in newvmlist:
    print(myvm.name + " - " + myvm.state + " - disks: " + str(myvm.disk))

