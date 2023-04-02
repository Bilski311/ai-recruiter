# AI Recruiter

Web app with AI generated IT interview questions

In order to run backend or generation scripts you need to configure your connection to mongo.
For MacOS:
Open the Terminal app on your Mac.
To edit the shell's configuration file, run the following command:
bash
Copy code
bash
vim ~/.bash_profile
This will open the bash_profile file in the Vim text editor.

In Vim, move the cursor to the end of the file and press the i key to enter insert mode.
Add the following line to set the MONGO_URI environment variable:
arduino
Copy code
export MONGO_URI="mongodb://username:password@<hostname>:27017/mydatabase"
Replace "username" and "password" with your actual credentials and replace <hostname> with a placeholder for the actual hostname. For example, you can use myhostname.local as a placeholder.

Press the Esc key to exit insert mode.

Type :wq and press Enter to save the changes and exit Vim.

To apply the changes to the shell, run the following command:

bash
Copy code
source ~/.bash_profile
Now the MONGO_URI environment variable will be available permanently on your machine.
