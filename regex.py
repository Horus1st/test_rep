# Author: Samuel. O
#Created on 07/09/2022
import re
pattern_1 = '^h...s$'
input_1 = 'hello did you get a pattern?'
outcome_1 = re.match(pattern1, input1)
if outcome_1:
	print('Input_1 pattern found')
	print(outcome_1)
else:
	print('no match found')
input_2 = 'roll no 7 is doing better than rollno 12 but rollno 10 exceeding good'
pattern_2 = '\d+'
outcome_2 = re.findall(pattern_2, input_2)
print(outcome_2)
data = 'Twelve : 12 Eighty nine : 89'
pattern_3 = '\d+'
outcome_3 = re.split(pattern, data)
print(outcome_3)

