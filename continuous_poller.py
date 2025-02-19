import time
from pymodbus.client import ModbusTcpClient

HOST = '<IP>'
PORT = 502
POLL_INTERVAL = 1  

# Update the coils and register values according to your needs
coils = {
            "coil_1": 5, # i.e. motor
            "coil_2": 8, # i.e. pump
            "coil_3": 11 # i.e. valve
        }

holding_registers = {
            "holding_register_1": 8 # i.e. setpoint
        }

input_registers = {
            "input_register_1": 1, # i.e. temperature
            "input_register_2": 2  # i.e. pressure
        }

discrete_inputs = {
            "discrete_input_1": 1, # i.e. alarm
            "discrete_input_2": 2  # i.e. fault
        }

previous_coil_values = {}
previous_holding_register_values = {}
previous_input_register_values = {}
previous_discrete_input_values = {}

client = ModbusTcpClient(host=HOST, port=PORT)
if client.connect():
    print("Connected to Modbus server")
    
    while True:
        # Poll coil values
        for key, coil in coils.items():
            result = client.read_coils(coil, 1)
            value = result.bits[0]
            
            if coil not in previous_coil_values or previous_coil_values[coil] != value:
                print(f"Coil {key} ({coil}) updated to {value}")
                previous_coil_values[coil] = value

        # Poll holding register values
        for key, register in holding_registers.items():
            result = client.read_holding_registers(register, 1)
          
            value = result.registers[0]
            if register not in previous_holding_register_values or previous_holding_register_values[register] != value:
                print(f"Register {key} ({register}) updated to {value}")
                previous_holding_register_values[register] = value
    
        # Poll input register values
        for key, register in input_registers.items():
            result = client.read_input_registers(register, 1)
           
            value = result.registers[0]
            if register not in previous_input_register_values or previous_input_register_values[register] != value:
                print(f"Register {key} ({register}) updated to {value}")
                previous_input_register_values[register] = value
    
        # Poll discrete input values
        for key, discrete_input in discrete_inputs.items():
            result = client.read_discrete_inputs(discrete_input, 1)
            value = result.bits[0]
           
            if discrete_input not in previous_discrete_input_values or previous_discrete_input_values[discrete_input] != value:
                print(f"Discrete input {key} ({discrete_input}) updated to {value}")
                previous_discrete_input_values[discrete_input] = value
    
    
        time.sleep(POLL_INTERVAL)
        
else:
    print("Failed to connect to Modbus server")
client.close()
