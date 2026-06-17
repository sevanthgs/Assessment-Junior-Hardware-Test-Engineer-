import pyvisa

ps = pyvisa.ResourceManager().open_resource("POWER_SUPPLY_ADDRESS")

ps.write("VOLT 5")      # Set voltage to 5V
ps.write("CURR 2")      # Set current limit to 2A
ps.write("OUTP ON")     # Turn ON output

# Testing...

ps.write("OUTP OFF")    # Turn OFF output
