Objective

Deploy a Linux server in a virtualized environment and simulate IT administrative tasks including user onboarding, group management, shared directory configuration, and permission assignment.

Environment

Hypervisor: Oracle VirtualBox


OS: Ubuntu Server LTS


Hostname: DriftwoodDragon


Primary Admin User: evanc0323


Network: DHCP assigned IP




Task 1 – System Verification

Validated system identity and network configuration:
whoami


hostname


ip a


Confirmed the active administrative user, hostname configuration, and network interface assignment.



Task 2 – User Onboarding Simulation

Created new employee account: 
 sudo adduser employee1
Verified account creation:
 cat /etc/passwd | grep employee1




Task 3 – Shared Directory Configuration

Created a shared organizational directory and test file:
sudo mkdir /companydata
sudo touch /companydata/project.txt

This simulates a centralized file storage location for department collaboration.




Task 4 – Department Group Management

Created a department security group:
sudo groupadd staff

Added employee to group:
sudo usermod -aG staff employee1




Task 5 – Permission Assignment

Assigned group ownership:
sudo chown :staff /companydata

Applied secure directory permissions:
sudo chmod 770 /companydata

Permission Model implemented:
Owner: Full access


Group: Full access


Others: No access

This enforces controlled access aligned with organizational security practices.




Task 6 – Permission Testing & Troubleshooting

Switched to employee account:
su - employee1

Attempted to access shared directory:
cd /companydata

Encountered authentication error during testing. Resolved issue by resetting employee password:
sudo passwd employee1

if permissions set properly, it will change the name to “employee1@DriftwoodDragon”) 

cd /companydata 

Successfully validated directory access after correction.




Key Skills Demonstrated
Linux user management


Group-based access control


File system permissions


Troubleshooting authentication issues


Command-line administration
