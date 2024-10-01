# ecef_to_sez.py

# Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km
#  Converts ECEF vector components to SEZ

# Parameters:
#  o_x_km: x component of ECEF vector
#  o_y_km: y component of ECEF vector
#  o_z_km: z component of ECEF vector
#  x_km: x component of ECEF position
#  y_km: y component of ECEF position
#  z_km: z component of ECEF position
# Output:
#  Prints the coordinates in the SEZ reference frame (s, e, z), answer in km

# Written by Maxwell Oross
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys  # argv

# "constants"

# initialize script arguments
o_x_km: float(sys.argv[1])
o_y_km: float(sys.argv[2])
o_z_km: float(sys.argv[3])
x_km: float(sys.argv[4])
y_km: float(sys.argv[5])
z_km: float(sys.argv[6])

# parse script arguments
if len(sys.argv)==7:
  o_x_km = float(sys.argv[1])
  o_y_km = float(sys.argv[2])
  o_z_km = float(sys.argv[3])
  x_km = float(sys.argv[4])
  y_km = float(sys.argv[5])
  z_km = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ecef_to_llh.py r_x_km r_y_km r_z_km'\
  )
  exit()

# write script below this line
s_km = x_km - o_x_km
e_km = y_km - o_y_km
z_km = z_km - o_z_km

# Display final answers
print(s_km)
print(e_km)
print(z_km)

