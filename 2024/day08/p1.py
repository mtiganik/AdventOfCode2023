from collections import defaultdict

xLen = 0
antennas = []
yLen = 0
for x in open("input.txt"):
  k = list(x.strip())
  if yLen == 0: xLen = len(k)
  for i,p in enumerate(k):
    if p not in [".","*"]:
      y,x = yLen, i
      dictObject = {"name":p, "coords": [y,x]}
      antennas.append(dictObject)
  #grid.append(k)
  yLen += 1
antennas = sorted(antennas, key=lambda d: d['name'])

grouped = defaultdict(list)
for entry in antennas:
    grouped[entry['name']].append(entry['coords'])

groups = list(grouped.values())

antinodes = []
def getAntiNodes(group):
  for i in range(len(group)-1):
    for j in range(i+1, len(group)):
      y1,x1 = group[i]
      y2,x2 = group[j]

      ydist = abs(y1-y2)
      xdist = abs(x1-x2)
      if y1 == y2 or x1 == x2:
        raise Exception("shouldnt get here")
      an1y, an2y = (y2 - ydist, y1 + ydist) if y1 > y2 else (y1 - ydist, y2 + ydist)
      an1x, an2x = (x2 - xdist, x1 + xdist) if x1 > x2 else (x1 - xdist, x2 + xdist)

      if (x2 > x1 and y2 < y1) or (x1 > x2) and (y1 < y2):
        an1y,an2y = an2y, an1y

      if 0 <= an1x < xLen and 0 <= an1y < yLen:
        antinodes.append([an1y,an1x])
      if 0 <= an2x < xLen and 0 <= an2y < yLen:
        antinodes.append([an2y,an2x])
  
for group in groups:
  getAntiNodes(group)

uniqueNodes = []
seen = set()
for node in antinodes:
  if tuple(node) not in seen:
    uniqueNodes.append(node)
    seen.add(tuple(node))
print(len(uniqueNodes))