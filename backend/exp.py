from random import randint as randint, choice as choice

# Notes: constant, hardcode
Q_ROUND=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
# For searching without excess lines of code
Q_ROUND_x2=Q_ROUND+Q_ROUND

# Function set of random note
def gen_random_note():
  random_note_result=randint(0,11)
  return random_note_result

# Function set of random scale (Major/Minor) 
def gen_random_scale():
  random=randint(0,1)
  if random == 1:
      random_scale_result="m"
  else:
      random_scale_result=""
  return random_scale_result

# Looking for a Dominant chord
note=gen_random_note()
scale=gen_random_scale()
dominant=Q_ROUND[note] + scale
#print(dominant)

# Looking for a consonance of the Dominant chord
if scale == "m":
  consonances=[dominant, Q_ROUND_x2[note+3], Q_ROUND_x2[note+5]+'m', Q_ROUND_x2[note+7]+"m", Q_ROUND_x2[note+8], Q_ROUND_x2[note+10]]
else:
  consonances=[dominant, Q_ROUND_x2[note+2]+'m', Q_ROUND_x2[note+4]+'m', Q_ROUND_x2[note+5], Q_ROUND_x2[note+7], Q_ROUND_x2[note+9]+'m']

# Output a chords: first is Dominant, another is Consonance
print(consonances)  



