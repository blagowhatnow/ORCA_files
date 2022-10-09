#Parse ORCA output file to extract HOMO LUMO Gap. Might need revision.

import re
string="ORBITAL ENERGIES"

lines=[]
linenum=0

with open('inpu.txt') as my_file:
     for line in my_file:
         linenum+=1
         if line.find(string) !=-1:
             lines.append(linenum+15)
             lines.append(linenum+16)
 
linenum=0
select=[]

with open('inpu.txt') as my_file:
     for line in my_file:
         linenum+=1
         if linenum==lines[2]:
            select.append(str(line))
         elif linenum==lines[3]:
            select.append(str(line))

HOMO=[float(s) for s in re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",select[0])][3]

LUMO=[float(s) for s in re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",select[1])][3]

print("LUMO: "+str(LUMO))
print("HOMO: "+str(HOMO))
print("GAP: "+str(LUMO-HOMO))
