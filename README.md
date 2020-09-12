# 📬 Bloomberg Terminal Update Check

## 🗓 What's it do?

Check the internet to see if Bloomberg has released an update to their terminal software. Bloomberg releases updates to the software monthly, but without notice. Updates on the client are throttled and can frequently be slow. It is helpful to know when an update is available to allow for an update to be installed before user intervention. 

[Bloomberg Software](https://www.bloomberg.com/professional/downloads/)

Bloomberg has a standard format in the URL of their terminal update:
 
https://bdn-ak-ssl.bloomberg.com/software/trv/upgr09072020.exe

The tail of the URL is the date of release in the example, it would mean the update was made September 7, 2020.

## 👓 Example Usage 

Check out the main method when it is called. This is a very simple use case. 
The intention is to allow the code to be used within messaging or e-mail, and such that the message will only occur once a month. 

```
 if main(sys.argv) == True:
        print "An update is found!"
```

When an update is found a text file is created with the date of the update, and the 
positive feedback will only occur if the file in question does not exist, which allows for a cron job or task to be run daily calling the code. 

You might also have the code download the update and save for network deployment to selected terminals. 

## 🕸 Compatibility 

This will work on Python 3.8.x and is known to work on Windows and Linux, since macOS is similar it is assumed to work there, too. 

## 👽 Contributors

* Hexadecimalz
* Anonymous (with guidance from Hexadecimalz)
