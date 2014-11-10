import ldap
import getpass

pd = getpass.getpass()

#LDAP authentication
try:
	l = ldap.open("192.168.x.x")
	l.protocol_version = ldap.VERSION3
	username = "cn=Directory Manager, dc=corp, dc=example, dc=com"
	password = pd
	l.simple_bind_s(username, password)
except ldap.LDAPError, e:
	print e

##LDAP search
baseDN = "ou=people, dc=corp, dc=example, dc=com"
searchScope = ldap.SCOPE_SUBTREE
## retrieve all attributes
retrieveAttributes = ['mail']
searchFilter = "sn=*"

try:
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
	result_set = []
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
		if (result_data == []):
			break
		else:
			if result_type == ldap.RES_SEARCH_ENTRY:
                result_set = result_data
            print result_set

except ldap.LDAPError, e:
	print 'error'
