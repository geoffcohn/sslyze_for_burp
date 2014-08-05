from burp import IBurpExtender
import subprocess
import os
import javax.swing as swing
import sys

class BurpExtender(IBurpExtender):

  def registerExtenderCallbacks(self, callbacks):    
    # your extension code here
    callbacks.setExtensionName("sslyze")
    #print "this is the current working directory: " + os.getcwd()

    sslyzePath = "sslyze9.0/sslyze.py"
    
    url = swing.JOptionPane.showInputDialog("Enter a URL or IP")
    print ("printing the url entered: " + url)

    fileName = url + "_sslyze"
    myFile = open(fileName,'w')


    process = subprocess.Popen(['python', sslyzePath, '--regular', url],
       stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    
   
    for line in process.stdout:
       myFile.write(line.rstrip(os.linesep) + '\n')
       #print line.rstrip(os.linesep) + '\n'

    myFile.write("this output was produced by SSLyze an open source project hosted at: https://github.com/iSECPartners/sslyze")
    myFile.close()
    
    originalPath = os.path.abspath(myFile.name)
    destinationPath = os.path.join(os.path.split(originalPath)[0], "sslyze_burp_output", fileName + ".txt")

    uniqueFile = False
    counter = 0
    while( uniqueFile == False):
        if os.path.isfile(destinationPath):
            destinationPath = os.path.join(os.path.split(destinationPath)[0], fileName + str(counter) + ".txt" )
            counter += 1
        else:
            uniqueFile = True

    print "outpute stored at: " + destinationPath

    os.rename(originalPath, destinationPath)

    print("done")
    


    return