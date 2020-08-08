
#Provenance Domain: 

f = open("myfile.txt","w") 


print("Fill in the prompts to create a BCO" )
print("Provenance Domain \n")
f.write( "\"provenance_domain\": { \n")

embargo_yn = input(" Does your BCO have an Embargo Period? yes or no: ")
if embargo_yn == "yes":
    start_time = input(" Embargo Start Time: ")
    end_time = input(" Embargo End Time: ")
    f.write("\t\"embargo\": {\n")
    f.write("\t\t\"start_time\": \"%s\",\n" %start_time)
    f.write("\t\t\"end_time\": \"%s\" ,\n" %end_time)
    f.write("\t},\n")

print("\nBCO Information:\n" )
BCO_name = input(" name: ")
version = input(" version: ")
obsolete_after = input(" obsolete after: ")



print("\n Review Subdomain: \n" )
print("Enter Information about the reviewer:" )
r_name = input(" name: ")
r_affiliation = input(" affiliation: ")
r_contribution = input(" contribution: ")
r_email = input(" email: ")
r_orcid = input(" orcid: ")
reviewer_comment = input(" comment: ")

f.write("\t\"review\": [ \n")    
f.write("\t\t\"reviewer\": {\n" )
f.write("\t\t\t\"name\": \"%s\",\n" %r_name)
f.write("\t\t\t\"affiliation\": \"%s\",\n"%r_affiliation)
f.write("\t\t\t\"contribution\": \"%s\" \n" %r_contribution )                   
f.write("\t\t\t\"email\": \"%s\",\n" %r_email)
f.write("\t\t\t\"orcid\": \"%s\",\n" %r_orcid)
f.write("\t\t\t\"status\": \"unreviewed\",\n")
f.write("\t\t\t\"reviewer_comment\": \"%s\"\n" %reviewer_comment)

rev_yn = input(" Would you like to include more reviewers? yes or no: ")
if rev_yn == "yes":
    rev=int(input('Enter Amount of Reviewers you would like to add: \n'))  
    for i in range (0,rev):
        print("Enter Information about reviewer number %s:" %rev )
        r_name = input(" name: ")
        r_affiliation = input(" affiliation: ")
        r_contribution = input(" contribution: ")
        r_email = input(" email: ")
        r_orcid = input(" orcid: ")
        reviewer_comment = input(" comment: ")
        print("\n")
        f.write("\t\t\t\"reviewer\": {\n" )
        f.write("\t\t\t\"name\": \"%s\",\n" %r_name)
        f.write("\t\t\t\"affiliation\": \"%s\",\n"%r_affiliation)
        f.write("\t\t\t\"contribution\": \"%s\" \n" %r_contribution )                   
        f.write("\t\t\t\"email\": \"%s\",\n" %r_email)
        f.write("\t\t\t\"orcid\": \"%s\",\n" %r_orcid)
        f.write("\t\t\t\"status\": \"unreviewed\",\n")
        f.write("\t\t\t\"reviewer_comment\": \"%s\"\n" %reviewer_comment)
    
    
dev = input(" Derived From: ")
f.write("\t\"derived_from\": \"%s\",\n" %dev)

print("\n Contributer Subdomain: \n" )
print("Enter Information about the contributer:" )

c_email = input(" email: ")
c_name = input(" name: ")
c_contribution = input(" contribution:")
c_affiliation = input(" affiliation:")
c_orcid = input(" orcid:") 
created = input(" created: ")    
modified = input(" modified: ")

f.write("\t\"contributors\": [\n")
f.write("\t\t\t\email\": \"%s\",\n" %c_email)
f.write("\t\t\t\"name\": \"%s\",\n" %c_name)
f.write("\t\t\t\"orcid\": \"%s\",\n" %c_orcid)
f.write("\t\t\t\"contribution\": \"%s,\",\n" %c_contribution)
f.write("\t\t\t\"affiliation\": \"%s\",\n"%c_affiliation)
f.write("\t\t\t\"created\": \"%s\",\n"%created)
f.write( "\t\t\t\"modified\": \"%s\",\n"%modified)


c_yn = input(" Would you like to include more contributer? yes or no: ")
if c_yn == "yes":
    cev=int(input('Enter Amount of contributer you would like to add: \n'))  
    c_email = input(" email: ")
    c_name = input(" name: ")
    c_contribution = input("contribution:") 
    c_affiliation = input("affiliation:") 
    c_orcid = input("orcid:") 
    created = input(" created: ")
    modified = input(" modified: ")
    derived_from = input(" derived_from: ")
    f.write("\t\"derived_from\": \"%s\",\n" %dev)
    
    f.write("\t\"contributors\": [\n")
    f.write("\t\t\"email\": \"%s\",\n" %c_email)
    f.write("\t\t\"name\": \"%s\",\n" %c_name)
    f.write("\t\t\"orcid\": \"%s\",\n" %c_orcid)
    f.write("\t\t\"contribution\": \"%s,\",\n" %c_contribution)
    f.write("\t\t\"affiliation\": \"%s\",\n"%c_affiliation)
    f.write("\t\t\"created\": \"%s\",\n"%created)
    f.write( "\t\t\"modified\": \"%s\",\n"%modified)

f.write("\t\"name\": \"%s\",\n" %BCO_name)
f.write("\t\"version\": \"%s\",\n" %version)
f.write("\t\"obsolete_after\": \"%s\",\n "%obsolete_after)

license_yn = input(" Is the license of your BCO the the default or recommended license Attribution 4.0 International? yes or no: ")
if license_yn == "no":
    license = input(" license: ")
    f.write("\"license\": %s [ \n" %license)
if license_yn == "yes":
    f.write("\"license\": \"https://spdx.org/licenses/CC-BY-4.0.html\" ,\n")


f.close()

