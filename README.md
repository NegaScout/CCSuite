# CCSuite

This is a simple implementation of a C&C channel for BSY assignment. It consists of
two components. client.py and server.py. Client has an execution loop (see below) where it
looks for new commands, executes them and uploads results and pings. Server is a REPL program,
which can dispatch several commands. See src/server/util/print_help/help_string.

Client communication loop:
 - START
 - Registered?
   - NO:
     - Create log
   - YES:
     - Continue
 - Alive msg  to log
 - :loop
 - Check for new commands
   - NEW?
     - Execute
     - Append to log
   - NO?
     - Continue
 - Sleep xyz
 - Ping msg to log
 - goto :loop

# Satisfying requirements
- _Both parts should use www.dropbox.com to communicate. You can register a free account and create a new application that uses the Python SDK (dropbox library) to upload and download files, etc._
  - The server and clients communicate through a log, which is hidden in an image with name of the client id
- _The controller should check if the bots are alive periodically_
  - The bot appends keepalive messages to log. The server can check online hosts with `local online` command
-  `w` command, **via** `remote <target_host_id> w`
-  `ls` command, **via** `remote <target_host_id> ls \*args`
-  `id` command, **via** `remote <target_host_id> id`
-  _Copy a file from the bot to the controller_ **via**
   -  `remote <target_host_id> upload <bot_local_path>`
   -  `local get <dropbox_path>`
-  _Execute a binary inside the bot given the name of the binary_ **via** `remote <target_host_id> <bot_local_path> *args`

# Instalation:
`pip install -r requirements.txt`

# Usage:
Just execute both src/client.py and src/server.py with `DROPBOX_TOKEN=<token>` environment variable
and issue commands to the server REPL

# Issues I know of:
- Hostname is not a unique identifier, multiple bots could connect to the same C&C chanel
- File uploads are not hidden. It is because the files could be arbitrary large and an image
has limited capacity of string length which can hide
- The log length is finite, for indefinite function, I would need to add 
  - `commit` msg type for server,
  that would indicate, that server has stored everything it wants up to this message and the client can clear it.
  - ping msg clearing, only last one is really important
  - string size reduction with some string encoding or compression
