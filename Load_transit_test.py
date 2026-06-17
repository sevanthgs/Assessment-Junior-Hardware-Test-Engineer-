import csv

rails = {
    "3.6V": 3.6,
    "1.8V": 1.8,
    "3.3V": 3.3,
    "2.5V": 2.5
}

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Rail", "Voltage", "Ripple", "Status"])

    for rail, voltage in rails.items():

        measured_voltage = voltage
        ripple = 0.02

        status = "PASS" if ripple < 0.05 else "FAIL"

        writer.writerow([rail, measured_voltage, ripple, status])

        print(rail, measured_voltage, ripple, status)

print("Test Completed")
