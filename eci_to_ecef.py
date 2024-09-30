# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
# Text explaining script usage
# Parameters:
# arg1: description of argument 1
# arg2: description of argument 2
# ...
# Output:
# A description of the script output
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
# e.g., import math # math module
import sys
import math
import numpy as np
# "constants"
R_E_KM = 6378.137
w=7.292115*(10**-5)
# helper functions
## function description
# def calc_something(param1, param2):
# pass
# initialize script arguments
year=float('nan')
month=float('nan')
day=float('nan')
hour=float('nan')
minute=float('nan')
second=float('nan')
eci_x_km=float('nan')
eci_y_km=float('nan')
eci_z_km=float('nan')
if len(sys.argv)==10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day  = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    eci_x_km=float(sys.argv[7])
    eci_y_km=float(sys.argv[8])
    eci_z_km=float(sys.argv[9])
else:
    print(\
     'Usage: '\
     'python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
    )
    exit()
# write script below this line
A = math.floor(year / 100)
B = 2 - A + math.floor(A / 4) 
jd = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5
# Add the fractional part of the day
d_frac = (hour + minute / 60 + second / 3600) / 24
jd_frac=jd+d_frac
T = (jd_frac - 2451545.0) / 36525.0
gmst_0 = (67310.54841 + (876600 * 60*60 +8640184.812866)*T + 0.093104 * T**2 - 6.2e-6 * T**3)
gmst_rad = math.fmod(gmst_0%86400 * w +2*math.pi, 2*math.pi)
#ecef_x_km=eci_x_km*(math.cos(gmst_rad))-eci_y_km*(math.sin(gmst_rad))
#ecef_y_km=eci_y_km*math.cos(gmst_rad)+eci_x_km*math.sin(gmst_rad)
#ecef_z_km=eci_z_km
eci_vec=np.array([eci_x_km, eci_y_km, eci_z_km])
rot_matrix= np.array([[math.cos(-gmst_rad), -math.sin(-gmst_rad), 0], 
                    [math.sin(-gmst_rad), math.cos(-gmst_rad), 0],
                    [0,0,1]])
r_ecef=np.dot(rot_matrix, eci_vec)
ecef_x_km=r_ecef[0]
ecef_y_km=r_ecef[1]
ecef_z_km=r_ecef[2]
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)