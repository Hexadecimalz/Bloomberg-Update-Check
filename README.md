# Bloomberg Update Check

## Synopsis 

Check the internet to see if Bloomberg has released an update to their terminal software. Bloomberg releases updates to the software monthly, but without notice. Updates on the client are throttled and can frequently be slow. It is helpful to know when an update is available to allow for an update to be installed before user intervention. 

[Bloomberg Software](https://www.bloomberg.com/professional/downloads/)

Bloomberg has a standard format in the URL of their terminal update:
 
[http://bdn-ak.bloomberg.com/software/trv/**upgr03072017.exe**](http://bdn-ak.bloomberg.com/software/trv/upgr03072017.exe)

The tail of the URL is the date of release in the example, it would mean the update was made March 7, 2017. 

## Example Usage 

Check out the main method when it is called. This is a very simple use case. 
The intention is to allow the code to be used within messaging or e-mail, and such that the message will only occur once a month. 

```
 if main(sys.argv) == True:
        print "An update is found!"
```

When an update is found a text file is created with the date of the update, and the 
positive feedback will only occur if the file in question does not exist, which allows for a cron job or task to be run daily calling the code. 

You might also have the code download the update and save for network deployment to selected terminals. 

## Compatibility 

This will work on Python 2.7.x and is known to work on Windows and Linux, since macOS is similar it is assumed to work there, too. Your Cron job should have rights to write files or the code will ping each time the task runs. 

## Contributors

* Hexadecimalz
* Anonymous (with guidance from Hexadecimalz)

## Issues 

This is my first project using GitHub, please be kind and contribute. For example, the code assumes all months have 31 days, because it did not seem significant enough to modify for the small variances in the calendar. 