import re
import string
import datetime
import CF_calculator as cfmod

surname = 'Dainese'
name = 'Carlo'
birthday = datetime.datetime(1967, 1, 7)
sex = 'M'
municipality = 'Z133'

cf = cfmod.build(surname,name,birthday,sex,municipality)

print(cf)