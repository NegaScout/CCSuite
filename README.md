# CCSuite

Client communication loop:
 - START
 - Registered?
   - NO:
     - Generate SUID
     - Create log
   - YES:
     - Continue
 - Alive msg  to log
 - Check for new commands
   - NEW?
     - Execute
     - Append to log
   - NO?
     - Continue
 - Sleep xyz
 - Ping msg to log
