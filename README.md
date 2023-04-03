# AI Recruiter

Web app with AI generated IT interview questions

MONGO CONNECTION:
For MacOS:
Open the Terminal app on your Mac.
To edit the shell's configuration file, run the following command:
vim ~/.zprofile
This will open the zprofile file in the Vim text editor.

In Vim, move the cursor to the end of the file and press the i key to enter insert mode.
Add the following line to set the MONGO_URI environment variable:
export MONGO_URI="mongodb://username:password@<hostname>:27017/mydatabase"
Replace "username" and "password" with your actual credentials and replace <hostname> with a placeholder for the actual hostname. For example, you can use myhostname.local as a placeholder.

Also add OPENAI_API_KEY variable in the same way.

Press the Esc key to exit insert mode.

Type :wq and press Enter to save the changes and exit Vim.
Restart terminal.
Now the MONGO_URI environment variable will be available permanently on your machine.

RUN BACK END:

Create a virtual environment using venv:
python3 -m venv venv

Activate the virtual environment:
source venv/bin/activate

Install the required packages from the requirements.txt file:
pip3 install -r requirements.txt

Remember to set the MONGO_URI variable as stated in MONGO_CONNECTION point

Run the Flask application:
python3 app.py
