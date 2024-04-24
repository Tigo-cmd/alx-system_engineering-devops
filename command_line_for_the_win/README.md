#command_line_for_the_win
Background Context

CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

Requirements
General

    A README.md file, at the root of the folder of the project, is mandatory
    This project will be manually reviewed.
    As each task is completed, the name of that task will turn green
    Create a screenshot, showing that you completed the required levels
    Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

Specific

In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

References :

    SFTP Guide
    SFTP File Transfer Tutorial

Here are the steps to follow:

    Take the screenshots of the completed levels as mentioned in the general requirements.
    Open a terminal or command prompt on your local machine.
    Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the hostname, username, and password provided to you for the sandbox environment.
    Once connected, navigate to the directory where you want to upload the screenshots.
    Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
    Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
    Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.
    Make sure to include the steps you followed to use the SFTP command-line tool in your project’s README.md file. This will help the reviewers understand how you performed the file transfer using SFTP.



#HOW TO USE

The SFTP (SSH File Transfer Protocol) put command is used to upload files from your local machine to a remote server. To use SFTP, you need to establish an SSH connection to the remote server first.

Here's a basic example of how you can use SFTP to upload files:

Open a terminal or command prompt on your local machine.

Connect to the remote server using SFTP:

	'sftp username@hostname'

Replace username with your username on the remote server and hostname with the hostname or IP address of the remote server.

Enter your password when prompted.

Navigate to the directory on the remote server where you want to upload the files:

	'cd /path/to/destination/directory'

Replace /path/to/destination/directory with the path to the directory where you want to upload the files.

Use the put command to upload the files:

	'put /path/to/local/file'

Replace /path/to/local/file with the path to the file you want to upload.

Repeat step 5 for each file you want to upload.

Once you've uploaded all the files, you can exit SFTP by typing:

		'exit'

