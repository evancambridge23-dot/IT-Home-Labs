**\#  Ubuntu Server Lab 3 – Security Hardening & Log Auditing**

**\#\#  Objective**

Simulate basic system security and monitoring tasks by:

\- Configuring a firewall using UFW  
\- Analyzing authentication logs  
\- Monitoring user activity and services  
\- Enhancing a Python script to log system reports

\#\#  Environment

\- Hypervisor: Oracle VM VirtualBox  
\- OS: Ubuntu Server LTS  
\- Network Mode: NAT (DHCP)  
\- Python Version: python3 \--version

\---

\#\# Firewall Configuration (UFW)

\#\#\# Check Firewall Status

\`\`\`bash  
sudo ufw status   
\`\`\`

\#\#\# Allow SSH Access (Port 22\) 

\`\`\`bash   
sudo ufw allow 22  
\`\`\`

\#\#\#  Enable Firewall 

\`\`\`bash   
sudo ufw enable  
\`\`\`

\#\#\# Verify Status

\`\`\`bash  
sudo ufw status verbose  
\`\`\`

\*\*Results:\*\* firewall enabled and SSH access permitted.

\#\#  Log File Analysis 

\#\#\#  Navigate to Logs 

\`\`\`bash   
cd /var/log  
\`\`\`

\#\#\#  View Authentication Logs 

\`\`\`bash  
sudo less auth.log  
\`\`\`

\#\#\# Filter Failed Login Attempts 

\`\`\`bash   
sudo grep "Failed password" /var/log/auth.log  
\`\`\`

\#\# User Monitoring 

\#\#\#  Active Users 

\`\`\`bash   
who  
\`\`\`

\#\#\#  Login History

\`\`\`bash   
last  
\`\`\`  
\*\*Results:\*\* Verified user sessions and login history.

\#\#  Service Monitoring

\`\`\`bash   
systemctl list-units \--type=service   
	\`\`\`  
\*\*Results:\*\* Displayed active system services (background processes). 

\#\# Python Automation

\`\`\`python

import os  
from datetime import datetime

log\_file \= "system\_report.txt"

with open(log\_file, "a") as f:  
    f.write("=== SYSTEM CHECK \===\\n")  
    f.write(f"Time: {datetime.now()}\\n\\n")

    f.write("Uptime:\\n")  
    os.system("uptime \>\> system\_report.txt")

    f.write("\\nDisk Usage:\\n")  
    os.system("df \-h \>\> system\_report.txt")

    f.write("\\nMemory Usage:\\n")  
    os.system("free \-h \>\> system\_report.txt")

    f.write("\\n----------------------\\n\\n")

print("System report saved to system\_report.txt")  
\`\`\`

\#\# Execute Script 

\`\`\`bash  
python3 system\_check.py  
\`\`\`

\#\# View Results 

\`\`\`bash   
cat system\_report.txt  
\`\`\`

\#\#  UFW Firewall  
\! \[Firewall Status\](Screenshots/FirewallStatus.png)

\#\#  View Authentication Logs  
\! \[Authentication Logs\](Screenshots/AdminLogs.png)

\#\# Monitor User Activity  
\! \[User Monitoring\](Screenshots/UserMonitoring.png)

\#\# Check Running Background Services  
\! \[Check Services\](Screenshots/RunningServices.png)

\#\# Python Automated System Check  
\! \[System Check\](Screenshots/SystemReportOutput.png)