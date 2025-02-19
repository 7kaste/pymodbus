from pymodbus.client import ModbusTcpClient

HOST = '<IP>'  
PORT = 502   
OBJECT_ID = 1 # Modbus Unit ID (commonly 1)

read_count = 20

client = ModbusTcpClient(HOST, port=PORT)
if client.connect():
    print("Connected to Modbus server.")
    try:
        
        response = client.read_device_information(object_id=OBJECT_ID)

        if not response.isError():
            print("Device Information:")
        for key, value in response.information.items():
            print(f"{key}: {value}")
        else:
            print(f"Error reading device information: {response}")
            
        # Query Holding Registers (Function Code 0x03)
        print("\nReading Holding Registers...")
        response = client.read_holding_registers(address=0, count=read_count)
        if not response.isError():
            print(f"Holding Registers Data: {response.registers}")
        else:
            print(f"Error reading holding registers: {response}")

        # Query Input Registers (Function Code 0x04)
        print("\nReading Input Registers...")
        response = client.read_input_registers(address=0, count=read_count)
        if not response.isError():
            print(f"Input Registers Data: {response.registers}")
        else:
            print(f"Error reading input registers: {response}")

        # Query Coils (Function Code 0x01)
        print("\nReading Coils...")
        response = client.read_coils(address=0, count=read_count)
        if not response.isError():
            print(f"Coils Data: {response.bits}")
        else:
            print(f"Error reading coils: {response}")

        # Query Discrete Inputs (Function Code 0x02)
        print("\nReading Discrete Inputs...")
        response = client.read_discrete_inputs(address=0, count=read_count)
        if not response.isError():
            print("Discrete Inputs Data: {response.bits}")
        else:
            print("Error reading discrete inputs: {response}")
            
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        client.close()
else:
    print("Failed to connect to the Modbus server.")
