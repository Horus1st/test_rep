# Author: Samuel. O
#Created on 07/09/2022
import re
pattern_1 = '^h...s$'
input_1 = 'Hello did you get a pattern?'
outcome_1 = re.match(pattern_1, input_1)
if outcome_1:
	print('Input_1 pattern found')
	print(outcome_1)
else:
	print('no match found')
input_2 = 'roll number 7 is doing better than number 12 but roll number 10 exceeding good'
pattern_2 = '\d+'
outcome_2 = re.findall(pattern_2, input_2)
print(outcome_2)
data = '1 Twelve is 12 and 2 Eighty nine is 89'
pattern_3 = '\d+'
outcome_3 = re.split(pattern_3, data)
print(outcome_3)

