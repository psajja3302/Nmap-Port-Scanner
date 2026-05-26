# Nmap-Port-Scanner
Utilizing the simple port scanner in the previous repo, we incorporate nmap in this scanner 

To use the nmap module, use Homebrew to install the nmap binary using (brew install nmap).
In order to use the nmap module, we will need to use (pip install python-nmap), but only after we set up a
virtual environment in VSCode. To do that, we use the commands (python -m venv .venv), (source .venv/bin/activate <- After this commmand, you will see the terminal use .venv)
, and (pip install python-nmap). Remember to do all this in your project directory. To verify the installation, use the command (nmap --version). After doing this, make sure
to switch your interpreter path to your current environment in order to utilize the nmap module. You can do this by using the command (which python3) to obtain
the path to your file, to which you then use the commands (Cmd + Shift + P) and look for "Python: Select Interpreter". Click "Enter interpreter path" and paste
the command you copied earlier.

Remember to use this tool responsibily and to be aware of the legal concerns.
https://nmap.org/book/legal-issues.html
