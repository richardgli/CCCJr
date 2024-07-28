start = list(map(int,input().split()))
end = list(map(int,input().split()))
steps = int(input())

def moves(pos, end, steps):

  if (pos == end) & (steps == 0):
    return True
  elif (pos != end) & (steps == 0):
    return False

  left = pos[:1]
  left.append(pos[1] - 1)
  right = pos[:1]
  right.append(pos[1] + 1)
  up = pos[1:]
  up.insert(0, pos[0] + 1)
  down = pos[1:]
  down.insert(0, pos[0] - 1)
  
  return moves(left, end, steps - 1) or moves(right, end, steps - 1) or moves(up, end, steps - 1) or moves(down, end, steps - 1) 

if moves(start, end, steps):
  print("Y")
else:
  print("N")
