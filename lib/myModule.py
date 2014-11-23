# my_module.py
import math

# this function finds the log_2 (lg) of the passed argument
def log2(value) :
  return math.log10(value)/math.log10(2)

# this function finds the log_n of the passed argument
def logN(value, base) :
  return math.log10(value)/math.log10(base)