# VSRepo

To use this script, make sure to replace the placeholder values in the configuration section with your actual email settings ($emailFrom, $emailTo, $smtpServer) and the path to your Tomcat logs directory ($tomcatLogsPath).

This script will run indefinitely, scanning the Tomcat logs every 5 minutes (as specified by $scanIntervalMinutes). It will send email notifications based on the status of the start operation and any errors or warnings found. It will also check if the server is in a hung state and not started properly.

You can save the script with a .ps1 extension (e.g., tomcat-log-scan.ps1), and then execute it from a PowerShell prompt or schedule it to run automatically using Task Scheduler.
