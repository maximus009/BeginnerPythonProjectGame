import decimal
def update_version():
	my_file = open("version.txt","r")
	txt = decimal.Decimal(my_file.readline())
	my_file.close()
	my_file = open("version.txt","w")
	number = 0.0001
	version = txt+decimal.Decimal(number)
	my_file.write(str(round(version,4)))
	my_file.close()
