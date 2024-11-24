num_pages = int(input())
d = {}
for i in range(1, num_pages+1):
    d[i] = list(map(int,input().split()))[1:]

visited = []
frontier = [1]
level = 1
found_ending = False
min_path = 0

while frontier:
    l = len(frontier)
    for i in range(len(l)):
        cur = frontier.pop(0)
        visited.append(cur)
        if d[cur] == [] and (not found_ending):
            min_path = level
            found_ending = True
        for i in d[cur]:
            if i not in visited:
                frontier.append(i)
    level += 1

if len(visited) == num_pages:
    print("Y")
else:
    print("N")

print(min_path)
