import pyvisa

scope = pyvisa.ResourceManager().open_resource("SCOPE_ADDRESS")

voltage = scope.query("MEAS:VOLT?")
ripple = scope.query("MEAS:VRIP?")

print("Voltage =", voltage)
print("Ripple =", ripple)
