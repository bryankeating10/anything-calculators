from math import sqrt

# WATER CONSTANTS
rho = 999.87					# Density (kg/m^3)
k = 2.23						# Thermal coefficient (W/m*K)
L_f = 334e3						# Latent heat of fussion (J/kg)

# VARIABLE INITITALIZATION
T_inf = 0						# Air temp (C)
xi = 0							# Initial thickness (m)
xf = 0							# Final thickness (m)
ti = 0							# Initial time (s)
tf = 3600*24*10					# Final time (s)


# NEW ICE THICKNESS
def new_ice(xi,ti,tf,T_inf):
	dt = tf-ti
	return sqrt(2*k*-T_inf*dt/(rho*L_f)+xi**2)

# CONVERTS METERS TO INCHES
def m2in(meters):
	return meters*39.37

result = new_ice(xi,ti,tf,-6.67)
print(result)
print(f'Inches: {m2in(result)}')

# INTEGRATION OF TEMPERATURE PROFILE
time_hours = list(range(25))
temp_hours = []