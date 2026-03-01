# IT Home Lab: Linux User Management

## Objective
Deploy a Linux server in a virtualized environment and simulate IT administrative tasks including user onboarding, group management, shared directory configuration, and permission assignment.

---

## Environment
* **Hypervisor:** Oracle VirtualBox
* **OS:** Ubuntu Server LTS
* **Hostname:** DriftwoodDragon
* **Primary Admin User:** evanc0323
* **Network:** DHCP assigned IP

---

## Lab Execution Steps

## Task 1 – System Verification
Validated system identity and network configuration to confirm the active administrative user and interface assignment.

bash
whoami
hostname
ip a

## Task 2 – User Onboarding Simulation
Created a new employee account and verified the entry within the system identity files.
Bash
sudo adduser employee1
cat /etc/passwd | grep employee1

## Task 3 – Shared Directory Configuration
Created a shared organizational directory and a test file to simulate a centralized file storage location for department collaboration.
Bash
sudo mkdir /companydata
sudo touch /companydata/project.txt

## Task 4 – Department Group Management
Created a department security group and added the new employee to the group to manage access levels.
Bash
sudo groupadd staff
sudo usermod -aG staff employee1

## Task 5 – Permission Assignment
Assigned group ownership and applied secure directory permissions to enforce the organizational security model.
Bash
sudo chown :staff /companydata
sudo chmod 770 /companydata

Permission Model Implemented:
Owner: Full access
Group: Full access
Others: No access
## Task 6 – Permission Testing & Troubleshooting
Switched to the employee account to validate directory access. Resolved an authentication error by resetting the employee password.
Bash
# Switch to the employee account
su - employee1

# If authentication fails, reset the password from the admin account:
sudo passwd employee1

# Successfully access the directory (Prompt should change to employee1@DriftwoodDragon)
cd /companydata
