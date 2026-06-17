import pyvisa

load = pyvisa.ResourceManager().open_resource("LOAD_ADDRESS")

load.write("CURR 1.0")   # Set load current to 1 A
