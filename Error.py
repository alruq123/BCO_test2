
#Error Domain 

f = open("myfile.txt","w+")

er= input("Would you like to include an error domain? yes or no:")
if er == 'yes':
    error= input("Input Error:")
    f.write(" \t\t\"error\": \"%s\" \n" %error)
if er == 'no':
  a = 9

f.close()
