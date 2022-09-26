print("                                 Security + Practice Exam 1 (90 multiple choice questions score at end of exam) Goodluck :) \n")
score = 0

# Question 1

answer1 = input("#1. You’ve hired a third-party to gather information about your company’s servers and data.\nThe third-party will not have direct access to your internal network but can gather information from any others.\nWhich of the following would BEST describe this approach? \n \na. Backdoor testing \nb. Passive footprinting \nc. OS fingerprinting \nd. Partially known environment \nAnswer: ")
if answer1 == "b" or answer1 == "Passive footprinting":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.8 - Reconnaissance")
	print("\n")
else:
	print("Incorrect: The answer is b. Passive footprinting")
	print("Score:", score)
	print("SY0-601, Objective 1.8 - Reconnaissance")
	print("\n")

# Question 2

answer2 = input("#2.Which of these protocols use TLS to provide secure communication? \n \na. HTTPS and FTPS \nb. SSH \nc. SNMPv2 \nd. DNSSEC \ne. SRTP \nAnswer: ")
if answer2 == "a" or answer2 == "HTTPS and FTPS":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.1 - Secure Protocols")
	print("\n")
else:
	print("Incorrect: The answer is a. HTTPS")
	print("Score:", score)
	print("SY0-601, Objective 3.1 - Secure Protocols")
	print("\n")

# Question 3

answer3 = input("#3. Which of these threat actors would be MOST likely to attack systems for direct financial gain? \n \na. Organized crime \nb. Hacktivist \nc. Nation state \nd. Competitor \nAnswer: ")
if answer3 == "a" or answer3 == "Organized crime ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.5 - Threat Actors SY0-601, Objective 1.5 - Threat Actors")
	print("\n")
else:
	print("Incorrect: The answer is a. Organized crime")
	print("Score:", score)
	print("SY0-601, Objective 1.5 - Threat Actors SY0-601, Objective 1.5 - Threat Actors")
	print("\n")
	
# Question 4

answer4 = input("#4. A security incident has occurred on a file server. Which of the following data sources should be gathered to address file storage volatility? \n \na. Paritiion data and temporary file systems \nb. Kernal statistics \nc. ROM data \nd. Process table \n Answer: ")
if answer4 == "a" or answer4 == "Paritiion data and temporary file systems":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.5 - Forensics Data Acquisition")
	print("\n")
else:
	print("Incorrect: The answer is a. Paritiion data and temporary file systems")
	print("Score:", score)
	print("SY0-601, Objective 4.5 - Forensics Data Acquisition")
	print("\n")

# Question 5

answer5 = input("#5. An IPS at your company has found a sharp increase in traffic from all-in-one printers. After researching, your security team has found vulnerability associated with these devices that allows the device to be remotely controlled by a third-party. Which category would BEST describe these devices? \n \na. IoT \nb. RTOS  \nc. MFD  \nd. SoC \nAnswer: ")
if answer5 == "c" or answer5 == "MFD":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.6 - Embedded Systems")
	print("\n")
else:
	print("Incorrect: The answer is c. MFD")
	print("Score:", score)
	print("SY0-601, Objective 2.6 - Embedded Systems")
	print("\n")

# Question 6

answer6 = input("#6. Which of the following standards provides information on privacy and managing PII? \n \na. ISO 31000 \nb. ISO 27002  \nc. ISO 27701  \nd. ISO 27001 \nAnswer! ")
if answer6 == "c" or answer6 == "ISO 27701":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.2 - Security Frameworks")
	print("\n")
else:
	print("Incorrect: The answer is c. ISO 27701")
	print("Score:", score)
	print("SY0-601, Objective 5.2 - Security Frameworks")
	print("\n")

# Question 7

answer7 = input("#7. Elizabeth, a security administrator, is concerned about the potential for data exfiltration using external storage drives. Which of the following would be the BEST way to prevent this method of data exfiltration? \n \na. Create an operating system security policy to prevent the use of removable media \nb. Monitor removable media usage in host-based firewall logs  \nc. Only allow applications that do not use removable media  \nd. Define a removable media block rule in the UTM \nAnswer: ")
if answer7 == "a" or answer7 == "Create an operating system security policy to prevent the use of removable media":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.5 - Attack Vectors")
	print("\n")
else:
	print("Incorrect: The answer is a. Create an operating system security policy to prevent the use of removable media")
	print("Score:", score)
	print("SY0-601, Objective 1.5 - Attack Vectors")
	print("\n")

# Question 8

answer8 = input("#8. A CISO (Chief Information Security Officer) would like to decrease the response time when addressing security incidents. Unfortunately, the company does not have the budget to hire additional security engineers. Which of the following would assist the CISO with this requirement? \n \na. ISO 27701 \nb. PKI \nc. IaaS  \nd. SOAR \nAnswer! ")
if answer8 == "d" or answer8 == "SOAR":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.4 - Security Configurations")
	print("\n")
else:
	print("Incorrect: The answer is d. SOAR")
	print("Score:", score)
	print("SY0-601, Objective 4.4 - Security Configurations")
	print("\n")

# Question 9

answer9 = input("#9 An insurance company has created a set of policies to handle data breaches. The security team has been given this set of requirements based on these policies: Access records from all devices must be saved and archived, Any data access outside of normal working hours must be immediately reported, Data access must only occur inside of the country, Access logs and audit reports must be created from a single databas,  \n \na. Restrict login access by IP address and GPS location, Consolidate all logs on a SIEM, Enable time-of-day restrictions on the authentication server \nb. Require government-issued identification during the onboarding process \nc. Add additional password complexity for accounts that access data \nd. Conduct monthly permission auditing \nAnswer: ")
if answer9 == "a" or answer9 == "a":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.7 - Account Policies")
	print("\n")
else:
	print("Incorrect: The answer is a. Restrict login access by IP address and GPS location, Consolidate all logs on a SIEM, Enable time-of-day restrictions on the authentication server ")
	print("Score:", score)
	print("SY0-601, Objective 3.7 - Account Policies")
	print("\n")
	
# Question 10

answer10 = input("#10 Rodney, a security engineer, is viewing this record from the firewall logs: UTC  04/05/2018  03:09:15809	AV Gateway Alert 136.127.92.171	80  ->  10.16.10.14	60818 Gateway Anti-Virus Alert: XPACK.A_7854 (Trojan) blocked. Which of the following can be observed from this log information? \n \na. The victim's IP address is 136.127.92.171 \nb. A download was blocked from a web server \nc. A botnet DDoS attack was blocked \nd. The Trojan was blocked, but the file was not \nAnswer: ")
if answer10 == "b" or answer10 == " A download was blocked from a web server ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.3 - Log Files")
	print("\n")
else:
	print("Incorrect: The answer is b. A download was blocked from the web server ")
	print("Score:", score)
	print("SY0-601, Objective 4.3 - Log Files")
	print("\n")

# Question 11

answer11 = input("#11 A user connects to a third-party website and receives this message: Your connection is not private. NET::ERR_CERT_INVALID Which of the following attacks would be the MOST likely reason for this message? \n \na. Brute force \nb. DoS \nc. On-Path \nd. Disassociation \nAnswer: ")
if answer11 == "c" or answer11 == "On-Path":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.4 - On-Path Attacks")
	print("\n")
else:
	print("Incorrect: The answer is c. On-Path")
	print("Score:", score)
	print("SY0-601, Objective 1.4 - On-Path Attacks")
	print("\n")

# Question 12

answer12 = input("#12 Which of the following would be the BEST way to provide a website login using existing credentials from a third-party site? \n \na. Federation \nb. 802.1X \nc. PEAP \nd. EAP-FAST \nAnswer: ")
if answer12 == "a" or answer12 == "Federation":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.4 - Authentication Methods")
	print("\n")
else:
	print("Incorrect: The answer is a. Federation")
	print("Score:", score)
	print("SY0-601, Objective 2.4 - Authentication Methods")
	print("\n")

# Question 13

answer13 = input("#13 A system administrator, Daniel, is working on a contract that will specify a minimum required uptime for a set of Internet-facing firewalls. Daniel needs to know how often the firewall hardware is expected to fail between repairs. Which of the following would BEST describe this information? \n \na. MTBF \nb. RTO \nc. MTTR \nd. MTTF \nAnswer: ")
if answer13 == "a" or answer13 == "MTBF (Mean Time Between Failures":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("\n")
else:
	print("Incorrect: The answer is a. MTBF (Mean Time Between Failures")
	print("Score:", score)
	print("\n")

# Question 14

answer14 = input("#14 An attacker calls into a company’s help desk and pretends to be the director of the company’s manufacturing department. The attacker states that they have forgotten their password and they need to have the password reset quickly for an important meeting. What kind of attack would BEST describe this phone call? \n \na. Social Engineering \nb. Tailgating \nc. Watering hole \nd. On-path \nAnswer: ")
if answer14 == "a" or answer14 == "Social Engineering":
	score += 1
	print("Correct!")
	print("SY0-601, Objective 1.1 - Principles of Social Engineering")
	print("Score:", score)
	print("\n")
else:
	print("Incorrect: The answer is a. Social Engineering")
	print("Score:", score)
	print("SY0-601, Objective 1.1 - Principles of Social Engineering")
	print("\n")

# Question 15

answer15 = input("#15 A security administrator has been using EAP-FAST wireless authentication since the migration from WEP to WPA2. The company’s network team now needs to support additional authentication protocols inside of an encrypted tunnel. Which of the following would meet the network team’s requirements?\n \na. EAP-TLS \nb. PEAP \nc. EAP-TTLS \nd. EAP-MSCHAPv2 \nAnswer: ")
if answer15 == "c" or answer15 == "EAP-TTLS":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.4 - Wireless Authentication Protocols")
	print("\n")
else:
	print("Incorrect: The answer is c. EAP-TTLS")
	print("Score:", score)
	print("SY0-601, Objective 3.4 - Wireless Authentication Protocols")
	print("\n")

# Question 16

answer16 = input("#16 Which of the following would be commonly provided by a CASB? \n \na. List of all internal Windows devices that have not installed the latest security patches \nb. List of applications in use and verification of encrypted data transfers \nc. Centralized log storage facility \nd. List of network outages for the previous month \nAnswer: ")
if answer16 == "b" or answer16 == "List of applications in use and verification of encrypted data transfers":
	score += 1
	print("Correct!")
	print("SY0-601, Objective 3.6 - Cloud Security Solutions")
	print("Score:", score)
	print("\n")
else:
	print("Incorrect: The answer is b. List of applications in use and verification of encrypted data transfers")
	print("Score:", score)
	print("SY0-601, Objective 3.6 - Cloud Security Solutions")
	print("\n")

# Question 17

answer17 = input("#17 The embedded OS in a company’s time clock appliance is configured to reset the file system and reboot when a file system error occurs. On one of the time clocks, this file system error occurs during the startup process and causes the system to constantly reboot. Which of the following BEST describes this issue? \n \na. DLL injection \nb. Resource exhaustion \nc. Race condition \nd. Weak configuration \nAnswer: ")
if answer17 == "c" or answer17 == "Race condition":
	score += 1
	print("Correct!")
	print("SY0-601, Objective 1.3 - Race Conditions")
	print("Score:", score)
	print("\n")
else:
	print("Incorrect: The answer is c. Race condition")
	print("Score:", score)
	print("SY0-601, Objective 1.3 - Race Conditions")
	print("\n")

# Question 18

answer18 = input("#18 A recent audit has found that existing password policies do not include any restrictions on password attempts, and users are not required to periodically change their passwords. Which of the following would correct these policy issues?\n \na. Password complexity \nb. Password expiration and lockout \nc. Password history \nd. Password recovery \nAnswer: ")
if answer18 == "b" or answer18 == "Password expiration and lockout":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.7 - Account Policies")
	print("\n")
else:
	print("Incorrect: The answer is b. Password expiration and lockout ")
	print("Score:", score)
	print("SY0-601, Objective 3.7 - Account Policies")
	print("\n")

# Question 19

answer19 = input("#19 What kind of security control is associated with a login banner? \n \na. Preventive \nb. Deterrent \nc. Corrective \nd. Detective \ne. Compensating \nf. Physical \nAnswer: ")
if answer19 == "b" or answer19 == "Deterrent":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.1 - Security Controls")
	print("\n")
else:
	print("Incorrect: The answer is b. Deterrent")
	print("Score:", score)
	print("SY0-601, Objective 5.1 - Security Controls")
	print("\n")

# Question 20

answer20 = input("#20 A security team has been provided with a non-credentialed vulnerability scan report created by a third-party. Which of the following would they expect to see on this report? \n \na. A summary of all files with invalid group assignments \nb. A list of all unpatched operating systems files \nc. The version of web server software in use \nd. A list of local user accounts \nAnswer: ")
if answer20 == "c" or answer20 == "The version of web server software in use":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.7 - Vulnerability Scans")
	print("\n")
else:
	print("Incorrect: The answer is c. The version of web server software in use")
	print("Score:", score)
	print("SY0-601, Objective 1.7 - Vulnerability Scans")
	print("\n")

# Question 21

answer21 = input("#21 A business manager is documenting a set of steps for processing orders if the primary Internet connection fails. Which of these would BEST describe these steps? \n \na. Communication plan \nb. Continuity of operations \nc. Stakeholder management \nd. Tabletop exercise \nAnswer: ")
if answer21 == "b" or answer21 == "Continuity of operations":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.2 - Incident Response Planning")
	print("\n")
else:
	print("Incorrect: The answer is b. Continuity of operations")
	print("Score:", score)
	print("SY0-601, Objective 4.2 - Incident Response Planning")
	print("\n")

# Question 22

answer22 = input("#22 A security administrator is concerned about data exfiltration resulting from the use of malicious phone charging stations. Which of the following would be the BEST way to protect against this threat? \n \na. USB data blocker \nb. Personal firewall \nc. MFA \nd. FDE \nAnswer: ")
if answer22 == "a" or answer22 == "USB data blocker":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.7 - Physical Security Controls")
	print("\n")
else:
	print("Incorrect: The answer is a. USB data blocker ")
	print("Score:", score)
	print("SY0-601, Objective 2.7 - Physical Security Controls")
	print("\n")

# Question 23

answer23 = input("#23 A company would like to protect the data stored on laptops used in the field. Which of the following would be the BEST choice for this requirement? \n \na. MAC \nb. SED \nc. CASB \nd. SOAR \nAnswer: ")
if answer23 == "b" or answer23 == "SED":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.2 - Application Hardening")
	print("\n")
else:
	print("Incorrect: The answer is b. SED (Self-Encrypting Drive)")
	print("Score:", score)
	print("SY0-601, Objective 3.2 - Application Hardening")
	print("\n")

# Question 24

answer24 = input("#24 A file server has a full backup performed each Monday at 1 AM. Incremental backups are performed at 1 AM on Tuesday, Wednesday, Thursday, and Friday. The system administrator needs to perform a full recovery of the file server on Thursday afternoon. How many backup sets would be required to complete the recovery? \n \na. 2 \nb. 3 \nc. 4 \nd. 1 \nAnswer: ")
if answer24 == "c" or answer24 == "4":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.5 - Backup Types")
	print("\n")
else:
	print("Incorrect: The answer is c. 4 ")
	print("Score:", score)
	print("SY0-601, Objective 2.5 - Backup Types")
	print("\n")

# Question 25

answer25 = input("#25 A company is creating a security policy that will protect all corporate mobile devices: All mobile devices must be automatically locked after a predefined time period. Some mobile devices will be used by the remote sales teams, so the location of each device needs to be traceable. All of the user’s information should be completely separated from company data. Which of the following would be the BEST way to establish these security policy rules?\n \na. Containerization \nb. Biometrics \nc. COPE \nd. VDI \ne. Geofencing \nf. MDM \nAnswer: ")
if answer25 == "f" or answer25 == "MDM":
	score += 1

	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.5 - Mobile Device Management")
	print("\n")
else:
	print("Incorrect: The answer is f. MDM")
	print("Score:", score)
	print("SY0-601, Objective 3.5 - Mobile Device Management")
	print("\n")

# Question 26

answer26 = input("#26 A security engineer runs a monthly vulnerability scan. The scan doesn’t list any vulnerabilities for Windows servers, but a significant vulnerability was announced last week and none of the servers are patched yet. Which of the following best describes this result? \n \na. Exploit \nb. Credentialed \nc. Zero-day attack \nd. False negative \nAnswer: ")
if answer26 == "d" or answer26 == "False negative":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.7 - Vulnerability Scans")
	print("\n")
else:
	print("Incorrect: The answer is d. False negative ")
	print("Score:", score)
	print("SY0-601, Objective 1.7 - Vulnerability Scans")
	print("\n")

# Question 27

answer27 = input("#27 A security administrator is adding additional authentication controls to the existing infrastructure. Which of the following should be added by the security administrator? \n \na. TOTP and Smart Card \nb. Least privilege \nc. Role-based awareness training \nd. Separation of duties \ne. Job rotation \nAnswer: ")
if answer27 == "a" or answer27 == "TOTP and Smart Card":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.4 - Authentication Methods")
	print("\n")
else:
	print("Incorrect: The answer is a. TOTP and Smart Card ")
	print("Score:", score)
	print("SY0-601, Objective 2.4 - Authentication Methods")
	print("\n")

# Question 28

answer28 = input("#28 A network administrator would like each user to authenticate with their personal username and password when connecting to the company's wireless network. Which of the following should the network administrator configure on the wireless access points? \n \na. WPA2-PSK \nb. 802.1X \nc. WPS \nd. WPA2-AES \nAnswer: ")
if answer28 == "b" or answer28 == "802.1X":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.4 - Wireless Authentication Protocols")
	print("\n")
else:
	print("Incorrect: The answer is b. 802.1X")
	print("Score:", score)
	print("SY0-601, Objective 3.4 - Wireless Authentication Protocols")
	print("\n")

# Question 29

answer29 = input("29 A security administrator needs to identify all references to a Javascript file in the HTML of a web page. Which of the following tools should be used to view the source of the web page and search through the file for a specific filename? \n \na. tail \nb. openssl \nc. scanless \nd. grep and curl \ne. Nmap \nf. head \nAnswer: ")
if answer29 == "d" or answer29 == "grep and curl":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.1 - Reconnaissance Tools Part 2")
	print("\n")
else:
	print("Incorrect: The answer is d. grep and curl")
	print("Score:", score)
	print("SY0-601, Objective 4.1 - Reconnaissance Tools Part 2")
	print("\n")

# Question 30

answer30 = input("#30 A user has assigned individual rights and permissions to a file on their network drive. The user adds three additional individuals to have read- only access to the file. Which of the following would describe this access control model? \n \na. DAC \nb. MAC \nc. ABAC \nd. RBAC \nAnswer: ")
if answer30 == "a" or answer30 == "DAC":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.8 - Access Control")
	print("\n")
else:
	print("Incorrect: The answer is a. DAC (Discretionary Access Control)")
	print("Score:", score)
	print("SY0-601, Objective 3.8 - Access Control")
	print("\n")

# Question 31

answer31 = input("#31 A remote user has received a text message requesting login details to the corporate VPN server. Which of the following would BEST describe this message? \n \na. Brute force \nb. Prepending \nc. Typosquatting \nd. Smishing \nAnswer: ")
if answer31 == "d" or answer31 == "Smishing":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.1 - Phishing")
	print("\n")
else:
	print("Incorrect: The answer is d. Smishing")
	print("Score:", score)
	print("SY0-601, Objective 1.1 - Phishing")
	print("\n")

# Question 32

answer32 = input("#32 A department store policy requires that a floor manager approves each transaction when a gift certificate is used for payment. The security team has found that some of these transactions have been processed without the approval of a manager. Which of the following would provide a separation of duties to enforce this store policy? \n \na. Use a WAF to monitor all gift certificate transactions \nb. Disable all gift certificates transactions for cashiers \nc. Implement a discretionary access control policy \nd. Require an approval PIN for the cashier and a separate approval PIN for manager \nAnswer: ")
if answer32 == "d" or answer32 == "Require an approval PIN for the cashier and a separate approval PIN for manager":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.3 - Personnel Security ")
	print("\n")
else:
	print("Incorrect: The answer is d. Require an approval PIN for the cashier and a separate approval PIN for manager")
	print("Score:", score)
	print("SY0-601, Objective 5.3 - Personnel Security ")
	print("\n")

# Question 33

answer33 = input("#33 Which of the following is true of a rainbow table?  \n \na. The rainbow table is built in real-time during the attack \nb. Rainbow tables are the most effective online attack type \nc. Rainbow tables require significant CPU cycles at attack time \nd. Different tables are required for different hashing methods, and it won’t be useful if the passwords are salted \nAnswer: ")
if answer33 == "d" or answer33 == " Different tables are required for different hashing methods and it won’t be useful if the passwords are salted ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.2 - Password Attacks ")
	print("\n")
else:
	print("Incorrect: The answer is d. Different tables are required for different hashing methods and it won’t be useful if the passwords are salted ")
	print("Score:", score)
	print("SY0-601, Objective 1.2 - Password Attacks ")
	print("\n")

# Question 34

answer34 = input("#34 A server administrator at a bank has noticed a decrease in the number of visitors to the bank's website. Additional research shows that users are being directed to a different IP address than the bank's web server. Which of the following would MOST likely describe this attack? \n \na. Disassociation \nb. DDoS \nc. Buffer overflow \nd. DNS poisoning \nAnswer: ")
if answer34 == "d" or answer34 == "DNS poisoning":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.4 - DNS Attacks ")
	print("\n")
else:
	print("Incorrect: The answer is d. DNS poisoning")
	print("Score:", score)
	print("SY0-601, Objective 1.4 - DNS Attacks ")
	print("\n")

# Question 35

answer35 = input("#35 Which of these cloud deployment models would share resources between a private virtualized data center and externally available cloud services? \n \na. SaaS \nb. Community \nc. Hybrid \nd. Containerization \nAnswer: ")
if answer35 == "c" or answer35 == "Hybrid":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.2 - Cloud Models ")
	print("\n")
else:
	print("Incorrect: The answer is c. Hybrid")
	print("Score:", score)
	print("SY0-601, Objective 2.2 - Cloud Models ")
	print("\n")

# Question 36

answer36 = input("#36 A company hires a large number of seasonal employees, and their system access should normally be disabled when the employee leaves the company. The security administrator would like to verify that their systems cannot be accessed by any of the former employees. Which of the following would be the BEST way to provide this verification? \n \na. Confirm that no unauthorized accounts have administrator access \nb. Validate the account lockout policy \nc. Validate the processes and procedures for all outgoing employees \nd. Create a report that shows all authentications for a 24-hr period \nAnswer: ")
if answer36 == "c" or answer36 == "Validate the processes and procedures for all outgoing employees":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.3 - Personnel Security ")
	print("\n")
else:
	print("Incorrect: The answer is c. Validate the processes and procedures for all outgoing employees")
	print("Score:", score)
	print("SY0-601, Objective 5.3 - Personnel Security ")
	print("\n")

answer37 = input("#37 A network administrator has installed a new access point, but only a portion of the wireless devices are able to connect to the network. Other devices can see the access point, but they are not able to connect even when using the correct wireless settings. Which of the following security features was MOST likely enabled? \n \na. MAC filtering \nb. SSID broadcast suppression \nc. 802.1X authentication \nd. Anti-spoofing \nAnswer: ")
if answer37 == "a" or answer37 == "MAC filtering":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.3 - Port Security ")
	print("\n")
else:
	print("Incorrect: The answer is a MAC filtering")
	print("Score:", score)
	print("SY0-601, Objective 3.3 - Port Security ")
	print("\n")

# Question 38

answer38 = input("#38 Active Connections \n Proto Local Address Foreign Address State PID \n TCP 192.168.1.14:49194 75.125.212.75:http CLOSE_WAIT 2948 \n TCP 192.168.1.14:49196 a795sm:http CLOSE_WAIT 2948 \n TCP 192.168.1.14:49197 a795sm:http CLOSE_WAIT 2948 \n Which of the following is being used to create this information? \n \na. tracert \nb. netstat \nc. dig \nd. netcat \nAnswer: ")
if answer38 == "b" or answer38 == "netstat":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.1 - Reconnaissance Tools Part 1 ")
	print("\n")
else:
	print("Incorrect: The answer is b. netstat")
	print("Score:", score)
	print("SY0-601, Objective 4.1 - Reconnaissance Tools Part 1 ")
	print("\n")

# Question 39

answer39 = input("#39 An attacker has discovered a way to disable a server by sending specially crafted packets from many remote devices to the operating system. When the packet is received, the system crashes and must be rebooted to restore normal operations. Which of the following would BEST describe this attack? \n \na. Privilege escalation \nb. Spoofing \nc. Replay attack \nd. DDoS \nAnswer: ")
if answer39 == "d" or answer39 == "DDoS":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.4 - Denial of Service ")
	print("\n")
else:
	print("Incorrect: The answer is d. DDoS (Distributed Denial of Service ")
	print("Score:", score)
	print("SY0-601, Objective 1.4 - Denial of Service ")
	print("\n")

# Question 40

answer40 = input("#40 A data breach has occurred in a large insurance company. A security administrator is building new servers and security systems to get all of the financial systems back online. Which part of the incident response process would BEST describe these actions? \n \na. Lessons learned \nb. Isolation and containment \nc. Reconstitution \nd. Precursors \nAnswer: ")
if answer40 == "c" or answer40 == "Reconstitution":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.2 - Incident Response Process ")
	print("\n")
else:
	print("Incorrect: The answer is c. Reconstitution")
	print("Score:", score)
	print("SY0-601, Objective 4.2 - Incident Response Process ")
	print("\n")

# Question 41

answer41 = input("#41 A manufacturing company has moved an inventory application from their internal systems to a PaaS service. Which of the following would be the BEST way to manage security policies on this new service? \n \na. DLP \nb. SIEM \nc. IPS \nd. CASB \nAnswer: ")
if answer41 == "d" or answer41 == "CASB":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.6 - Cloud Security Solutions ")
	print("\n")
else:
	print("Incorrect: The answer is d. CASB (Cloud Access Security Broker ")
	print("Score:", score)
	print("SY0-601, Objective 3.6 - Cloud Security Solutions ")
	print("\n")

# Question 42

answer42 = input("#42 An organization has identified a significant vulnerability in a firewall that was recently installed for Internet connectivity. The firewall company has stated there are no plans to create a patch for this vulnerability. Which of the following would BEST describe this issue? \n \na. Lack of vendor support \nb. Improper input handling \nc. Improper key management \nd. End-of-life \nAnswer: ")
if answer42 == "a" or answer42 == "Lack of vendor support":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.6 - Third-party Risks ")
	print("\n")
else:
	print("Incorrect: The answer is a. Lack of vendor support")
	print("Score:", score)
	print("SY0-601, Objective 1.6 - Third-party Risks ")
	print("\n")

# Question 43

answer43 = input("#43 A company has decided to perform a disaster recovery exercise during an annual meeting with the IT directors and senior directors. A simulated disaster will be presented, and the participants will discuss the logistics and processes required to resolve the disaster. Which of the following would BEST describe this exercise? \n \na. After-action report \nb. Business impact analysis \nc. Alternate business practice \nd. Tabletop exercise \nAnswer: ")
if answer43 == "d" or answer43 == "Tabletop exercise":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.2 - Incident Response Planning ")
	print("\n")
else:
	print("Incorrect: The answer is d. Tabletop exercise ")
	print("Score:", score)
	print("SY0-601, Objective 4.2 - Incident Response Planning ")
	print("\n")

# Question 44

answer44 = input("#44 A security administrator needs to identify all computers on the company network infected with a specific malware variant. Which of the following would be the BEST way to identify these systems? \n \na. Honeynet \nb. Data masking \nc. DNS sinkhole \nd. DLP \nAnswer: ")
if answer44 == "c" or answer44 == "DNS sinkhole":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.1 - Honeypots and Deception ")
	print("\n")
else:
	print("Incorrect: The answer is d. DNS sinkhole")
	print("Score:", score)
	print("SY0-601, Objective 2.1 - Honeypots and Deception ")
	print("\n")

# Question 45

answer45 = input("#45 A system administrator has been called to a system that is suspected to have a malware infection. The administrator has removed the device from the network and has disconnected all USB flash drives. Which of these incident response steps is the administrator following? \n \na. Lessons learned \nb. Containment \nc. Detection \nd. Reconstitution \nAnswer: ")
if answer45 == "b" or answer45 == "Containment":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.2 - Incident Response Process ")
	print("\n")
else:
	print("Incorrect: The answer is b. Containment")
	print("Score:", score)
	print("SY0-601, Objective 4.2 - Incident Response Process ")
	print("\n")

# Question 46

answer46 = input("#46 How can a company ensure that all data on a mobile device is unrecoverable if the device is lost or stolen? \n \na. Containerization \nb. Geofencing \nc. Screen locks \nd. Remote wipe \nAnswer: ")
if answer46 == "d" or answer46 == "Remote wipe":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.5 - Mobile Device Management ")
	print("\n")
else:
	print("Incorrect: The answer is d. Remote wipe ")
	print("Score:", score)
	print("SY0-601, Objective 3.5 - Mobile Device Management ")
	print("\n")

# Question 47

answer47 = input("#47 A security administrator is collecting information associated with a ransomware infection on the company's web servers. Which of the following log files would provide information regarding the memory contents of these servers? \n \na. Web \nb. Packet \nc. Dump \nd. DNS \nAnswer: ")
if answer47 == "c" or answer47 == "Dump":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.3 - Log Files ")
	print("\n")
else:
	print("Incorrect: The answer is c. Dump")
	print("Score:", score)
	print("SY0-601, Objective 4.3 - Log Files ")
	print("\n")

# Question 48

answer48 = input("#48 Which part of the PC startup process verifies the digital signature of the OS kernel? \n \na. Measured Boot \nb. Trusted Boot \nc. Secure Boot \nd. POST \nAnswer: ")
if answer48 == "b" or answer48 == "Trusted Boot":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.2 - Boot Integrity ")
	print("\n")
else:
	print("Incorrect: The answer is b. Trusted Boot")
	print("Score:", score)
	print("SY0-601, Objective 3.2 - Boot Integrity ")
	print("\n")

# Question 49

answer49 = input("#49 Which of these best describes two-factor authentication? \n \na. A printer uses a password and a pin \nb. The door to a building requires a fingerprint scan \nc. An application requires a TOTP code \nd. A Windows Domain requires a username, password, and smart card \nAnswer: ")
if answer49 == "d" or answer49 == " A Windows Domain requires a username, password, and smart card ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.4 - Multi-factor Authentication ")
	print("\n")
else:
	print("Incorrect: The answer is d. A Windows Domain requires a username, password, and smart card ")
	print("Score:", score) 
	print("SY0-601, Objective 2.4 - Multi-factor Authentication ")
	print("\n")

# Question 50

answer50 = input("#50 A company is deploying a new mobile application to all of its employees in the field. Some of the problems associated with this rollout include: \n The company does not have a way to manage the mobile devices in the field \n Company data on mobile devices in the field introduces additional risk \n Team members have many different kinds of mobile devices \n Which of the following deployment models would address these concerns? \n \na. Corporate-owned \nb. COPE \nc. VDI \nd. BYOD \nAnswer: ")
if answer50 == "c" or answer50 == "VDI":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.5 - Mobile Deployment Models ")
	print("\n")
else:
	print("Incorrect: The answer is c. VDI ")
	print("Score:", score)
	print("SY0-601, Objective 3.5 - Mobile Deployment Models ")
	print("\n")

# Question 51

answer51 = input("#51 An organization is installing a UPS for their new data center. Which of the following would BEST describe this type of control? \n \na. Compensating \nb. Preventive \nc. Managerial \nd. Detective \nAnswer: ")
if answer51 == "a" or answer51 == "Compensating":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.1 - Security Controls ")
	print("\n")
else:
	print("Incorrect: The answer is a. Compensating ")
	print("Score:", score)
	print("SY0-601, Objective 5.1 - Security Controls ")
	print("\n")

# Question 52

answer52 = input("#52 A manufacturing company would like to track the progress of parts as they are used on an assembly line. Which of the following technologies would be the BEST choice for this task? \n \na. Quantum computing \nb. Blockchain \nc. Hashing \nd. Asymmetric  \nAnswer: ")
if answer52 == "b" or answer52 == "Blockchain":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.8 - Blockchain Technology ")
	print("\n")
else:
	print("Incorrect: The answer is b. Blockchain")
	print("Score:", score)
	print("SY0-601, Objective 2.8 - Blockchain Technology ")
	print("\n")

# Question 53

answer53 = input("#53 A security administrator has been asked to respond to a potential security breach of the company’s databases, and they need to gather the most volatile data before powering down the database servers. In which order should they collect this information? \n \na. CPU registers, temporary files, memory, remote monitoring data \nb. Memory, CPU registers, remote monitoring data, temporary files \nc. Memory, CPU registers, temporary files, remote monitoring data \nd. CPU registers, memory, temporary files, remote monitoring data \nAnswer: ")
if answer53 == "d" or answer53 == " CPU registers, memory, temporary files, remote monitoring data ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.5 - Forensics Data Acquisition ")
	print("\n")
else:
	print("Incorrect: The answer is d. CPU registers, memory, temporary files, remote monitoring data ")
	print("Score:", score)
	print("SY0-601, Objective 4.5 - Forensics Data Acquisition ")
	print("\n")

# Question 54

answer54 = input("#54 A Linux administrator is downloading an updated version of her Linux distribution. The download site shows a link to the ISO and a SHA256 hash value. Which of these would describe the use of this hash value? \n \na. Verifies that the file was not corrupted during the file transfer \nb. Provides a key for decrypting the ISO after download \nc. Authenticates the site as an official ISO distribution site \nd. Confirms that the file does not contain any malware \nAnswer: ")
if answer54 == "a" or answer54 == " Verifies that the file was not corrupted during the file transfer ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.8 - Hashing and Digital Signatures ")
	print("\n")
else:
	print("Incorrect: The answer is a. Verifies that the file was not corrupted during the file transfer ")
	print("Score:", score)
	print("SY0-601, Objective 2.8 - Hashing and Digital Signatures ")
	print("\n")

# Question 55

answer55 = input("#55 A company's security policy requires that login access should only be available if a person is physically within the same building as the server. Which of the following would be the BEST way to provide this requirement? \n \na. TOTP \nb. Biometric scanner \nc. PIN \nd. SMS \nAnswer: ")
if answer55 == "b" or answer55 == "Biometric scanner":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.7 - Physical Security Controls ")
	print("\n")
else:
	print("Incorrect: The answer is b. Biometric scanner ")
	print("Score:", score)
	print("SY0-601, Objective 2.7 - Physical Security Controls ")
	print("\n")

# Question 56

answer56 = input("#56 Your development team has installed a new application and database to a cloud service. After running a vulnerability scanner on the application instance, you find that the database is available for anyone to query without providing any authentication. Which of these vulnerabilities is MOST associated with this issue? \n \na. Improper error handling \nb. Open permissions \nc. Race condition \nd. Memory leak \nAnswer: ")
if answer56 == "b" or answer56 == "Open permissions":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.6 - Vulnerability Types ")
	print("\n")
else:
	print("Incorrect: The answer is b. Open permissions")
	print("Score:", score)
	print("SY0-601, Objective 1.6 - Vulnerability Types ")
	print("\n")

# Question 58

answer58 = input("#58 Which of the following risk management strategies would include the purchase and installation of an NGFW? \n \na. Transference \nb. Mitigation \nc. Acceptance \nd. Risk-avoidance \nAnswer: ")
if answer58 == "b" or answer58 == "Mitigation":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.6 - Risk Management Types")
	print("\n")
else:
	print("Incorrect: The answer is b. Mitigation ")
	print("Score:", score)
	print("SY0-601, Objective 5.6 - Risk Management Types")
	print("\n")

# Question 59

answer59 = input("#59 Which of the following would be the BEST way to confirm the secure baseline of a deployed application instance? \n \na. Compare the production application to the sandbox \nb. Perform an integrity measurement \nc. Compare the production application to the previous version \nd. Perform QA testing on the application instance \nAnswer: ")
if answer59 == "b" or answer59 == "Perform an integrity measurement":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.3 - Secure Deployments ")
	print("\n")
else:
	print("Incorrect: The answer is b. Perform an integrity measurement ")
	print("Score:", score)
	print("SY0-601, Objective 2.3 - Secure Deployments ")
	print("\n")

# Question 60

answer60 = input("#60 A member of the accounting team was out of the office for two weeks, and an important financial transfer was delayed until they returned. Which of the following would have prevented this delay? \n \na. Split knowledge \nb. Least privilege \nc. Job rotation \nd. Dual control \nAnswer: ")
if answer60 == "c" or answer60 == "Job rotation":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.3 - Personnel Security ")
	print("\n")
else:
	print("Incorrect: The answer is c. Job rotation ")
	print("Score:", score)
	print("SY0-601, Objective 5.3 - Personnel Security ")
	print("\n")

# Question 61

answer61 = input("#61 A security analyst has identified a number of sessions from a single IP address with a TTL equal to zero. One of the sessions has a destination of the Internet firewall, and a session immediately after has a destination of your DMZ server. Which of the following BEST describes this log information? \n \na. Someone is performing a vulnerability scan against the firewall and DMZ server \nb. Users are performing DNS lookups \nc. A remote user is grabbing banners of the firewall and DMZ server \nd. Someone is performing a traceroute to the DMZ server \nAnswer: ")
if answer61 == "d" or answer61 == " Someone is performing a traceroute to the DMZ ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.1 - Reconnaissance Tools Part 1 ")
	print("\n")
else:
	print("Incorrect: The answer is d. Someone is performing a traceroute to the DMZ ")
	print("Score:", score)
	print("SY0-601, Objective 4.1 - Reconnaissance Tools Part 1 ")
	print("\n")

# Question 62

answer62 = input("#62 An attacker has sent more information than expected in a single API call, and this has allowed the execution of arbitrary code. Which of the following would BEST describe this attack? \n \na. Buffer overflow \nb. Replay attack \nc. Session hijacking \nd. DDoS \nAnswer: ")
if answer62 == "a" or answer62 == "Buffer overflow":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.3 - Buffer Overflows ")
	print("\n")
else:
	print("Incorrect: The answer is a. Buffer overflow ")
	print("Score:", score)
	print("SY0-601, Objective 1.3 - Buffer Overflows ")
	print("\n")

# Question 63

answer63 = input("#63 A company encourages users to encrypt all of their confidential materials on a central server. The organization would like to enable key escrow as a backup. Which of these keys should the organization place into escrow? \n \na. Private \nb. CA \nc. Session \nd. Public \nAnswer: ")
if answer63 == "a" or answer63 == "Private":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.9 - Certificate Concepts ")
	print("\n")
else:
	print("Incorrect: The answer is a. Private")
	print("Score:", score)
	print("SY0-601, Objective 3.9 - Certificate Concepts ")
	print("\n")

# Question 64

answer64 = input("#64 A security administrator is designing an authentication process for a new remote site deployment. They would like the users to provide their credentials when they authenticate in the morning, and they do not want any additional authentication requests to appear during the rest of the day. Which of the following should be used to meet this requirement? \n \na. TACACS+ \nb. LDAPS \nc. Kerberos \nd. 802.1X \nAnswer: ")
if answer64 == "c" or answer64 == "Kerberos":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.8 - Identity and Access Services ")
	print("\n")
else:
	print("Incorrect: The answer is c. Kerberos ")
	print("Score:", score)
	print("SY0-601, Objective 3.8 - Identity and Access Services ")
	print("\n")

# Question #65

answer65 = input("#65 A manufacturing company would like to use an existing router to separate a corporate network and a manufacturing floor that use the same physical switch. The company does not want to install any additional hardware. Which of the following would be the BEST choice for this segmentation?  \n \na. Connect the corporate network and the manufacturing floor with a VPN \nb. Build an air gapped manufacturing floor network \nc. Use personal firewalls on each device \nd. Create separate VLANs for the corporate network and the manufacturing floor \nAnswer: ")
if answer65 == "d" or answer65 == " Create separate VLAN for the corporate network and the manufacturing floor ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.3 - Network Segmentation ")
	print("\n")
else:
	print("Incorrect: The answer is d. Create separate VLAN for the corporate network and the manufacturing floor")
	print("Score:", score)
	print("SY0-601, Objective 3.3 - Network Segmentation ")
	print("\n")

# Question #66

answer66 = input("#66 When a home user connects to the corporate VPN, they are no longer able to print to their local network printer. Once the user disconnects from the VPN, the printer works normally. Which of the following would be the MOST likely reason for this issue? \n \na. The VPN uses IPSec instead of SSL \nb. Printer traffic is filtered by the VPN client \nc. The VPN is stateful \nd. The VPN tunnel is configured for full tunnel \nAnswer: ")
if answer66 == "d" or answer66 == "The VPN tunnel is configured for full tunnel":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("")
	print("\n")
else:
	print("Incorrect: The answer is d. The VPN tunnel is configured for full tunnel ")
	print("Score:", score)
	print("")
	print("\n")

# Question #67

answer67 = input("#67 A data center manager has built a Faraday cage in the data center, and a set of application servers have been placed into racks inside the Faraday cage. Which of the following would be the MOST likely reason for the data center manager to install this configuration of equipment? \n \na. Protect the servers against unwanted electromagnetic fields \nb. Prevent physical access to the servers without the proper credentials \nc. Provide additional cooling to all devices in the cage \nd. Adds additional fire protection for the application servers \nAnswer: ")
if answer67 == "a" or answer67 == " Protect the servers against any unwanted electromagnetic fields ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.7 - Physical Security Controls ")
	print("\n")
else:
	print("Incorrect: The answer is a. Protect the servers against unwanted electromagnetic fields" )
	print("Score:", score)
	print("SY0-601, Objective 2.7 - Physical Security Controls ")
	print("\n")

# Question 68

answer68 = input("#68 A recent report shows the return of a vulnerability that was previously patched four months ago. After researching this issue, the security team has found that a recent patch has reintroduced this vulnerability on the servers. Which of the following should the security administrator implement to prevent this issue from occurring in the future? \n \na. Templates \nb. Elasticity \nc. Master image \nd. Continuous monitoring \nAnswer: ")
if answer68 == "d" or answer68 == "Continuous monitoring":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.3 - Automation and Scripting ")
	print("\n")
else:
	print("Incorrect: The answer is d. Continuous monitoring ")
	print("Score:", score)
	print("SY0-601, Objective 2.3 - Automation and Scripting ")
	print("\n")

# Question 69

answer69 = input("#69 A security manager would like to ensure that unique hashes are used with an application login process. Which of the following would be the BEST way to add random data when generating a set of stored password hashes? \n \na. Salting \nb. Obfuscation \nc. Key stretching \nd. Digital signature \nAnswer: ")
if answer69 == "a" or answer69 == "Salting":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.8 - Hashing and Digital Signatures ")
	print("\n")
else:
	print("Incorrect: The answer is a. Salting")
	print("Score:", score)
	print("SY0-601, Objective 2.8 - Hashing and Digital Signatures ")
	print("\n")

# Question 70

answer70 = input("#70 Which cryptographic method is used to add trust to a digital certificate? \n \na. X.509 \nb. Hash \nc. Symmetric encryption \nd. Digital signature \nAnswer: ")
if answer70 == "d" or answer70 == "Digital signature":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.9 - Public Key Infrastructure ")
	print("\n")
else:
	print("Incorrect: The answer is ")
	print("Score:", score)
	print("SY0-601, Objective 3.9 - Public Key Infrastructure ")
	print("\n")

# Question 71

answer71 = input("#71 An MSP is designing a new server room for a large company. Which of the following should be included in the design to provide redundancy?  \n \na. SIEM \nb. Temperature monitors \nc. RAID arrays and dual power supplies \nd. Hot and cold aisles \nAnswer: ")
if answer71 == "c" or answer71 == " RAID arrays and dual power supplies ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.5 - Disk Redundancy ")
	print("\n")
else:
	print("Incorrect: The answer is c. RAID arrays and dual power supplies ")
	print("Score:", score)
	print("SY0-601, Objective 2.5 - Disk Redundancy ")
	print("\n")

# Question 72

answer72 = input("#72 An organization maintains a large database of customer information for sales tracking and customer support. Which person in the organization would be responsible for managing the access rights to this data? \n \na. Data processor \nb. Data owner \nc. Privacy officer \nd. Data custodian \nAnswer: ")
if answer72 == "d" or answer72 == "Data custodian":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.5 - Data Roles and Responsibilities ")
	print("\n")
else:
	print("Incorrect: The answer is d. Data custodian")
	print("Score:", score)
	print("SY0-601, Objective 5.5 - Data Roles and Responsibilities ")
	print("\n")
# Question 73

answer73 = input("#73 An organization’s content management system (CMS) currently labels files and documents as “Unclassified” and “Restricted.” On a recent updated to the CMS, a new classification type of “PII” was added. Which of the following would be the MOST likely reason for this addition?  \n \na. Healthcare system integration \nb. Simplified categorization \nc. Expanded privacy compliance \nd. Decreased search time \nAnswer: ")
if answer73 == "c" or answer73 == " Expanded privacy compliance ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.5 - Data Classifications ")
	print("\n")
else:
	print("Incorrect: The answer is c. Expanded privacy compliance ")
	print("Score:", score)
	print("SY0-601, Objective 5.5 - Data Classifications ")
	print("\n")

# Question 74

answer74 = input("#74 A corporate security team would like to consolidate and protect the private keys across all of their web servers. Which of these would be the BEST way to securely store these keys? \n \na. Use an HSM \nb. Implement full disk encryption on the web servers \nc. Use a TPM \nd. Upgrade the web servers to use a UEFI BIOS \nAnswer: ")
if answer74 == "a" or answer74 == " Use an HSM ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.3 - Other Network Appliances ")
	print("\n")
else:
	print("Incorrect: The answer is a. Use an HSM ")
	print("Score:", score)
	print("SY0-601, Objective 3.3 - Other Network Appliances ")
	print("\n")

# Question 75

answer75 = input("#75 Jennifer is reviewing this security log from her IPS: \n ALERT 2018-06-01 13:07:29 [163bcf65118-179b547b] \n Cross-Site Scripting in JSON Data 222.43.112.74:3332 -> 64.235.145.35:80 \n URL/index.html - Method POST - Query String - \n User Agent: curl/7.21.3 (i386-redhat-linux-gnu) libcurl/7.21.3 NSS/3.13.1.0 zlib/1.2.5 libidn/1.19ibssh2/1.2.7 \n Detail: token=<script> key=key7 value= <script>alert(2)</script> \n Which of the following can be determined from this log information?  \n \na. The alert was generated from a malformed User Agent header \nb. The alert was generated from an embedded script and the attacker’s IP address is 222.43.112.74 \nc. The attacker’s IP address is 64.235.145.35 \nd. The alert was generated due to an invalid client port number \nAnswer:")
if answer75 == "b" or answer75 == " The alert was generated from an embedded script and the attacker’s IP address is 222.43.112.74 ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.3 - Log Files ")
	print("\n")
else:
	print("Incorrect: The answer is b. The alert was generated from an embedded script and the attacker’s IP address is 222.43.112.74 ")
	print("Score:", score)
	print("SY0-601, Objective 4.3 - Log Files ")
	print("\n")

# Question 76

answer76 = input("#76 Which of the following describes a monetary loss if one event occurs? \n \na. ALE \nb. SLE \nc. RTO \nd. ARO \nAnswer: ")
if answer76 == "b" or answer76 == "SLE (Single Loss Expectancy) ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.4 - Risk Analysis ")
	print("\n")
else:
	print("Incorrect: The answer is b. SLE (Single Loss Expectancy) ")
	print("Score:", score)
	print("SY0-601, Objective 5.4 - Risk Analysis ")
	print("\n")

# Question 77

answer77 = input("#77 A user with restricted access has typed this text in a search field of an internal web-based application: \n USER77' OR  '1'='1 \n After submitting this search request, all of the database records are displayed on the screen. Which of the following would BEST describe this search? \n \na. CSRF \nb. Buffer overflow \nc. SQL injection \nd. SSL stripping \nAnswer: ")
if answer77 == "c" or answer77 == "SQL injection":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.3 - Injection Attacks ")
	print("\n")
else:
	print("Incorrect: The answer is c. SQL injection ")
	print("Score:", score)
	print("SY0-601, Objective 1.3 - Injection Attacks ")
	print("\n")

# Question 78

answer78 = input("#78 A user has opened a helpdesk ticket complaining of poor system performance, excessive pop up messages, and the cursor moving without anyone touching the mouse. This issue began after they opened a spreadsheet from a vendor containing part numbers and pricing information. Which of the following is MOST likely the cause of this user's issues? \n \na.  \nb.  \nc.  \nd.  \nAnswer: ")
if answer78 == "c" or answer78 == "RAT (Remote Access Trojan":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.2 - Trojans and RATs ")
	print("\n")
else:
	print("Incorrect: The answer is c. Remote Access Trojan")
	print("Score:", score)
	print("SY0-601, Objective 1.2 - Trojans and RATs ")
	print("\n")

# Question 79

answer79 = input("#79 A web-based manufacturing company processes monthly charges to credit card information saved in the customer's profile. Which of the following standards would be required to maintain this payment information? \n \na. GDPR \nb. ISO 27001 \nc. PCI DSS \nd. CSA CCM \nAnswer: ")
if answer79 == "c" or answer79 == "PCI DSS":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 5.2 - Security Regulations and Standards ")
	print("\n")
else:
	print("Incorrect: The answer is c. PCI DSS ")
	print("Score:", score)
	print("SY0-601, Objective 5.2 - Security Regulations and Standards  ")
	print("\n")

# Question 80

answer80 = input("#80 A security manager has created a report showing intermittent network communication from external IP addresses to certain workstations on the internal network. These traffic patterns occur at random times during the day. Which of the following would be the MOST likely reason for these traffic patterns? \n \na. ARP poisoning \nb. Backdoor \nc.  Polymorphic \nd. Trojan horse \nAnswer: ")
if answer80 == "b" or answer80 == "Backdoor":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.2 - Trojans and RATs ")
	print("\n")
else:
	print("Incorrect: The answer is b. Backdoor ")
	print("Score:", score)
	print("SY0-601, Objective 1.2 - Trojans and RATs ")
	print("\n")

# Question 81

answer81 = input("#81 The security policies in a manufacturing company prohibit the transmission of customer information. However, a security administrator has received an alert that credit card numbers were transmitted as an email attachment. Which of the following was the MOST likely source of this alert message? \n \na. IPS \nb. DLP \nc. SMTP \nd. IPsec \nAnswer: ")
if answer81 == "b" or answer81 == "DLP":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 4.4 - Security Configurations ")
	print("\n")
else:
	print("Incorrect: The answer is b. DLP ")
	print("Score:", score)
	print("SY0-601, Objective 4.4 - Security Configurations ")
	print("\n")

# Question 82

answer82 = input("#82 A security administrator has configured a virtual machine in a screened subnet with a guest login account and no password. Which of the following would be the MOST likely reason for this configuration? \n \na. The server is a honeypot for attracting potential attackers \nb. The server is a cloud storage service for remote users \nc. The server will be used as a VPN concentrator \nd. The server is a development sandbox for third-party programming projects \nAnswer: ")
if answer82 == "a" or answer82 == " The server is a honeypot for attracting potential attackers ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.1 - Honeypots and Deception ")
	print("\n")
else:
	print("Incorrect: The answer is a. The server is a honeypot for attracting potential attackers ")
	print("Score:", score)
	print("SY0-601, Objective 2.1 - Honeypots and Deception ")
	print("\n")

# Question 83

answer83 = input("#83 A company's outgoing email server currently uses SMTP with no encryption. The security administrator would like to implement encryption between email clients without changing the existing server-to-server communication. Which of the following would be the BEST way to implement this requirement? \n \na. Implement Secure IMAP \nb. Require the use of S/MIME \nc. Install an SSL certificate on the email server \nd. Use a VPN tunnel between email clients \nAnswer: ")
if answer83 == "b" or answer83 == "Require the use of S/MIME (Secure/Multipurpose Internet Mail Extensions) ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.1 - Secure Protocols ")
	print("\n")
else:
	print("Incorrect: The answer is b. Require the use of S/MIME (Secure/Multipurpose Internet Mail Extensions) ")
	print("Score:", score)
	print("SY0-601, Objective 3.1 - Secure Protocols ")
	print("\n")
# Question 83

answer83 = input("#83 A company's outgoing email server currently uses SMTP with no encryption. The security administrator would like to implement encryption between email clients without changing the existing server-to-server communication. Which of the following would be the BEST way to implement this requirement? \n \na. Implement Secure IMAP \nb. Require the use of S/MIME \nc. Install an SSL certificate on the email server \nd. Use a VPN tunnel between email clients \nAnswer: ")
if answer83 == "b" or answer83 == "Require the use of S/MIME (Secure/Multipurpose Internet Mail Extensions) ":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 3.1 - Secure Protocols ")
	print("\n")
else:
	print("Incorrect: The answer is b. Require the use of S/MIME (Secure/Multipurpose Internet Mail Extensions) ")
	print("Score:", score)
	print("SY0-601, Objective 3.1 - Secure Protocols ")
	print("\n")

# Question 84

answer84 = input("#84 A company would like to securely deploy applications without the overhead of installing a virtual machine for each system. Which of the following would be the BEST way to deploy these applications? \n \na. Containerization \nb. IaaS \nc. Proxies \nd. CASB \nAnswer: ")
if answer84 == "a" or answer84 == "Containerization":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 2.2 - Designing the Cloud ")
	print("\n")
else:
	print("Incorrect: The answer is a. Containerization ")
	print("Score:", score)
	print("SY0-601, Objective 2.2 - Designing the Cloud ")
	print("\n")

# Question 85

answer85 = input("#85 A company has just purchased a new application server, and the security director wants to determine if the system is secure. The system is currently installed in a test environment and will not be available to users until the rollout to production next week. Which of the following would be the BEST way to determine if any part of the system can be exploited? \n \na. Tabletop exercise \nb. Vulnerability scanner \nc. Password cracker \nd. Penetration test \nAnswer: ")
if answer85 == "d" or answer85 == "Penetration test":
	score += 1
	print("Correct!")
	print("Score:", score)
	print("SY0-601, Objective 1.8 - Penetration Testing ")
	print("\n")
else:
	print("Incorrect: The answer is d. Penetration test")
	print("Score:", score)
	print("SY0-601, Objective 1.8 - Penetration Testing ")
	print("\n")

