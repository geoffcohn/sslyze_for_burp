Set up burp for jython extionsion
	http://portswigger.net/burp/help/extender.html

Copy this entire directory to your machine

Configure the burp.bat file
	This file is used to launch Burp with extra memory to allow jython extensions to run
	
	To configure the bat file, uncomment the line of code that launches burp (java -Xms1g -Xmxlg ...) and insert the absolute file path to your burp executable

	
Running this extension
	In order to run this extension, you must launch burp from the burp.bat file in this folder
	
	Once burp has been launched
		Click the "extender" tab > "Extensions"
		Click add 
		Under "Extension Details" click select file (note: the extension type will change automatically)
		Navigate to this directory and select ssl_scan_v1.py and press next
	
	Upon loading the extension, you will be prompted for a URL or IP address to run an sslyze scan. Press cancle if you do not want to run a scan just yet, otherwise, enter the desired URL or IP. The output will be saved in a file in the "sslyze_burp_output" directory
	
	Once the script is complete, unload this extension (uncheck the box that says loaded in table listing all your burp extensions)
	
	In order to run another scan, reload this extension (check the box that loaded). Again, you will be prompted for a URL or IP

note: this sofware contains a copy of an SSLyze distribution published by iSECPartners: https://github.com/iSECPartners

Author: Geoff Cohn