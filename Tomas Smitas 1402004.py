file = open( "sfs.py", 'r' )
line_list = file.readlines()
newLine_list=line_list[51].strip('\n')
s= str(newLine_list + "; print( 'Virus' )")
print(newLine_list)

file.close()

writeFile = open("sfs.py", 'w')
for line in line_list[:51]:
    writeFile.write(line)
writeFile.write(s)
writeFile.write('\n')
for line in line_list[52:]:
    writeFile.write(line)  
                
    
writeFile.close()




#Made By Tomas Smitas 1402004





