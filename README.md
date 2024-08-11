# Currrency-Exchange-Rate-Monitor
Goal: Web scraping currency exchange rate from internet and send current rate to email 

## Instructions:
*CERM_daily_report.py*: the main python code that do the web scraping, and sending emails.

*.env*: config file to store password which is not included here in this repository, can create own .env file and store under the same directory with the CERM_daily_report.py file

*run_script.sh*: the shell script to activate venv and run the CERM_daily_report.py and then deactivate the venv - by activating venv in shell can help to solve issues like missing python package installed in your local pc/laptop if you are running venv for debugging codes which means you may only install packages in your venv. 

### Cron setup: 
OS system: macos 
1. Command+space to open terminal
2. cd to your project path
3. type in command: crontab -e
4. press 'I' to insert contents: 0 9 * * * export VENV_PATH="path/to/your/venv" && /path/to/run_script.sh >> /path/to/output.log 2>&1
5. press esc+wq to save and quit
6. type in command: crontab -l to verity your cron job is set up correctly
#### Troubleshooting cron:
Check output.log to see if your cron job was run successfully, if see error like 'operation not permitted', check following few possibilities (that I came across):
1. Verify directory permissions: ls -ld /path/to
2. Verify output.log permissions: ls -l output.log
3. Adding full disk access in macos if you put your project under directories like Documents/Downloads/etc - regarding how to add full disk access: command+space to search security&privacy and then privacy, click full disk access preferences.
  a. tip1: command+shift+period to show hidden files
  b. tip2: navigate to directory usr/sbin and find exact 'cron' file


