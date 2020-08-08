


# Execution Domain

# Software Prerequisites

f = open("myfile.txt","a")


print("\n Exectution Subdomain: \n" )
print("Enter Information:" )

sw_number = int(input("Input Number of Software Prerequisites: "))
for i in range(sw_number):
    
    print("Information about step number %s" %(i+1))
    sw_name = input(" Software Name: ")
    f.write(" \"name\": \"%s\" \n" %sw_name)
    sw_uri = input(" Software uri: ")
    f.write(" \"uri\": \"%s\" \n" %sw_uri)
    sw_access_time = input(" Access Time: ")
    f.write(" \"access_time\": \"%s\" \n" %sw_access_time)

f.write(" \n\"environment_variables\": [ \n \t{\n") 


print("\nEnter Evironmental Variables :\n")
sw_value = input(" Software Value:  ")
f.write(" \t\t\"value\": \"%s\" \n" %sw_value)
sw_key= input(" Software Key:  ")
f.write(" \t\t\"key\": \"%s\" \n" %sw_key)
    
sw_yn = input("\nWould you like to include more environment variables? yes or no: ")
if sw_yn == "yes":
    sw_no= input("How many?:")
    val = range(sw_no)
    for a in val: 
        sw_value = input(" Software Value:  ")
        f.write(" \t\t\"value\": \"%s\" \n" %sw_value)
        sw_key= input(" Software Key:  ")
        f.write(" \t\t\"key\": \"%s\" \n" %sw_key)
        
    

f.close()
