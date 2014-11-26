Google Contacts Uploader (gcup)
====

**gcup** is a Python script that bulk uploads vCards (.vcf files) stored in a directory to your Google Contacts.
This is a very minimal script that works with Basic Authentication.

**Because of this reason, if you use this script without following the steps below, you will get a *"Password Incorrect"* error.**

This issue will be resolved in future updates but for now, you can upload to Google Contacts via basic authentication by allowing less secure apps to access you account, as described [here](https://support.google.com/accounts/answer/6010255?hl=en).

<br/>
####Feature List
This is a very modest script. As of now, it has the following features:
- Supports Name, Phone number and Email for any contact. ( Address and photo support will be added later)
- Cannot sync automatically when vCard files are added.
<br/>

###Table of Contents
- Usage
- Dependencies
- Other Info
<br/>

####Usage
1. Download the **gcup.py** into the directory containing the vCards (.vcf files).
2. **[Enable the app to access your Google account](https://support.google.com/accounts/answer/6010255?hl=en)** 
3. Run the script. ```python gcup.py [email] [password]```
4. Enter '0' to exit program or any other key to start the upload.

<br/>
####Dependencies
- **GDATA**: Google Data APIs for Python. `pip install gdata`
- **VOBJECT**: For parsing .VCF files. `pip install vobject`
<br/>

####Other Info
I pulled this script off when I urgently needed to bulk upload vCards to my Google Contacts account.
This is a crude script but gets the job done for now. I will surely refine it more once I am over with my other projects.

