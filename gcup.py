import sys
import gdata.data
import gdata.contacts.client
import gdata.contacts.data
import glob
import vobject
import time

#Class Connection to invoke everything
class Connection(object):

	def __init__(self,emailID,Password):
		self.gd_client = gdata.contacts.client.ContactsClient(source='GContactsUploader')
		print self.gd_client.ClientLogin(emailID,Password,self.gd_client.source)
		print "\nWhoo Hoo! We're connected to the Google Server..."


	def Sync(self):

		flag = raw_input("Press '0' to exit program or any other key to continue: ")
		if flag == '0':
			exit()
			
		vcf_list = glob.glob("C:\Users\Tuhin\Desktop\contacts\*.vcf")
		count = 0

		for people in vcf_list:

			fp = open(people,"r")
			content = fp.read()
			fp.close()

			v = vobject.readOne(content)

			name=v.n.value
			number=v.tel.value

			new_contact = gdata.contacts.data.ContactEntry()
			new_contact.name = gdata.data.Name(full_name=gdata.data.FullName(text=name))
			new_contact.phone_number.append(gdata.data.PhoneNumber(text=number,rel=gdata.data.WORK_REL,primary='true'))

			contact_entry = self.gd_client.CreateContact(new_contact)
			print "Contact's ID: ", contact_entry.id.text
			name =""
			number = ""
			count = count + 1
			print "\nUploaded Contacts: (" + str(count) + "/322)"
			time.sleep(1)

	    	



#Main Function here, triggers the Connection class
def main():

	''' REVISION FOR LATER 
		This part would require further cleaning 
		Use GETOPT instead of simple SYS 
	'''

	if (len(sys.argv) < 3):
		print '\nINVAID INPUT FORMAT'
		print '\n\t Usage: python g.py [email] [password]'
		print '\n'
	else:
		email = sys.argv[1].replace(" ","")
		passw = sys.argv[2].replace(" ","")

		try:
			instance = Connection(email,passw)
			print '\nEmail is: ', email,' \nPassword is: ', passw
			print '\n'

			#Main function call!
			instance.Sync()	

		except gdata.client.BadAuthentication:
			print 'Invalid user credentials given'
			return

if __name__ == '__main__':
	main()