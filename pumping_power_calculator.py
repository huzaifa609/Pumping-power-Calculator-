Pumping Power Calculator

Calculates pumping power based on flow rate, head, density, gravity, and efficiency

Formula:

Pumping Power (W) = (rho * g * Q * H) / efficiency

Inputs

flow_rate = float(input("Enter flow rate Q (m^3/s): ")) head = float(input("Enter pump head H (m): ")) density = float(input("Enter fluid density rho (kg/m^3): ")) efficiency = float(input("Enter pump efficiency (0 to 1): "))

Constant

g = 9.81  # m/s^2

Calculation

pumping_power = (density * g * flow_rate * head) / efficiency

Output

print("\nResults") print(f"Pumping Power = {pumping_power:.2f} Watts") print(f"Pumping Power = {pumping_power/1000:.2f} kW")
