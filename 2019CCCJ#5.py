rule1 = list(input().split())
rule2 = list(input().split())
rule3 = list(input().split())
sequences = list(input().split())
steps = int(sequences[0])
listStep = []
initialSeq = sequences[1]
finalSeq = sequences[2]
d = {}

def substitution(step, seq, d, listStep):

  if (step == 0) and (seq == finalSeq):
    return d

  if (step == 0) and (seq != finalSeq):
    d[steps + 1] = "Nothing"
    return d

  for i in range(len(seq)):
    
    #rule 1
    #checks for rule 1, transforms the sequence, and adds the step to the dictionary
    if seq[i:i+len(rule1[0])] == rule1[0]:
      newSeq = seq[:i] + rule1[1] + seq[i+len(rule1[0]):]
      listStep = [1, i + 1, newSeq]
      d[steps - step + 1] = listStep
      di = substitution(step - 1, newSeq, d, listStep)
      if len(di) == steps:  
        return di
      d.popitem()  #to remove the "Nothing" from d

    #rule 2
    if seq[i:i+len(rule2[0])] == rule2[0]:
      newSeq = seq[:i] + rule2[1] + seq[i+len(rule2[0]):]
      listStep = [2, i + 1, newSeq]
      d[steps - step + 1] = listStep
      di = substitution(step - 1, newSeq, d, listStep)
      if len(di) == steps:
        return di
      d.popitem()

    #rule 3
    if seq[i:i+len(rule3[0])] == rule3[0]:
      newSeq = seq[:i] + rule3[1] + seq[i+len(rule3[0]):]
      listStep = [3, i + 1, newSeq]
      d[steps - step + 1] = listStep
      di = substitution(step - 1, newSeq, d, listStep)
      if len(di) == steps:
        return di
      d.popitem()
  #when all the letters are checked and the program returns back to the previous iteration of the function, the program stays in the loop without returning immediately
  d[steps + 1] = "Nothing"
  return d

di = substitution(steps, initialSeq, d, listStep)
for i in di:
  line = di[i]
  print(str(line[0]) + " " + str(line[1]) + " " + line[2])
