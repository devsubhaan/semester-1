# Week 1.2, Session 2: Task 6
import datetime

temp = int(input("Enter the machines temperature (Degrees): "))
pressure = int(input("Enter the machines pressure (PSI): "))
status = int(input("Enter the machines operational status (1 for operating, 0 for stopped): "))
result = "*"*26 + '\n' + str(datetime.datetime.now()) + '\n'
result += f"Temperature: {temp}" + '\n'
result += f"Pressure: {pressure}" + '\n'
result += f"Status: {status}" + '\n'

highTemp = False
if temp > 80:
    highTemp = True
    print("The temperature is too high! Shutdown is recommended.")
    result += "The temperature is too high! Shutdown is recommended." + '\n' 
elif 50 <= temp <= 80:
    print("The temperature is within safe limits.")
    result += "The temperature is within safe limits." + '\n' 
else:
    print("The temperature is low, no action is needed.")
    result += "The temperature is low, no action is needed." + '\n' 

highPressure = False
if pressure > 100:
    highPressure = True
    print("High pressure detected! Maintenance is recommended.")
    result += "High pressure detected! Maintenance is recommended." + '\n' 
elif 70 <= pressure <= 100:
    print("Pressure is stable.")
    result += "Pressure is stable." + '\n' 
else:
    print("Pressure is low, system is operating normally.")
    result += "Pressure is low, system is operating normally." + '\n' 

if status == 1 and (highPressure or highTemp):
    print("The machine is running in unsafe conditions, shutdown recommended!")
    result += "The machine is running in unsafe conditions, shutdown recommended!" + '\n'
elif status == 1:
    print("Everything is working normally.")
    result += "Everything is working normally." + '\n'
else:
    print("Machine is stopped, no immediate action needed.")
    result += "Machine is stopped, no immediate action needed." + '\n'

result += '*' * 26 + '\n'

file = open('week1.2/session2/task6/machine_log.txt', 'a')
file.write(result)
file.close()

