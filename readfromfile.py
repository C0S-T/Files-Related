FN = "Darius-13-100m-Fly.txt"
FOLDER = "swimdata/"

swimmer,age,meters,style = FN.removesuffix('.txt').split('-')
with open(FOLDER + FN, 'r') as f:
    data = f.read().strip().split(',')
print(data)
convert_time=[]
for i in data:
    first = i
    mins,rest = first.split(':')
    seconds,hundredths = rest.split('.')
    convert_time.append((int(mins)*60*100) + (int(seconds)*100) + (int(hundredths)))
print(convert_time)



