import os, sys
import readline
from time import sleep as timeout

def main():
    banner()
    print("   [01] Information Gathering")
    print("   [02] Vulnerability Analysis")
    print("   [03] Web Hacking")
    print("   [04] Database Assessment")
    print("   [05] Password Attacks")
    print("   [06] Wireless Attacks")
    print("   [07] Reverse Engineering")
    print("   [08] Exploitation Tools")
    print("   [09] Sniffing and Spoofing")
    print("   [10] Reporting Tools")
    print("   [11] Forensic Tools")
    print("   [12] Stress Testing")
    print("   [13] Install Linux Distro")
    print("   [14] Termux Utility")
    print("   [15] Shell Function [.bashrc]")
    print("   [16] Install CLI Games")
    print("   [17] Malware Analysis")
    print("   [18] Compiler/Interpreter")
    print("   [19] Social Engineering Tools")
    print("\n   [99] Update the Lazymux")
    print("   [00] Exit the Lazymux\n")
    lazymux = input("lzmx > set_install ")

    # 01 - Information Gathering
    if lazymux.strip() == "1" or lazymux.strip() == "01":
        print("\n    [01] Nmap: Utility for network discovery and security auditing")
        print("    [02] Red Hawk: Information Gathering, Vulnerability Scanning and Crawling")
        print("    [03] D-TECT: All-In-One Tool for Penetration Testing")
        print("    [04] sqlmap: Automatic SQL injection and database takeover tool")
        print("    [05] Infoga: Tool for Gathering Email Accounts Informations")
        print("    [06] ReconDog: Information Gathering and Vulnerability Scanner tool")
        print("    [07] AndroZenmap")
        print("    [08] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
        print("    [09] AstraNmap: Security scanner used to find hosts and services on a computer network")
        print("    [10] MapEye: Accurate GPS Location Tracker (Android, IOS, Windows phones)")
        print("    [11] Easymap: Nmap Shortcut")
        print("    [12] BlackBox: A Penetration Testing Framework")
        print("    [13] XD3v: Powerful tool that lets you know all the essential details about your phone")
        print("    [14] Crips: This Tools is a collection of online IP Tools that can be used to quickly get information about IP Address's, Web Pages and DNS records")
        print("    [15] SIR: Resolve from the net the last known ip of a Skype Name")
        print("    [16] EvilURL: Generate unicode evil domains for IDN Homograph Attack and detect them")
        print("    [17] Striker: Recon & Vulnerability Scanning Suite")
        print("    [18] Xshell: ToolKit")
        print("    [19] OWScan: OVID Web Scanner")
        print("    [20] OSIF: Open Source Information Facebook")
        print("    [21] Devploit: Simple Information Gathering Tool")
        print("    [22] Namechk: Osint tool based on namechk.com for checking usernames on more than 100 websites, forums and social networks")
        print("    [23] AUXILE: Web Application Analysis Framework")
        print("    [24] inther: Information gathering using shodan, censys and hackertarget")
        print("    [25] GINF: GitHub Information Gathering Tool")
        print("    [26] GPS Tracking")
        print("    [27] ASU: Facebook Hacking ToolKit")
        print("    [28] fim: Facebook Image Downloader")
        print("    [29] MaxSubdoFinder: Tool for Discovering Subdomain")
        print("    [30] pwnedOrNot: OSINT Tool for Finding Passwords of Compromised Email Accounts")
        print("    [31] Mac-Lookup: Finds information about a Particular Mac address")
        print("    [32] BillCipher: Information Gathering tool for a Website or IP address")
        print("    [33] dnsrecon: Security assessment and network troubleshooting")
        print("    [34] zphisher: Automated Phishing Tool")
        print("    [35] Mr.SIP: SIP-Based Audit and Attack Tool")
        print("    [36] Sherlock: Hunt down social media accounts by username")
        print("    [37] userrecon: Find usernames across over 75 social networks")
        print("    [38] PhoneInfoga: One of the most advanced tools to scan phone numbers using only free resources")
        print("    [39] SiteBroker: A cross-platform python based utility for information gathering and penetration testing automation")
        print("    [40] maigret: Collect a dossier on a person by username from thousands of sites")
        print("    [41] GatheTOOL: Information Gathering - API hackertarget.com")
        print("    [42] ADB-ToolKit")
        print("    [43] TekDefense-Automater: Automater - IP URL and MD5 OSINT Analysis")
        print("    [44] EagleEye: Stalk your Friends. Find their Instagram, FB and Twitter Profiles using Image Recognition and Reverse Image Search")
        print("    [45] EyeWitness: EyeWitness is designed to take screenshots of websites, provide some server header info, and identify default credentials if possible")
        print("    [46] InSpy: A python based LinkedIn enumeration tool")
        print("    [47] Leaked: Leaked? 2.1 - A Checking tool for Hash codes, Passwords and Emails leaked")
        print("    [48] fierce: A DNS reconnaissance tool for locating non-contiguous IP space")
        print("    [49] gasmask: Information gathering tool - OSINT")
        print("    [50] osi.ig: Information Gathering (Instagram)")
        print("    [51] proxy-checker: The simple script, which checks good and bad proxies")
        print("\n    [00] Back to main menu\n")
        infogathering = input("lzmx > set_install ")
        if infogathering == "@":
            infogathering = ""
            for x in range(1,201):
                infogathering += f"{x} "
        if len(infogathering.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for infox in infogathering.split():
            if infox.strip() == "01" or infox.strip() == "1": nmap()
            elif infox.strip() == "02" or infox.strip() == "2": red_hawk()
            elif infox.strip() == "03" or infox.strip() == "3": dtect()
            elif infox.strip() == "04" or infox.strip() == "4": sqlmap()
            elif infox.strip() == "05" or infox.strip() == "5": infoga()
            elif infox.strip() == "06" or infox.strip() == "6": reconDog()
            elif infox.strip() == "07" or infox.strip() == "7": androZenmap()
            elif infox.strip() == "08" or infox.strip() == "8": sqlmate()
            elif infox.strip() == "09" or infox.strip() == "9": astraNmap()
            elif infox.strip() == "10": mapeye()
            elif infox.strip() == "11": easyMap()
            elif infox.strip() == "12": blackbox()
            elif infox.strip() == "13": xd3v()
            elif infox.strip() == "14": crips()
            elif infox.strip() == "15": sir()
            elif infox.strip() == "16": evilURL()
            elif infox.strip() == "17": striker()
            elif infox.strip() == "18": xshell()
            elif infox.strip() == "19": owscan()
            elif infox.strip() == "20": osif()
            elif infox.strip() == "21": devploit()
            elif infox.strip() == "22": namechk()
            elif infox.strip() == "23": auxile()
            elif infox.strip() == "24": inther()
            elif infox.strip() == "25": ginf()
            elif infox.strip() == "26": gpstr()
            elif infox.strip() == "27": asu()
            elif infox.strip() == "28": fim()
            elif infox.strip() == "29": maxsubdofinder()
            elif infox.strip() == "30": pwnedOrNot()
            elif infox.strip() == "31": maclook()
            elif infox.strip() == "32": billcypher()
            elif infox.strip() == "33": dnsrecon()
            elif infox.strip() == "34": zphisher()
            elif infox.strip() == "35": mrsip()
            elif infox.strip() == "36": sherlock()
            elif infox.strip() == "37": userrecon()
            elif infox.strip() == "38": phoneinfoga()
            elif infox.strip() == "39": sitebroker()
            elif infox.strip() == "40": maigret()
            elif infox.strip() == "41": gathetool()
            elif infox.strip() == "42": adbtk()
            elif infox.strip() == "43": tekdefense()
            elif infox.strip() == "44": eagleeye()
            elif infox.strip() == "45": eyewitness()
            elif infox.strip() == "46": inspy()
            elif infox.strip() == "47": leaked()
            elif infox.strip() == "48": fierce()
            elif infox.strip() == "49": gasmask()
            elif infox.strip() == "50": osi_ig()
            elif infox.strip() == "51": proxy_checker()
            elif infox.strip() == "00" or infox.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 02 - Vulnerability Analysis
    elif lazymux.strip() == "2" or lazymux.strip() == "02":
        print("\n    [01] Nmap: Utility for network discovery and security auditing")
        print("    [02] AndroZenmap")
        print("    [03] AstraNmap: Security scanner used to find hosts and services on a computer network")
        print("    [04] Easymap: Nmap Shortcut")
        print("    [05] Red Hawk: Information Gathering, Vulnerability Scanning and Crawling")
        print("    [06] D-TECT: All-In-One Tool for Penetration Testing")
        print("    [07] Damn Small SQLi Scanner: A fully functional SQL injection vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code")
        print("    [08] SQLiv: massive SQL injection vulnerability scanner")
        print("    [09] sqlmap: Automatic SQL injection and database takeover tool")
        print("    [10] sqlscan: Quick SQL Scanner, Dorker, Webshell injector PHP")
        print("    [11] Wordpresscan: WPScan rewritten in Python + some WPSeku ideas")
        print("    [12] WPScan: Free wordPress security scanner")
        print("    [13] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
        print("    [14] termux-wordpresscan")
        print("    [15] TM-scanner: websites vulnerability scanner for termux")
        print("    [16] Rang3r: Multi Thread IP + Port Scanner")
        print("    [17] Striker: Recon & Vulnerability Scanning Suite")
        print("    [18] Routersploit: Exploitation Framework for Embedded Devices")
        print("    [19] Xshell: ToolKit")
        print("    [20] SH33LL: Shell Scanner")
        print("    [21] BlackBox: A Penetration Testing Framework")
        print("    [22] XAttacker: Website Vulnerability Scanner & Auto Exploiter")
        print("    [23] OWScan: OVID Web Scanner")
        print("    [24] XPL-SEARCH: Search exploits in multiple exploit databases")
        print("    [25] AndroBugs_Framework: An efficient Android vulnerability scanner that helps developers or hackers find potential security vulnerabilities in Android applications")
        print("    [26] Clickjacking-Tester: A python script designed to check if the website if vulnerable of clickjacking and create a poc")
        print("    [27] Sn1per: Attack Surface Management Platform | Sn1perSecurity LLC")
        print("\n    [00] Back to main menu\n")
        vulnsys = input("lzmx > set_install ")
        if vulnsys == "@":
            vulnsys = ""
            for x in range(1,201):
                vulnsys += f"{x} "
        if len(vulnsys.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for vulnx in vulnsys.split():
            if vulnsys.strip() == "01" or vulnsys.strip() == "1": nmap()
            elif vulnsys.strip() == "02" or vulnsys.strip() == "2": androZenmap()
            elif vulnsys.strip() == "03" or vulnsys.strip() == "3": astraNmap()
            elif vulnsys.strip() == "04" or vulnsys.strip() == "4": easyMap()
            elif vulnsys.strip() == "05" or vulnsys.strip() == "5": red_hawk()
            elif vulnsys.strip() == "06" or vulnsys.strip() == "6": dtect()
            elif vulnsys.strip() == "07" or vulnsys.strip() == "7": dsss()
            elif vulnsys.strip() == "08" or vulnsys.strip() == "8": sqliv()
            elif vulnsys.strip() == "09" or vulnsys.strip() == "9": sqlmap()
            elif vulnsys.strip() == "10": sqlscan()
            elif vulnsys.strip() == "11": wordpreSScan()
            elif vulnsys.strip() == "12": wpscan()
            elif vulnsys.strip() == "13": sqlmate()
            elif vulnsys.strip() == "14": wordpresscan()
            elif vulnsys.strip() == "15": tmscanner()
            elif vulnsys.strip() == "16": rang3r()
            elif vulnsys.strip() == "17": striker()
            elif vulnsys.strip() == "18": routersploit()
            elif vulnsys.strip() == "19": xshell()
            elif vulnsys.strip() == "20": sh33ll()
            elif vulnsys.strip() == "21": blackbox()
            elif vulnsys.strip() == "22": xattacker()
            elif vulnsys.strip() == "23": owscan()
            elif vulnsys.strip() == "24": xplsearch()
            elif vulnsys.strip() == "25": androbugs()
            elif vulnsys.strip() == "26": clickjacking()
            elif vulnsys.strip() == "27": sn1per()
            elif vulnsys.strip() == "00" or vulnsys.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 03 - Web Hacking
    elif lazymux.strip() == "3" or lazymux.strip() == "03":
        print("\n    [01] sqlmap: Automatic SQL injection and database takeover tool")
        print("    [02] WebDAV: WebDAV File Upload Exploiter")
        print("    [03] MaxSubdoFinder: Tool for Discovering Subdomain")
        print("    [04] Webdav Mass Exploit")
        print("    [05] Atlas: Quick SQLMap Tamper Suggester")
        print("    [06] sqldump: Dump sql result sites with easy")
        print("    [07] Websploit: An advanced MiTM Framework")
        print("    [08] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
        print("    [09] inther: Information gathering using shodan, censys and hackertarget")
        print("    [10] HPB: HTML Pages Builder")
        print("    [11] Xshell: ToolKit")
        print("    [12] SH33LL: Shell Scanner")
        print("    [13] XAttacker: Website Vulnerability Scanner & Auto Exploiter")
        print("    [14] XSStrike: Most advanced XSS Scanner")
        print("    [15] Breacher: An advanced multithreaded admin panel finder")
        print("    [16] OWScan: OVID Web Scanner")
        print("    [17] ko-dork: A simple vuln web scanner")
        print("    [18] ApSca: Powerful web penetration application")
        print("    [19] amox: Find backdoor or shell planted on a site via dictionary attack")
        print("    [20] FaDe: Fake deface with kindeditor, fckeditor and webdav")
        print("    [21] AUXILE: Auxile Framework")
        print("    [22] xss-payload-list: Cross Site Scripting ( XSS ) Vulnerability Payload List")
        print("    [23] Xadmin: Admin Panel Finder")
        print("    [24] CMSeeK: CMS Detection and Exploitation suite - Scan WordPress, Joomla, Drupal and over 180 other CMSs")
        print("    [25] CMSmap: A python open source CMS scanner that automates the process of detecting security flaws of the most popular CMSs")
        print("    [26] CrawlBox: Easy way to brute-force web directory")
        print("    [27] LFISuite: Totally Automatic LFI Exploiter (+ Reverse Shell) and Scanner")
        print("    [28] Parsero: Robots.txt audit tool")
        print("    [29] Sn1per: Attack Surface Management Platform | Sn1perSecurity LLC")
        print("    [30] Sublist3r: Fast subdomains enumeration tool for penetration testers")
        print("    [31] WP-plugin-scanner: A tool to list plugins installed on a wordpress powered website")
        print("    [32] WhatWeb: Next generation web scanner")
        print("    [33] fuxploider: File upload vulnerability scanner and exploitation tool")
        print("\n    [00] Back to main menu\n")
        webhack = input("lzmx > set_install ")
        if webhack == "@":
            webhack = ""
            for x in range(1,201):
                webhack += f"{x} "
        if len(webhack.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for webhx in webhack.split():
            if webhx.strip() == "01" or webhx.strip() == "1": sqlmap()
            elif webhx.strip() == "02" or webhx.strip() == "2": webdav()
            elif webhx.strip() == "03" or webhx.strip() == "3": maxsubdofinder()
            elif webhx.strip() == "04" or webhx.strip() == "4": webmassploit()
            elif webhx.strip() == "05" or webhx.strip() == "5": atlas()
            elif webhx.strip() == "06" or webhx.strip() == "6": sqldump()
            elif webhx.strip() == "07" or webhx.strip() == "7": websploit()
            elif webhx.strip() == "08" or webhx.strip() == "8": sqlmate()
            elif webhx.strip() == "09" or webhx.strip() == "9": inther()
            elif webhx.strip() == "10": hpb()
            elif webhx.strip() == "11": xshell()
            elif webhx.strip() == "12": sh33ll()
            elif webhx.strip() == "13": xattacker()
            elif webhx.strip() == "14": xsstrike()
            elif webhx.strip() == "15": breacher()
            elif webhx.strip() == "16": owscan()
            elif webhx.strip() == "17": kodork()
            elif webhx.strip() == "18": apsca()
            elif webhx.strip() == "19": amox()
            elif webhx.strip() == "20": fade()
            elif webhx.strip() == "21": auxile()
            elif webhx.strip() == "22": xss_payload_list()
            elif webhx.strip() == "23": xadmin()
            elif webhx.strip() == "24": cmseek()
            elif webhx.strip() == "25": cmsmap()
            elif webhx.strip() == "26": crawlbox()
            elif webhx.strip() == "27": lfisuite()
            elif webhx.strip() == "28": parsero()
            elif webhx.strip() == "29": sn1per()
            elif webhx.strip() == "30": sublist3r()
            elif webhx.strip() == "31": wppluginscanner()
            elif webhx.strip() == "32": whatweb()
            elif webhx.strip() == "33": fuxploider()
            elif webhx.strip() == "00" or webhx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 04 - Database Assessment
    elif lazymux.strip() == "4" or lazymux.strip() == "04":
        print("\n    [01] DbDat: DbDat performs numerous checks on a database to evaluate security")
        print("    [02] sqlmap: Automatic SQL injection and database takeover tool")
        print("    [03] NoSQLMap: Automated NoSQL database enumeration and web application exploitation tool")
        print("    [04] audit_couchdb: Detect security issues, large or small, in a CouchDB server")
        print("    [05] mongoaudit: An automated pentesting tool that lets you know if your MongoDB instances are properly secured")
        print("\n    [00] Back to main menu\n")
        dbssm = input("lzmx > set_install ")
        if dbssm == "@":
            dbssm = ""
            for x in range(1,201):
                dbssm += f"{x} "
        if len(dbssm.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for dbsx in dbssm.split():
            if dbsx.strip() == "01" or dbsx.strip() == "1": dbdat()
            elif dbsx.strip() == "02" or dbsx.strip() == "2": sqlmap()
            elif dbsx.strip() == "03" or dbsx.strip() == "3": nosqlmap
            elif dbsx.strip() == "04" or dbsx.strip() == "4": audit_couchdb()
            elif dbsx.strip() == "05" or dbsx.strip() == "5": mongoaudit()
            elif dbsx.strip() == "00" or dbsx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 05 - Password Attacks
    elif lazymux.strip() == "5" or lazymux.strip() == "05":
        print("\n    [01] Hydra: Network logon cracker supporting different services")
        print("    [02] FMBrute: Facebook Multi Brute Force")
        print("    [03] HashID: Software to identify the different types of hashes")
        print("    [04] Facebook Brute Force 3")
        print("    [05] Black Hydra: A small program to shorten brute force sessions on hydra")
        print("    [06] Hash Buster: Crack hashes in seconds")
        print("    [07] FBBrute: Facebook Brute Force")
        print("    [08] Cupp: Common User Passwords Profiler")
        print("    [09] InstaHack: Instagram Brute Force")
        print("    [10] Indonesian Wordlist")
        print("    [11] Xshell")
        print("    [12] Aircrack-ng: WiFi security auditing tools suite")
        print("    [13] BlackBox: A Penetration Testing Framework")
        print("    [14] Katak: An open source software login brute-forcer toolkit and hash decrypter")
        print("    [15] Hasher: Hash cracker with auto detect hash")
        print("    [16] Hash-Generator: Beautiful Hash Generator")
        print("    [17] nk26: Nkosec Encode")
        print("    [18] Hasherdotid: A tool for find an encrypted text")
        print("    [19] Crunch: Highly customizable wordlist generator")
        print("    [20] Hashcat: World's fastest and most advanced password recovery utility")
        print("    [21] ASU: Facebook Hacking ToolKit")
        print("    [22] Credmap: An open source tool that was created to bring awareness to the dangers of credential reuse")
        print("    [23] BruteX: Automatically brute force all services running on a target")
        print("    [24] Gemail-Hack: python script for Hack gmail account brute force")
        print("    [25] GoblinWordGenerator: Python wordlist generator")
        print("    [26] PyBozoCrack: A silly & effective MD5 cracker in Python")
        print("    [27] brutespray: Brute-Forcing from Nmap output - Automatically attempts default creds on found services")
        print("    [28] crowbar: Crowbar is brute forcing tool that can be used during penetration tests")
        print("    [29] elpscrk: An Intelligent wordlist generator based on user profiling, permutations, and statistics")
        print("    [30] fbht: Facebook Hacking Tool")
        print("\n    [00] Back to main menu\n")
        passtak = input("lzmx > set_install ")
        if passtak == "@":
            passtak = ""
            for x in range(1,201):
                passtak += f"{x} "
        if len(passtak.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for passx in passtak.split():
            if passx.strip() == "01" or passx.strip() == "1": hydra()
            elif passx.strip() == "02" or passx.strip() == "2": fmbrute()
            elif passx.strip() == "03" or passx.strip() == "3": hashid()
            elif passx.strip() == "04" or passx.strip() == "4": fbBrute()
            elif passx.strip() == "05" or passx.strip() == "5": black_hydra()
            elif passx.strip() == "06" or passx.strip() == "6": hash_buster()
            elif passx.strip() == "07" or passx.strip() == "7": fbbrutex()
            elif passx.strip() == "08" or passx.strip() == "8": cupp()
            elif passx.strip() == "09" or passx.strip() == "9": instaHack()
            elif passx.strip() == "10": indonesian_wordlist()
            elif passx.strip() == "11": xshell()
            elif passx.strip() == "12": aircrackng()
            elif passx.strip() == "13": blackbox()
            elif passx.strip() == "14": katak()
            elif passx.strip() == "15": hasher()
            elif passx.strip() == "16": hashgenerator()
            elif passx.strip() == "17": nk26()
            elif passx.strip() == "18": hasherdotid()
            elif passx.strip() == "19": crunch()
            elif passx.strip() == "20": hashcat()
            elif passx.strip() == "21": asu()
            elif passx.strip() == "22": credmap()
            elif passx.strip() == "23": brutex()
            elif passx.strip() == "24": gemailhack()
            elif passx.strip() == "25": goblinwordgenerator()
            elif passx.strip() == "26": pybozocrack()
            elif passx.strip() == "27": brutespray()
            elif passx.strip() == "28": crowbar()
            elif passx.strip() == "29": elpscrk()
            elif passx.strip() == "30": fbht()
            elif passx.strip() == "00" or passx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 06 - Wireless Attacks
    elif lazymux.strip() == "6" or lazymux.strip() == "06":
        print("\n    [01] Aircrack-ng: WiFi security auditing tools suite")
        print("    [02] Wifite: An automated wireless attack tool")
        print("    [03] Wifiphisher: The Rogue Access Point Framework")
        print("    [04] Routersploit: Exploitation Framework for Embedded Devices")
        print("    [05] PwnSTAR: (Pwn SofT-Ap scRipt) - for all your fake-AP needs!")
        print("    [06] Pyrit: The famous WPA precomputed cracker, Migrated from Google")
        print("\n    [00] Back to main menu\n")
        wiretak = input("lzmx > set_install ")
        if wiretak == "@":
            wiretak = ""
            for x in range(1,201):
                wiretak += f"{x} "
        if len(wiretak.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for wirex in wiretak.split():
            if wirex.strip() == "01" or wirex.strip() == "1": aircrackng()
            elif wirex.strip() == "02" or wirex.strip() == "2": wifite()
            elif wirex.strip() == "03" or wirex.strip() == "3": wifiphisher()
            elif wirex.strip() == "04" or wirex.strip() == "4": routersploit()
            elif wirex.strip() == "05" or wirex.strip() == "5": pwnstar()
            elif wirex.strip() == "06" or wirex.strip() == "6": pyrit()
            elif wirex.strip() == "00" or wirex.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 07 - Reverse Engineering
    elif lazymux.strip() == "7" or lazymux.strip() == "07":
        print("\n    [01] Binary Exploitation")
        print("    [02] jadx: DEX to JAVA Decompiler")
        print("    [03] apktool: A utility that can be used for reverse engineering Android applications")
        print("    [04] uncompyle6: Python cross-version byte-code decompiler")
        print("    [05] ddcrypt: DroidScript APK Deobfuscator")
        print("    [06] CFR: Yet another java decompiler")
        print("    [07] UPX: Ultimate Packer for eXecutables")
        print("    [08] pyinstxtractor: PyInstaller Extractor")
        print("    [09] innoextract: A tool to unpack installers created by Inno Setup")
        print("    [10] pycdc: C++ python bytecode disassembler and decompiler")
        print("    [11] APKiD: Android Application Identifier for Packers, Protectors, Obfuscators and Oddities - PEiD for Android")
        print("    [12] DTL-X: Python APK Reverser & Patcher Tool")
        print("    [13] APKLeaks: Scanning APK file for URIs, endpoints & secrets")
        print("    [14] apk-mitm: A CLI application that automatically prepares Android APK files for HTTPS inspection")
        print("    [15] ssl-pinning-remover: An SSL Pinning Remover for Android Apps")
        print("    [16] GEF: GEF (GDB Enhanced Features) - a modern experience for GDB with advanced debugging capabilities for exploit devs & reverse engineers on Linux")
        print("\n    [00] Back to main menu\n")
        reversi = input("lzmx > set_install ")
        if reversi == "@":
            reversi = ""
            for x in range(1,201):
                reversi += f"{x} "
        if len(reversi.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for revex in reversi.split():
            if revex.strip() == "01" or revex.strip() == "1": binploit()
            elif revex.strip() == "02" or revex.strip() == "2": jadx()
            elif revex.strip() == "03" or revex.strip() == "3": apktool()
            elif revex.strip() == "04" or revex.strip() == "4": uncompyle()
            elif revex.strip() == "05" or revex.strip() == "5": ddcrypt()
            elif revex.strip() == "06" or revex.strip() == "6": cfr()
            elif revex.strip() == "07" or revex.strip() == "7": upx()
            elif revex.strip() == "08" or revex.strip() == "8": pyinstxtractor()
            elif revex.strip() == "09" or revex.strip() == "9": innoextract()
            elif revex.strip() == "10": pycdc()
            elif revex.strip() == "11": apkid()
            elif revex.strip() == "12": dtlx()
            elif revex.strip() == "13": apkleaks()
            elif revex.strip() == "14": apkmitm()
            elif revex.strip() == "15": ssl_pinning_remover()
            elif revex.strip() == "16": gef()
            elif revex.strip() == "00" or revex.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 08 - Exploitation Tools
    elif lazymux.strip() == "8" or lazymux.strip() == "08":
        print("\n    [01] Metasploit: Advanced open-source platform for developing, testing and using exploit code")
        print("    [02] commix: Automated All-in-One OS Command Injection and Exploitation Tool")
        print("    [03] BlackBox: A Penetration Testing Framework")
        print("    [04] Brutal: Payload for teensy like a rubber ducky but the syntax is different")
        print("    [05] TXTool: An easy pentesting tool")
        print("    [06] XAttacker: Website Vulnerability Scanner & Auto Exploiter")  
        print("    [07] Websploit: An advanced MiTM Framework")
        print("    [08] Routersploit: Exploitation Framework for Embedded Devices")
        print("    [09] A-Rat: Remote Administration Tool")
        print("    [10] BAF: Blind Attacking Framework")
        print("    [11] Gloom-Framework: Linux Penetration Testing Framework")
        print("    [12] Zerodoor: A script written lazily for generating cross-platform  backdoors on the go :)")
        print("\n    [00] Back to main menu\n")
        exploitool = input("lzmx > set_install ")
        if exploitool == "@":
            exploitool = ""
            for x in range(1,201):
                exploitool += f"{x} "
        if len(exploitool.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for explx in exploitool.split():
            if explx.strip() == "01" or explx.strip() == "1": metasploit()
            elif explx.strip() == "02" or explx.strip() == "2": commix()
            elif explx.strip() == "03" or explx.strip() == "3": blackbox()
            elif explx.strip() == "04" or explx.strip() == "4": brutal()
            elif explx.strip() == "05" or explx.strip() == "5": txtool()
            elif explx.strip() == "06" or explx.strip() == "6": xattacker()
            elif explx.strip() == "07" or explx.strip() == "7": websploit()
            elif explx.strip() == "08" or explx.strip() == "8": routersploit()
            elif explx.strip() == "09" or explx.strip() == "9": arat()
            elif explx.strip() == "10": baf()
            elif explx.strip() == "11": gloomframework()
            elif explx.strip() == "12": zerodoor()
            elif explx.strip() == "00" or explx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 09 - Sniffing and Spoofing
    elif lazymux.strip() == "9" or lazymux.strip() == "09":
        print("\n    [01] KnockMail: Verify if Email Exists")
        print("    [02] tcpdump: A powerful command-line packet analyzer")
        print("    [03] Ettercap: Comprehensive suite for MITM attacks, can sniff live connections, do content filtering on the fly and much more")
        print("    [04] hping3: hping is a command-line oriented TCP/IP packet assembler/analyzer")
        print("    [05] tshark: Network protocol analyzer and sniffer")
        print("\n    [00] Back to main menu\n")
        sspoof = input("lzmx > set_install ")
        if sspoof == "@":
            sspoof = ""
            for x in range(1,201):
                sspoof += f"{x} "
        if len(sspoof.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for sspx in sspoof.split():
            if sspx.strip() == "01" or sspx.strip() == "1": knockmail()
            elif sspx.strip() == "02" or sspx.strip() == "2": tcpdump()
            elif sspx.strip() == "03" or sspx.strip() == "3": ettercap()
            elif sspx.strip() == "04" or sspx.strip() == "4": hping3()
            elif sspx.strip() == "05" or sspx.strip() == "5": tshark()
            elif sspx.strip() == "00" or sspx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 10 - Reporting Tools
    elif lazymux.strip() == "10":
        print("\n    [01] dos2unix: Converts between DOS and Unix text files")
        print("    [02] exiftool: Utility for reading, writing and editing meta information in a wide variety of files")
        print("    [03] iconv: Utility converting between different character encodings")
        print("    [04] mediainfo: Command-line utility for reading information from media files")
        print("    [05] pdfinfo: PDF document information extractor")
        print("\n    [00] Back to main menu\n")
        reportls = input("lzmx > set_install ")
        if reportls == "@":
            reportls = ""
            for x in range(1,201):
                reportls += f"{x} "
        if len(reportls.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for reportx in reportls.split():
            if reportx.strip() == "01" or reportx.strip() == "1": dos2unix()
            elif reportx.strip() == "02" or reportx.strip() == "2": exiftool()
            elif reportx.strip() == "03" or reportx.strip() == "3": iconv()
            elif reportx.strip() == "04" or reportx.strip() == "4": mediainfo()
            elif reportx.strip() == "05" or reportx.strip() == "5": pdfinfo()
            elif reportx.strip() == "00" or reportx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 11 - Forensic Tools
    elif lazymux.strip() == "11":
        print("\n    [01] steghide: Embeds a message in a file by replacing some of the least significant bits")
        print("    [02] tesseract: Tesseract is probably the most accurate open source OCR engine available")
        print("    [03] sleuthkit: The Sleuth Kit (TSK) is a library for digital forensics tools")
        print("    [04] CyberScan: Network's Forensics ToolKit")
        print("    [05] binwalk: Firmware analysis tool")
        print("\n    [00] Back to main menu\n")
        forensc = input("lzmx > set_install ")
        if forensc == "@":
            forensc = ""
            for x in range(1,201):
                forensc += f"{x} "
        if len(forensc.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for forenx in forensc.split():
            if forenx.strip() == "01" or forenx.strip() == "1": steghide()
            elif forenx.strip() == "02" or forenx.strip() == "2": tesseract()
            elif forenx.strip() == "03" or forenx.strip() == "3": sleuthkit()
            elif forenx.strip() == "04" or forenx.strip() == "4": cyberscan()
            elif forenx.strip() == "05" or forenx.strip() == "5": binwalk()
            elif forenx.strip() == "00" or forenx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 12 - Stress Testing
    elif lazymux.strip() == "12":
        print("\n    [01] Torshammer: Slow post DDOS tool")
        print("    [02] Slowloris: Low bandwidth DoS tool")
        print("    [03] Fl00d & Fl00d2: UDP Flood tool")
        print("    [04] GoldenEye: GoldenEye Layer 7 (KeepAlive+NoCache) DoS test tool")
        print("    [05] Xerxes: The most powerful DoS tool")
        print("    [06] Planetwork-DDOS")
        print("    [07] Xshell")
        print("    [08] santet-online: Social Engineering Tool")
        print("    [09] dost-attack: WebServer Attacking Tools")
        print("    [10] DHCPig: DHCP exhaustion script written in python using scapy network library")
        print("\n    [00] Back to main menu\n")
        stresstest = input("lzmx > set_install ")
        if stresstest == "@":
            stresstest = ""
            for x in range(1,201):
                stresstest += f"{x} "
        if len(stresstest.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for stressx in stresstest.split():
            if stressx.strip() == "01" or stressx.strip() == "1": torshammer()
            elif stressx.strip() == "02" or stressx.strip() == "2": slowloris()
            elif stressx.strip() == "03" or stressx.strip() == "3": fl00d12()
            elif stressx.strip() == "04" or stressx.strip() == "4": goldeneye()
            elif stressx.strip() == "05" or stressx.strip() == "5": xerxes()
            elif stressx.strip() == "06" or stressx.strip() == "6": planetwork_ddos()
            elif stressx.strip() == "07" or stressx.strip() == "7": xshell()
            elif stressx.strip() == "08" or stressx.strip() == "8": sanlen()
            elif stressx.strip() == "09" or stressx.strip() == "9": dostattack()
            elif stressx.strip() == "10": dhcpig()
            elif stressx.strip() == "00" or stressx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 13 - Install Linux Distro
    elif lazymux.strip() == "13":
        print("\n    [01] Ubuntu (impish)")
        print("    [02] Fedora")
        print("    [03] Kali Nethunter")
        print("    [04] Parrot")
        print("    [05] Arch Linux")
        print("    [06] Alpine Linux (edge)")
        print("    [07] Debian (bullseye)")
        print("    [08] Manjaro AArch64")
        print("    [09] OpenSUSE (Tumbleweed)")
        print("    [10] Void Linux")
        print("\n    [00] Back to main menu\n")
        innudis = input("lzmx > set_install ")
        if innudis == "@":
            innudis = ""
            for x in range(1,201):
                innudis += f"{x} "
        if len(innudis.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for innux in innudis.split():
            if innux.strip() == "01" or innux.strip() == "1": ubuntu()
            elif innux.strip() == "02" or innux.strip() == "2": fedora()
            elif innux.strip() == "03" or innux.strip() == "3": nethunter()
            elif innux.strip() == "04" or innux.strip() == "4": parrot()
            elif innux.strip() == "05" or innux.strip() == "5": archlinux()
            elif innux.strip() == "06" or innux.strip() == "6": alpine()
            elif innux.strip() == "07" or innux.strip() == "7": debian()
            elif innux.strip() == "08" or innux.strip() == "8": manjaroArm64()
            elif innux.strip() == "09" or innux.strip() == "9": opensuse()
            elif innux.strip() == "10": voidLinux()
            elif innux.strip() == "00" or innux.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 14 - Termux Utility
    elif lazymux.strip() == "14":
        print("\n    [01] SpiderBot: Curl website using random proxy and user agent")
        print("    [02] Ngrok: tunnel local ports to public URLs and inspect traffic")
        print("    [03] Sudo: sudo installer for Android")
        print("    [04] google: Python bindings to the Google search engine")
        print("    [05] kojawafft")
        print("    [06] ccgen: Credit Card Generator")
        print("    [07] VCRT: Virus Creator")
        print("    [08] E-Code: PHP Script Encoder")
        print("    [09] Termux-Styling")
        print("    [11] xl-py: XL Direct Purchase Package")
        print("    [12] BeanShell: A small, free, embeddable Java source interpreter with object scripting language features, written in Java")
        print("    [13] vbug: Virus Maker")
        print("    [14] Crunch: Highly customizable wordlist generator")
        print("    [15] Textr: Simple tool for running text")
        print("    [16] heroku: CLI to interact with Heroku")
        print("    [17] RShell: Reverse shell for single listening")
        print("    [18] TermPyter: Fix all error Jupyter installation on termux")
        print("    [19] Numpy: The fundamental package for scientific computing with Python")
        print("    [20] BTC-to-IDR-checker: Check the exchange rate virtual money currency to Indonesia Rupiah from Bitcoin.co.id API")
        print("    [21] ClickBot: Earn money using telegram bot")
        print("    [22] pandas: Powerful open-source data manipulation and analysis library")
        print("    [23] jupyter-notebook: Interactive web application that allows users to create and share documents containing live code, equations, visualizations, and narrative text")
        print("\n    [00] Back to main menu\n")
        moretool = input("lzmx > set_install ")
        if moretool == "@":
            moretool = ""
            for x in range(1,201):
                moretool += f"{x} "
        if len(moretool.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for moret in moretool.split():
            if moret.strip() == "01" or moret.strip() == "1": spiderbot()
            elif moret.strip() == "02" or moret.strip() == "2": ngrok()
            elif moret.strip() == "03" or moret.strip() == "3": sudo()
            elif moret.strip() == "04" or moret.strip() == "4": google()
            elif moret.strip() == "05" or moret.strip() == "5": kojawafft()
            elif moret.strip() == "06" or moret.strip() == "6": ccgen()
            elif moret.strip() == "07" or moret.strip() == "7": vcrt()
            elif moret.strip() == "08" or moret.strip() == "8": ecode()
            elif moret.strip() == "09" or moret.strip() == "9": stylemux()
            elif moret.strip() == "10": passgencvar()
            elif moret.strip() == "11": xlPy()
            elif moret.strip() == "12": beanshell()
            elif moret.strip() == "13": vbug()
            elif moret.strip() == "14": crunch()
            elif moret.strip() == "15": textr()
            elif moret.strip() == "16": heroku()
            elif moret.strip() == "17": rshell()
            elif moret.strip() == "18": termpyter()
            elif moret.strip() == "19": numpy()
            elif moret.strip() == "20": btc2idr()
            elif moret.strip() == "21": clickbot()
            elif moret.strip() == "22": pandas()
            elif moret.strip() == "23": notebook()
            elif moret.strip() == "00" or moret.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 15 - Shell Function [.bashrc]
    elif lazymux.strip() == "15":
        print("\n    [01] FBVid (FB Video Downloader)")
        print("    [02] cast2video (Asciinema Cast Converter)")
        print("    [03] iconset (AIDE App Icon)")
        print("    [04] readme (GitHub README.md)")
        print("    [05] makedeb (DEB Package Builder)")
        print("    [06] quikfind (Search Files)")
        print("    [07] pranayama (4-7-8 Relax Breathing)")
        print("    [08] sqlc (SQLite Query Processor)")
        print("\n    [00] Back to main menu\n")
        myshf = input("lzmx > set_install ")
        if myshf == "@":
            myshf = ""
            for x in range(1,201):
                myshf += f"{x} "
        if len(myshf.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for mysh in myshf.split():
            if mysh.strip() == "01" or mysh.strip() == "1": fbvid()
            elif mysh.strip() == "02" or mysh.strip() == "2": cast2video()
            elif mysh.strip() == "03" or mysh.strip() == "3": iconset()
            elif mysh.strip() == "04" or mysh.strip() == "4": readme()
            elif mysh.strip() == "05" or mysh.strip() == "5": makedeb()
            elif mysh.strip() == "06" or mysh.strip() == "6": quikfind()
            elif mysh.strip() == "07" or mysh.strip() == "7": pranayama()
            elif mysh.strip() == "08" or mysh.strip() == "8": sqlc()
            elif mysh.strip() == "00" or mysh.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 16 - Install CLI Games
    elif lazymux.strip() == "16":
        print("\n    [01] Flappy Bird")
        print("    [02] Street Car")
        print("    [03] Speed Typing")
        print("    [04] NSnake: The classic snake game with textual interface")
        print("    [05] Moon buggy: Simple game where you drive a car across the moon's surface")
        print("    [06] Nudoku: ncurses based sudoku game")
        print("    [07] tty-solitaire")
        print("    [08] Pacman4Console")
        print("\n    [00] Back to main menu\n")
        cligam = input("lzmx > set_install ")
        if cligam == "@":
            cligam = ""
            for x in range(1,201):
                cligam += f"{x} "
        if len(cligam.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for clig in cligam.split():
            if clig.strip() == "01" or clig.strip() == "1": flappy_bird()
            elif clig.strip() == "02" or clig.strip() == "2": street_car()
            elif clig.strip() == "03" or clig.strip() == "3": speed_typing()
            elif clig.strip() == "04" or clig.strip() == "4": nsnake()
            elif clig.strip() == "05" or clig.strip() == "5": moon_buggy()
            elif clig.strip() == "06" or clig.strip() == "6": nudoku()
            elif clig.strip() == "07" or clig.strip() == "7": ttysolitaire()
            elif clig.strip() == "08" or clig.strip() == "8": pacman4console()
            elif clig.strip() == "00" or clig.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 17 - Malware Analysis
    elif lazymux.strip() == "17":
        print("\n    [01] Lynis: Security Auditing and Rootkit Scanner")
        print("    [02] Chkrootkit: A Linux Rootkit Scanners")
        print("    [03] ClamAV: Antivirus Software Toolkit")
        print("    [04] Yara: Tool aimed at helping malware researchers to identify and classify malware samples")
        print("    [05] VirusTotal-CLI: Command line interface for VirusTotal")
        print("    [06] avpass: Tool for leaking and bypassing Android malware detection system")
        print("    [07] DKMC: Dont kill my cat - Malicious payload evasion tool")
        print("\n    [00] Back to main menu\n")
        malsys = input("lzmx > set_install ")
        if malsys == "@":
            malsys = ""
            for x in range(1,201):
                malsys += f"{x} "
        if len(malsys.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for malx in malsys.split():
            if malx.strip() == "01" or malx.strip() == "1": lynis()
            elif malx.strip() == "02" or malx.strip() == "2": chkrootkit()
            elif malx.strip() == "03" or malx.strip() == "3": clamav()
            elif malx.strip() == "04" or malx.strip() == "4": yara()
            elif malx.strip() == "05" or malx.strip() == "5": virustotal()
            elif malx.strip() == "06" or malx.strip() == "6": avpass()
            elif malx.strip() == "07" or malx.strip() == "7": dkmc()
            elif malx.strip() == "00" or malx.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 18 - Compiler/Interpreter
    elif lazymux.strip() == "18":
        print("\n    [01] Python2: Python 2 programming language intended to enable clear programs")
        print("    [02] ecj: Eclipse Compiler for Java")
        print("    [03] Golang: Go programming language compiler")
        print("    [04] ldc: D programming language compiler, built with LLVM")
        print("    [05] Nim: Nim programming language compiler")
        print("    [06] shc: Shell script compiler")
        print("    [07] TCC: Tiny C Compiler")
        print("    [08] PHP: Server-side, HTML-embedded scripting language")
        print("    [09] Ruby: Dynamic programming language with a focus on simplicity and productivity")
        print("    [10] Perl: Capable, feature-rich programming language")
        print("    [11] Vlang: Simple, fast, safe, compiled language for developing maintainable software")
        print("    [12] BeanShell: Small, free, embeddable, source level Java interpreter with object based scripting language features written in Java")
        print("    [13] fp-compiler: Free Pascal is a 32, 64 and 16 bit professional Pascal compiler")
        print("    [14] Octave: Scientific Programming Language")
        print("    [15] BlogC: A blog compiler")
        print("    [16] Dart: General-purpose programming language")
        print("    [17] Yasm: Assembler supporting the x86 and AMD64 instruction sets")
        print("    [18] Nasm: A cross-platform x86 assembler with an Intel-like syntax.")
        print("\n    [00] Back to main menu\n")
        compter = input("lzmx > set_install ")
        if compter == "@":
            compter = ""
            for x in range(1,201):
                compter += f"{x} "
        if len(compter.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for compt in compter.split():
            if compt.strip() == "01" or compt.strip() == "1": python2()
            elif compt.strip() == "02" or compt.strip() == "2": ecj()
            elif compt.strip() == "03" or compt.strip() == "3": golang()
            elif compt.strip() == "04" or compt.strip() == "4": ldc()
            elif compt.strip() == "05" or compt.strip() == "5": nim()
            elif compt.strip() == "06" or compt.strip() == "6": shc()
            elif compt.strip() == "07" or compt.strip() == "7": tcc()
            elif compt.strip() == "08" or compt.strip() == "8": php()
            elif compt.strip() == "09" or compt.strip() == "9": ruby()
            elif compt.strip() == "10": perl()
            elif compt.strip() == "11": vlang()
            elif compt.strip() == "12": beanshell()
            elif compt.strip() == "13": fpcompiler()
            elif compt.strip() == "14": octave()
            elif compt.strip() == "15": blogc()
            elif compt.strip() == "16": dart()
            elif compt.strip() == "17": yasm()
            elif compt.strip() == "18": nasm()
            elif compt.strip() == "00" or compt.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    
    # 19 - Social Engineering Tools
    elif lazymux.strip() == "19":
        print("\n    [01] weeman: HTTP server for phishing in python")
        print("    [02] SocialFish: Educational Phishing Tool & Information Collector")
        print("    [03] santet-online: Social Engineering Tool")
        print("    [04] SpazSMS: Send unsolicited messages repeatedly on the same phone number")
        print("    [05] LiteOTP: Multi Spam SMS OTP")
        print("    [06] F4K3: Fake User Data Generator")
        print("    [07] Hac")
        print("    [08] Cookie-stealer: Crappy cookie stealer")
        print("    [09] zphisher: Automated Phishing Tool")
        print("    [10] Evilginx: Advanced Phishing With Two-factor Authentication Bypass")
        print("    [11] ghost-phisher: Automatically exported from code.google.com/p/ghost-phisher")
        print("\n    [00] Back to main menu\n")
        soceng = input("lzmx > set_install ")
        if soceng == "@":
            soceng = ""
            for x in range(1,201):
                soceng += f"{x} "
        if len(soceng.split()) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for socng in soceng.split():
            if socng.strip() == "01" or socng.strip() == "1": weeman()
            elif socng.strip() == "02" or socng.strip() == "2": socfish()
            elif socng.strip() == "03" or socng.strip() == "3": sanlen()
            elif socng.strip() == "04" or socng.strip() == "4": spazsms()
            elif socng.strip() == "05" or socng.strip() == "5": liteotp()
            elif socng.strip() == "06" or socng.strip() == "6": f4k3()
            elif socng.strip() == "07" or socng.strip() == "7": hac()
            elif socng.strip() == "08" or socng.strip() == "8": cookiestealer()
            elif socng.strip() == "09" or socng.strip() == "9": zphisher()
            elif socng.strip() == "10": evilginx()
            elif socng.strip() == "11": ghostphisher()
            elif socng.strip() == "00" or socng.strip() == "0": restart_program()
            else: print("\nERROR: Wrong Input");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)
    elif lazymux.strip() == "99":
        os.system("git pull")
    elif lazymux.strip() == "0" or lazymux.strip() == "00":
        sys.exit()
    
    else:
        print("\nERROR: Wrong Input")
        timeout(1)
        restart_program()

debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION=CURRENT_VERSION.replace('\n','')



import os,sys,random,requests



def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")
        


try:
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    
#text = """
#< [ Telegram Ewan_Ali ] > X < [ TikTok Ewan.Shex.Ali ] >"""[1:]


banner = r"""



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠶⠶⠚⠛⠛⠛⠛⠛⠛⠛⠷⠶⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⣀⠄⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⡤⠤⠤⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⢄⡀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠏⠀⢀⣀⣠⣶⠟⠁⠀⠀⠀⣠⠴⠀⢀⠔⠋⢁⠎⠀⡇⠘⡄⠉⠲⣍⠑⠢⢄⡀⠀⠀⠀⠙⣷⣦⣤⡀⠀⠙⣷⡀⠀⠀⠀
⠀⠀⢀⣾⠃⠀⣴⠏⣼⡿⣣⠀⠀⢀⡴⠋⠠⢄⡴⠃⠀⠀⡞⠀⠀⠃⠀⠹⡄⠀⠈⢳⡀⠤⠘⠢⡀⠀⠀⢾⢻⣷⡘⣦⡀⠈⢿⡄⠀⠀
⠀⠀⣾⠁⣠⢺⣿⢘⣭⣾⠃⠀⡰⠋⠀⠀⢀⡜⠁⠁⠀⢺⠀⣴⣞⡳⣶⡄⠁⠀⠉⠀⠱⡄⠀⠀⠈⠢⡀⠈⢷⣬⡓⢻⣷⢦⠈⢿⡄⠀
⠀⣼⠃⢰⡇⢸⣷⡿⢻⠁⢀⠞⠀⠀⠀⠀⡜⠀⠀⠀⠀⠈⠀⠈⠁⣷⠿⠃⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠱⡄⠀⢿⢿⣾⡿⢸⣧⠈⣷⠀
⢠⡟⠀⣾⣿⢸⣫⣶⠇⠀⡞⠀⠀⠒⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠃⠠⠀⠀⠀⢹⡀⠘⣷⣌⠧⢸⣿⠀⢸⡇
⣼⡇⣰⢻⣿⣸⡿⠋⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⢸⣿⣧⣼⡿⢀⠀⣷
⣿⠀⣿⡀⢿⡟⢡⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠸⣆⠻⣿⠃⣼⠀⢿
⣿⠀⢿⣷⠘⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡟⠀⣹⣯⡁⢸⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⢿⣦⠙⣼⣿⠀⢸
⣿⠀⠘⣿⣇⣿⡏⡄⠀⣄⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⠃⠀⢰⣇⠀⠀⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⢸⠁⢀⠸⣿⢰⣿⠇⠀⣾
⢻⡇⣷⡈⢻⣿⢀⣿⠀⢸⡀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⠀⢠⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⡾⠀⣼⡆⢿⡿⠃⣼⠀⣿
⠘⣧⠘⣿⣦⡙⢸⣿⣦⡀⢣⠀⡠⠤⠒⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⠒⠢⠤⣀⣰⠁⡰⣿⡇⢚⣴⣾⠏⢸⡇
⠀⢻⡄⢈⠻⣿⣼⣿⡇⣷⡈⢦⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⡰⢃⣼⠁⣿⣧⣾⡿⡃⢀⡿⠀
⠀⠈⢿⡀⢷⣌⠛⢿⣧⢸⣷⡀⠑⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠜⠁⣼⡟⢸⡿⠟⣉⡴⠃⣼⠃⠀
⠀⠀⠈⢿⡄⠻⢿⣶⣬⣁⢿⣧⢳⣄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⡖⣹⣿⢃⣥⣴⣾⠟⢁⣼⠃⠀⠀
⠀⠀⠀⠈⢻⣆⠀⢝⠻⠿⢿⣿⣦⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿⡿⠿⠟⣋⠁⢠⡾⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢷⡀⠙⠶⣶⣤⣤⣥⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣼⣥⣤⣶⡶⠛⢁⣴⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⢦⣀⠀⢭⣉⣙⣉⣉⣁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⣉⣉⣋⣉⡩⠁⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣤⡈⠙⠛⠻⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⢉⣠⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣄⣀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣀⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀


⠀⠀
                   █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█
                   █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄
                       
                   𝙲𝙰𝚁 𝙿𝙰𝚁𝙺𝙸𝙽𝙶 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙰𝚈𝙴𝚁
                         𝙿𝚁𝙴𝚂𝚂 𝙴𝙽𝚃𝙴𝚁                                 
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.red_to_yellow, pyColorate.Vertical, enter=True)


#pyAnime.Fade(pyCenter.Center(text), pyColors.purple_to_red, pyColorate.Vertical, enter=True)
#print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))

pySystem.Clear()

#print("\n"*2    )
#print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
#print("\n"*2)




from pystyle import Box
import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate
from pystyle import Center
import datetime



from cpmkurdish import CPMKurdish

__CHANNEL_USERNAME__ = "cpmkurdish_channel"
__GROUP_USERNAME__   = "cpmkurdish_group"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "                  ▄████▄   ██▓███   ███▄ ▄███▓▓█████  █     █░ ▄▄▄       ███▄    █ \n"
    brand_name += "                  ▒██▀ ▀█  ▓██░  ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓█░ █ ░█░▒████▄     ██ ▀█   █ \n"
    brand_name += "                  ▒▓█    ▄ ▓██░ ██▓▒▓██    ▓██░▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██  ▀█ ██▒\n"
    brand_name += "                  ▒▓▓▄ ▄██▒▒██▄█▓▒ ▒▒██    ▒██ ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▓██▒  ▐▌██▒\n"
    brand_name += "                  ▒ ▓███▀ ░▒██▒ ░  ░▒██▒   ░██▒░▒████▒░░██▒██▓  ▓█   ▓██▒▒██░   ▓██░\n"
    brand_name += "                  ░ ░▒ ▒  ░▒▓▒░ ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░   ▒ ▒ \n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter( '─══════════════════════════════════════════☆☆═════════════════════════════════════════─')))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋")))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃")))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f" 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}")))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter('─════════════════════════════[ 𝖯𝖫𝖠𝖸𝖤𝖱 𝖣𝖤𝖳𝖠𝖨𝖫𝖲 ]════════════════════════════─')))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f'Name: {(data.get("Name") if "Name" in data else "UNDEFINED")} <> LocalID: {data.get("localID")} <> Money: {data.get("money")} <> Coins: {data.get("coin")}')))
                
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ERROR: new accounts most be signed-in to the game at least once !.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ERROR: seems like your login is not properly set !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter('─══════════════════════[ 𝖠𝖢𝖢𝖤𝖲𝖲 𝖪𝖤𝖸 𝖣𝖤𝖳𝖠𝖨𝖫𝖲 ]══════════════════════─')))
    
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f'Access Key: {data.get("access_key")} <> Telegram ID: {data.get("telegram_id")} <> Balance: {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}')))
    
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} CANNOT BE EMPTY OR JUST SPACES, PLEASE TRY AGAIN'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter('─═════════════════════[ 𝖫𝖮𝖢𝖠𝖳𝖨𝖮𝖭 ]═════════════════════─')))
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f'Country: {data.get("country")} <> Region: {data.get("regionName")} <> City: {data.get("city")}')))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[?] ACCOUNT EMAIL", "Email", password=False)
        acc_password = prompt_valid_value("[?] ACCOUNT PASSWORD", "Password", password=False)
        acc_access_key = prompt_valid_value("[?] ACCESS KEY", "Access Key", password=False)
        console.print("[%] TRYING TO LOGIN: ", end=None)
        cpm = CPMKurdish(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'WRONG PASSWORD'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'INVALID ACCESS KEY'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TRY AGAIN'))
                print(Colorate.Horizontal(Colors.rainbow, '! NOTE: MAKE SURE YOU FILLED OUT THE FIELDS'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(Box.DoubleCube( '                             𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝑇𝑂 𝑈𝑆𝐸 𝑀𝑌 𝑇𝑂𝑂𝐿\n\n             𝑁𝑂𝑇𝐸: 𝑇𝐻𝐸 𝑈𝑁𝐿𝐼𝑀𝐼𝑇𝐸𝐷 𝐵𝐴𝐿𝐴𝑁𝐶𝐸 𝑂𝑁𝐿𝑌 𝑊𝑂𝑅𝐾𝑆 𝐹𝑂𝑅 𝑂𝑁𝐸 𝑀𝑂𝑁𝑇𝐻\n\n\n01: Unlock Paid Cars           [3.500K] & 02: Increase Money            [1.000K]\n\n\n03: Unlock Coin Cars           [3.000K] & 04: Increase Coins            [3.000K]\n\n\n05: Unlock All Cars            [4.000K] & 06: King Rank                 [3.500K]\n\n\n07: Unlock all Cars Siren      [3.500K] & 08: Change ID                 [2.500K]\n\n\n09: Unlock w16 Engine          [3.000K] & 10: Change Name               [1..00K]\n\n\n11: Unlock All Horns           [3.000K] & 12: Change Name (Rainbow)     [1..00K]\n\n\n13: Unlock Disable Damage      [2.000K] & 14: Number Plates             [2.000K]\n\n\n15: Unlock Unlimited Fuel      [2.000K] & 16: Account Delete            [F.REE.]\n\n\n17: Unlock All Wheels          [2.500K] & 18: Account Register          [F.REE.]\n\n\n19: Unlock House 3             [2.500K] & 20: Delete Friends            [5..00K]\n\n\n21: Unlock Smoke               [2.000K] & 22: Change Race Wins          [7..00K]\n\n\n23: Change Race Loses          [7..00K] & 24: Custom Engine             [4.000K]\n\n\n25: remove car bumper (Car_ID) [2.000K] & 26: Speed Car Hack (Car_ID)   [1.500K]\n\n\n27: Speed All Cars Hack        [2.500K] & 28: Chrome All Cars           [3.500K]\n\n\n29: All Cars Max Milage        [2.000K] & 30: Clone Account             [5.000K]\n\n\n31: Unlock All Tuning          [1.000K] & 32: Steering Angle (Car_ID)   [1.500K]\n\n\n33: Unlock Equipaments Male    [3.000K] & 34: Unlock Equipaments Female [3.000K]\n\n\n35: Fake clan Dressing Male    [2.000K] & 36:﻿Fake clan Dressing Famale [2.000K]\n\n\n37: Remove Head Male           [2.500K] & 38: Remove Head Famale        [2.500K]\n\n\n                         𝑇𝐸𝐿𝐸𝐺𝑅𝐴𝑀 𝐵𝑂𝑇:- @CPMKurdishBot\n\n       𝑈𝑁𝐿𝐼𝑀𝐼𝑇𝐸𝐷 𝐵𝐴𝐿𝐴𝑁𝐶𝐸 𝐹𝑂R 𝐸𝑉𝐸𝑅𝑌 𝑃𝐸𝑅𝑆𝑂𝑁 𝑊𝐻𝑂 𝐴𝐷𝐷𝑆 100 𝑃𝐸𝑂𝑃𝐿𝐸 𝑇𝑂 𝑀𝑌 𝐺𝑅𝑂𝑈𝑃'))))
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(Box.DoubleCube(  ' ➩{39}: GO TO ANOTHER ACCOUNT'))))
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(Box.DoubleCube(  ' ➩{0}: Exit'))))
            print(Colorate.Horizontal(Colors.rainbow, '                               ─═══════════════[ ☆SERVICE☆ ]═══════════════─'))
            
            service = IntPrompt.ask(f"[bold]                                     [?] SELECT A SERVICE[red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))



            elif service == 1: # Unlock All Paid Cars
                print(Colorate.Horizontal(Colors.rainbow, "[!] NOTE: THIS FUNCTION TAKES A WHILE TO COMPLETE, PLEASE DON'T CANCEL"))
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL PAID CARS: "))
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 2: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSERT HOW MUCH MONEY DO YOU WANT'))
                amount = IntPrompt.ask("[?] AMOUNT")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA:"))
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)



                    continue
            elif service == 3: # Unlock All coins Cars
                print(Colorate.Horizontal(Colors.rainbow, "[!] NOTE: THIS FUNCTION TAKES A WHILE TO COMPLETE, PLEASE DON'T CANCEL"))
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL COIN CARS: "))
                if cpm.unlock_coins_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue              
                    
                          
                                      
            elif service == 4: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] INSERT HOW MUCH COINS DO YOU WANT'))
                amount = IntPrompt.ask("[red][?] AMOUNT[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA: "))
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)



                    continue



            elif service == 5: # Unlock All Cars
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL CARS: "))
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 6: # King Rank
                print(Colorate.Horizontal(Colors.rainbow, "[!] NOTE: IF THE KING RANK DOESN'T APPEAR IN GAME, CLOSE IT AND OPEN FEW TIMES"))
                print(Colorate.Horizontal(Colors.rainbow, "[!] NOTE: PLEASE DON'T DO KING RANK ON SAME ACCOUNT TWICE"))
                sleep(2)
                print(Colorate.Horizontal(Colors.rainbow, "[%] GIVING YOU A KING RANK: "))
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)



                    continue



            elif service == 7: # Unlock All Cars Siren
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL CARS SIREN: "))
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 8: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW ID'))
                new_id = Prompt.ask("[red][?] ID[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA: "))
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID ID'))
                    sleep(2)
                    continue



            elif service == 9: # Unlock w16 Engine
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING W16 ENGINE: "))
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 10: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW NAME'))
                new_name = Prompt.ask("[red][?] NAME[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA: "))
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 11: # Unlock All Horns
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING ALL HORNS: "))
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 12: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] ENTER YOUR NEW RAINBOW NAME'))
                new_name = Prompt.ask("[red][?] NAME[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] SAVING YOUR DATA: "))
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 13: # Disable Engine Damage
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING DISABLE DAMAGE: "))
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 14: # Number Plates
                print(Colorate.Horizontal(Colors.rainbow, "[%] GIVING YOU A NUMBER PLATES: "))
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 15: # Unlimited Fuel
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING UNLIMITED FUEL: "))
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 16: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] AFTER DELETING YOUR ACCOUNT THERE IS NO GOING BACK'))
                answ = Prompt.ask("[red][?] DO YOU WANT TO DELETE THIS ACCOUNT[/red]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                else: continue



            elif service == 17: # Unlock Car Wheels
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING All WHEELS: "))
                if cpm.unlock_car_wheel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                  



            elif service == 18: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] REGISTRING NEW ACCOUNT'))
                acc2_email = prompt_valid_value("[red][?] ACCOUNT EMAIL[/red]", "Email", password=False)
                acc2_password = prompt_valid_value("[red][?] ACCOUNT PASSWORD[/red]", "Password", password=False)
                print(Colorate.Horizontal(Colors.rainbow, "[%] CREATING NEW ACCOUNT: "))
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, f'INFO: IN ORDER TO TWEAK THIS ACCOUNT WITH Ewan_Kurdish.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'YOU MOST SIGN-IN TO THE GAME USING THIS CCOUNT'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'THIS EMAIL IS ALREADY EXISTS'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 19: # Unlock House 3
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING HOUSE 3:"))
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 20: # Delete Friends
                print(Colorate.Horizontal(Colors.rainbow, "[%] DELETING FRIENDS[/red]: "))
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 21: # Unlock Smoke
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCKING SMOKE: "))
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 22: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you win.'))
                amount = IntPrompt.ask("[red][?] Amount[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] CHANGING YOUR DATA: "))
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 23: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] INSERT HOW MUCH RACES YOU LOSE'))
                amount = IntPrompt.ask("[red][?] AMOUNT[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] CHANGING YOUR DATA: "))
                if amount > 0 and amount <= 999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                        print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue



            elif service == 24: # custom engine
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))            
                hp = IntPrompt.ask("[red][?] HP[/red]")                
                innerhp = IntPrompt.ask("[red][?] INNER HP[/red]")
                nm = IntPrompt.ask("[red][?] NM[/red]")
                innernm = IntPrompt.ask("[red][?] INNER NM[/red]")
                gearbox = IntPrompt.ask("[red][?] GEARBOX[/red]")                
                print(Colorate.Horizontal(Colors.rainbow, "[%] CUSTOM ENGINE: "))
                if cpm.custom_engine(hp, innerhp, nm, innernm, gearbox):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    



            elif service == 25: # remove bumper
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[red][?] CAR ID[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] REMOVE ALL BUMPERS: "))
                if cpm.car_bumper(car_id):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 26: # Hack Car Speed (299hp)
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[red][?] CAR ID[/red]")
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING CAR SPEED: "))
                if cpm.hack_car_speed(car_id):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue



            elif service == 27: # Hack All Car Speed 99hp
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL SPEED CAN NOT BE RESTORED'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING ALL CARS SPEED: "))
                if cpm.hack_car_sexo():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 28: # Chrome All Cars
                print(Colorate.Horizontal(Colors.rainbow, '[!] CHROME'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING All CARS CHROME: "))
                if cpm.chrome_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue               
                    
                    
                    
            elif service == 29: # ALL CARS MAX MILAGE
                print(Colorate.Horizontal(Colors.rainbow, '[!] NOTE: ORIGINAL MILAGE CAN NOT BE RESTORED'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING MILAGE: "))
                if cpm.hack_car_milage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                           
                    
                                                 
                                                                       
            elif service == 30: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE ENTER ACCOUNT DETALIS'))
                to_email = prompt_valid_value("[red][?] ACCOUNT EMAIL[/red]", "Email", password=False)
                to_password = prompt_valid_value("[red][?] ACCOUNT PASSWORD[/red]", "Password", password=False)
                print(Colorate.Horizontal(Colors.rainbow, "[%] CLONING YOU ACCOUNT: "))
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE USE VALID VALUES'))
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 31: # Unlock Tuning
                print(Colorate.Horizontal(Colors.rainbow, '[!] TUNING'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] UNLOCK ALL TUNING: "))
                if cpm.unlock_tuning():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                   
                    
                    
                    
            elif service == 32: # ANGLE
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER CAR DETALIS'))
                car_id = IntPrompt.ask("[red][?] CAR ID[/red]")
                print(Colorate.Horizontal(Colors.rainbow, '[!] ENTER STEERING ANGLE'))
                custom = IntPrompt.ask("[red][?]﻿ENTER THE AMOUNT OF ANGLE YOU WANT[/red]")                
                print(Colorate.Horizontal(Colors.rainbow, "[%] HACKING CAR ANGLE: "))
                if cpm.max_max1(car_id, custom):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    
                    
                    
                    
            elif service == 33: # Unlocking Equipaments Male
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))
                print(Colorate.Horizontal(Colors.rainbow, "[%] Unlocking Equipaments Male: "))
                if cpm.unlock_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    
                    
                    
                    
            elif service == 34: # Unlocking Equipaments Female
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))
                print(Colorate.Horizontal(Colors.rainbow, "[%] Unlocking Equipaments Female: "))
                if cpm.unlock_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    
                    
                    
                    
            elif service == 35: # Unlocking clan Equipaments Male
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] ﻿FAKE CLAN DRSSING MALE: "))
                if cpm.unlock_clan_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                   
                    
                     
                       
            elif service == 36: # Unlocking clan Equipaments Female
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] FAKE CLAN DRSSING FEMALE: "))
                if cpm.unlock_clan_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                        
                    
                    
                    
            elif service == 37: # remove head Male
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] REMOVE HEAD MALE: "))
                if cpm.unlock_remove_face_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                    
                    
                    
                    
            elif service == 38: # remove head Female
                print(Colorate.Horizontal(Colors.rainbow, ' %100'))            
                print(Colorate.Horizontal(Colors.rainbow, "[%] REMOVE HEAD FEMALE: "))
                if cpm.unlock_remove_face_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED'))
                    print(Colorate.Horizontal(Colors.rainbow, 'PLEASE TRY AGAIN'))
                    sleep(2)
                    continue                                                            
                    
                    
                    
            elif service == 39: # OPENING ANOTHER ACCOUNT
                print(Colorate.Horizontal(Colors.rainbow, '[!] PLEASE ENTER ACCOUNT DETALIS'))
                account_email = prompt_valid_value("[red][?] ACCOUNT EMAIL[/red]", "Email", password=False)
                to_password = prompt_valid_value("[red][?] ACCOUNT PASSWORD[/red]", "Password", password=False)
                print(Colorate.Horizontal(Colors.rainbow, "[%] OPENING ANOTHER ACCOUNT: "))
                if cpm.another_account(account_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND'))
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'THANK YOU FOR USING OUR TOOL, PLEASE JOIN OUR TELEGRAM CHANNEL: @{__CHANNEL_USERNAME__}'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    sleep(2)
                    continue                    
            else: continue
            break
        break
