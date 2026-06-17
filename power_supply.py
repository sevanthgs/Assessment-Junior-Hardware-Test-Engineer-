import pyvisa

ps = pyvisa.ResourceManager().open_resource("ADDRESS")

ps.write("VOLT 5")    # Set 5V
ps.write("CURR 2")    # Set 2A current limit
ps.write("OUTP ON")   # Turn ON output

# Run test

ps.write("OUTP OFF")  # Turn OFF output
