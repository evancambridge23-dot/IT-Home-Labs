import os

print("=== SYSTEM STATUS CHECK ===\n")

# Uptime
print("Uptime:")
os.system("uptime")
print("\n")

# Disk Usage
print("Disk Usage:")
os.system("df -h")
print("\n")

# Memory Usage
print("Memory Usage:")
os.system("free -h")
print("\n")