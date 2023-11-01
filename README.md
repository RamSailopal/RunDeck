# RunDeck SCM change import automation

![example workflow](https://github.com/RamSailopal/RunDeck/actions/workflows/lint.yml/badge.svg)

The current implementation of RunDeck required a manual step to "pull" changes made on a given repo into RunDeck either as additional jobs or as job modification.

This repo offers a solution and allows the automated import of any changes.

## Process

1)  Ensure that **Python3** is installed on the RunDeck server as well as **Python3-pip**
2)  Install the Python **requests** library through:

        sudo su rundeck
        pip3 install requests
        exit

4) Copy the **import.py** code into a new file located a given location on the Rundeck server that can be accessible by the **rundeck** user.

5)  Modify the TOKEN variable to reference your actual RunDeck API token.

6)  Given the script execute permissions:

        chmod o+x import.py

7) Modify the following line in the **Test/import.yaml** file:

   
   **command: python3 '/home/rundeck/import.py'**

Change **/home/rundeck/import.py** to the location of the file on the server.

8) Manually setup and import the repository, following [this](https://docs.rundeck.com/docs/learning/howto/how2scm.html#exporting-jobs-continued) guide.

Through the import.py script running every minute, new repo changes will automatically get imported and "synced" with RunDeck.

## Testing

A containerised local instance of RunDeck can be run with:

        docker run --name some-rundeck -p 4440:4440 rundeck/rundeck:4.17.1

Navigate to the containers command line through:

        docker exec -it some-rundeck /bin/bash

Follow the process steps referenced above.

To access the web console, navigate to http://localhost:4440 with the credentials:

Username: **admin**
Password: **admin**