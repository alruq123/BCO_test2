
#------------------------------------------------------------
#"parametric_domain": 


print("\n Parametric Subdomain: \n" )


f = open("myfile.txt","a") 


param = input(" param: ")
value = input(" value: ")
step = input(" step: ")


f.write( "\"parametric_domain\":" )
f.write("\param\": \"%s\"," %param)
f.write( "\"value\": \"%s\"," %value)
f.write("\"step\": \"%s\"" %step)


sw_yn = input(" \n Would you like to include more parameters? yes or no:")
if sw_yn == "yes":
    a = input("How many?")
    val = range(a)
    for i in val: 
        param = input(" param: ")
        value = input(" value: ")
        step = input(" step: ")
        
        f.write( "\"parametric_domain\": \n" )
        f.write("\param\": \"%s\",\n" %param)
        f.write( "\"value\": \"%s\",\n"%value)
        f.write("\"step\": \"%s\"\n" %step)



f.close()
#--------------------------------------------------------
