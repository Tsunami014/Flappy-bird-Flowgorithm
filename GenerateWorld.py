import re

def cleanFile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        top = max([len(i.rstrip(' \n')) for i in lines])
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip(' \n')
            if len(lines[i]) < top:
                lines[i] = lines[i] + " " * ((top - len(lines[i]))) + '\n'
        with open(file, 'w') as f:
            f.writelines(lines)

# To be implemented when we have multiple world-based projects:
# inp = input("Enter game to update world of ('Platformer'): ")
# if inp == "Platformer":

assign = "            <assign variable=\"world1[0]\" expression=\"&quot;{0}&quot;\"/>\n"

newdata = ""
with open('data/level1.txt', 'r') as f:
    data = f.readlines()
    for i in range(len(data)):
        newdata += assign.format(data[i].strip('\n'))

cleanFile('data/level1.txt')
with open('Platformer.fprg', 'r') as f:
    data = f.read()
wrapper = '<comment text="Auto generated code below"/>{0}            <comment text="Auto generated code above"/>'
for i in re.findall('(%s)' % wrapper.replace('/', '\\/').format("(.|\n)+?"), data):
    data = data.replace(i[0], wrapper.format('\n'+newdata))

with open('Platformer.fprg', 'w') as f:
    f.write(data)
