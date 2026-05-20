from netmiko import ConnectHandler

# Device configuration
device = {
    'device_type': 'generic',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

def connect_to_device():
    try:
        print("Connecting to device...")
        connection = ConnectHandler(**device)
        print("Connected successfully!")
        
        # Here we will add network commands later
        connection.disconnect()
        print("Disconnected.")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    connect_to_device()
