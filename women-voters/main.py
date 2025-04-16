import csv

marches = []
states = []

with open('2017_womens_march.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    marches.append(row)
print("step 2")
print(len(marches))

print("2.a")
print(marches[0].keys())

for march in marches:
  states.append(march['State'])

uniqueStates = list(set(states))
uniqueStates.sort()
print("2.b")
print(uniqueStates)

# C
fewestMarchers = 10000000
cityWithFewest = ""
for march in marches:
  if float(march['Low estimate']) <fewestMarchers:
    fewestMarchers = float(march['Low estimate'])
    cityWithFewest = march['City']
print("2.c")
print(fewestMarchers)
print(cityWithFewest)

# 1
mostMarch = 0
mostCity = ""
for march in marches:
  if float(march['High estimate']) >mostMarch:
    mostMarch = float(march['High estimate'])
    mostCity = march['City']
print("1:")
print(mostCity)
print(mostMarch)

# 2
maineMarchers = 0
for march in marches:
  if march['State'] == 'ME':
    maineMarchers = maineMarchers + 1
print("2:")
print(maineMarchers)