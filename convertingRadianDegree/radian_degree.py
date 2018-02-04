# This Program allows us to convert angle from radian to degree, minutes, seconds and vice-versa

import math # import math module for using pi

print("Converting Radian to Degree, Minutes, Seconds")
rad = float(input("Enter the angle (in radian)\n"))
degree_float = (rad * 180) / math.pi
degree_int = int(degree_float)
degree_dec_part = degree_float - degree_int
number_seconds = degree_dec_part * 3600
minutes = number_seconds // 60
modulo = number_seconds % 60
seconds = modulo
print("{} radian(s) represents {} degree, {} minute(s), {} second(s)".format(rad, degree_int, minutes, seconds)) 