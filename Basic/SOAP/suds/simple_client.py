# -*- coding: utf-8 -*-
import suds
authWsdlUrl = "http://web02.psps.ifa.hawaii.edu/DFetch/WSDL/AuthService.wsdl.php"
jobsWsdlUrl = "http://web02.psps.ifa.hawaii.edu/DFetch/WSDL/JobsService.wsdl.php"

schemaGroup = "PS1_SCHEMA"
schema  = "PS1_3PI"
query = "select top 10 * from Object"
user = 'conradh'
password = 'nothing0'

# get arguments for query file and file name to write output.
queryFileName = sys.argv[1]
resultFileName = sys.argv[2]

authClient = suds.client.Client( authWsdlUrl )
jobsClient = suds.client.Client( jobsWsdlUrl )

print "Authenticating..."
sessionID =  authClient.service.login( user, password)
print "Log in successful session token:", sessionID
task = "Executing query from python script"

#executeQuickJob(xs:string sessionID, xs:string schemaGroup, xs:string query, xs:string context, xs:string taskname, xs:boolean isSystem, )
# SOAP call to execute query
queryResults = jobsClient.service.executeQuickJob( sessionID, schemaGroup, query, schema, task, False);
print queryResults;


