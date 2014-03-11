my_file = open("version.txt","r")
txt = float(my_file.readline())
my_file.close()
my_file = open("version.txt","w")
version = txt+0.0001
my_file.write(str(version))
my_file.close()
