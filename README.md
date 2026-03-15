### All in One Hacking tool For Hackers
![](https://img.shields.io/github/license/Z4nzu/hackingtool)
![](https://img.shields.io/github/issues/Z4nzu/hackingtool)
![](https://img.shields.io/github/issues-closed/Z4nzu/hackingtool)
![](https://img.shields.io/badge/Python-3.10+-blue)
![](https://img.shields.io/badge/version-2.0.0-green)
![](https://img.shields.io/github/forks/Z4nzu/hackingtool)
![](https://img.shields.io/github/stars/Z4nzu/hackingtool)
![](https://img.shields.io/github/last-commit/Z4nzu/hackingtool)
![](https://img.shields.io/badge/platform-Linux%20%7C%20KaliLinux%20%7C%20ParrotOs%20%7C%20macOS-blue)

## What's new in v2.0.0
- Python 3.10+ required — all Python 2 code removed
- OS-aware menus — Linux-only tools are hidden automatically on macOS
- Archived tools (Python 2, unmaintained) shown in a separate sub-menu
- All `os.chdir()` bugs fixed — tools install to `~/.hackingtool/tools/`
- No more `sudo git clone` — tools install to user home, no root needed
- 22 new modern tools added across 6 categories
- Rich terminal UI with shared theme — no more 32 different console instances
- Iterative menus — no more recursion stack overflow on deep navigation
- Docker image builds locally — no unverified external images
- requirements.txt cleaned — removed unused flask/boxes/lolcat/requests

# Hackingtool Menu
- [Anonymously Hiding Tools](#anonymously-hiding-tools)
- [Information gathering tools](#information-gathering-tools)
- [Wordlist Generator](#wordlist-generator)
- [Wireless attack tools](#wireless-attack-tools)
- [SQL Injection Tools](#sql-injection-tools)
- [Phishing attack tools](#phishing-attack-tools)
- [Web Attack tools](#web-attack-tools)
- [Post exploitation tools](#post-exploitation-tools)
- [Forensic tools](#forensic-tools)
- [Payload creation tools](#payload-creation-tools)
- [Exploit framework](#exploit-framework)
- [Reverse engineering tools](#reverse-engineering-tools)
- [DDOS Attack Tools](#ddos-attack-tools)
- [Remote Administrator Tools (RAT)](#remote-administrator-tools-rat)
- [XSS Attack Tools](#xss-attack-tools)
- [Steganography tools](#steganography-tools)
- [Other tools](#other-tools)
    - [SocialMedia Bruteforce](#socialmedia-bruteforce)
    - [Android Hacking tools](#android-hacking-tools)
    - [IDN Homograph Attack](#idn-homograph-attack)
    - [Email Verify tools](#email-verify-tools)
    - [Hash cracking tools](#hash-cracking-tools)
    - [Wifi Deauthenticate](#wifi-deauthenticate)
    - [SocialMedia Finder](#socialmedia-finder)
    - [Payload Injector](#payload-injector)
    - [Web crawling](#web-crawling)
    - [Mix tools](#mix-tools)


### Anonymously Hiding Tools
- [Anonymously Surf](https://github.com/Und3rf10w/kali-anonsurf)
- [Multitor](https://github.com/trimstray/multitor)

### Information gathering tools
- [Network Map (nmap)](https://github.com/nmap/nmap)
- [Dracnmap](https://github.com/Screetsec/Dracnmap)
- Port scanning
- Host to IP
- [Xerosploit](https://github.com/LionSec/xerosploit)
- [RED HAWK (All In One Scanning)](https://github.com/Tuhinshubhra/RED_HAWK)
- [ReconSpider](https://github.com/bhavsec/reconspider)
- IsItDown (Check Website Down/Up)
- [Infoga - Email OSINT](https://github.com/m4ll0k/Infoga)
- [ReconDog](https://github.com/s0md3v/ReconDog)
- [Striker](https://github.com/s0md3v/Striker)
- [SecretFinder (API keys, tokens)](https://github.com/m4ll0k/SecretFinder)
- [Find Info Using Shodan](https://github.com/m4ll0k/Shodanfy.py)
- [Port Scanner - rang3r](https://github.com/floriankunushevci/rang3r)
- [Breacher](https://github.com/s0md3v/Breacher)
- [theHarvester](https://github.com/laramies/theHarvester) ★ new
- [Amass](https://github.com/owasp-amass/amass) ★ new
- [Masscan](https://github.com/robertdavidgraham/masscan) ★ new
- [RustScan](https://github.com/RustScan/RustScan) ★ new
- [Holehe](https://github.com/megadose/holehe) ★ new
- [Maigret](https://github.com/soxoj/maigret) ★ new
- [httpx](https://github.com/projectdiscovery/httpx) ★ new

### Wordlist Generator
- [Cupp](https://github.com/Mebus/cupp)
- [WordlistCreator](https://github.com/Z4nzu/wlcreator)
- [Goblin WordGenerator](https://github.com/UndeadSec/GoblinWordGenerator)
- [Password list (1.4B Passwords)](https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got)
- [Hashcat](https://github.com/hashcat/hashcat) ★ new
- [John the Ripper](https://github.com/openwall/john) ★ new
- [haiti (Hash Identifier)](https://github.com/noraj/haiti) ★ new

### Wireless attack tools
- [WiFi-Pumpkin](https://github.com/P0cL4bs/wifipumpkin3)
- [pixiewps](https://github.com/wiire/pixiewps)
- [Bluetooth Honeypot GUI Framework](https://github.com/andrewmichaelsmith/bluepot)
- [Fluxion](https://github.com/thehackingsage/Fluxion)
- [Wifiphisher](https://github.com/wifiphisher/wifiphisher)
- [Wifite](https://github.com/derv82/wifite2)
- [EvilTwin](https://github.com/Z4nzu/fakeap)
- [Fastssh](https://github.com/Z4nzu/fastssh)
- Howmanypeople
- [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon) ★ new
- [hcxdumptool](https://github.com/ZerBea/hcxdumptool) ★ new
- [hcxtools](https://github.com/ZerBea/hcxtools) ★ new

### SQL Injection Tools
- [Sqlmap](https://github.com/sqlmapproject/sqlmap)
- [NoSqlMap](https://github.com/codingo/NoSQLMap)
- [Damn Small SQLi Scanner](https://github.com/stamparm/DSSS)
- [Explo](https://github.com/dtag-dev-sec/explo)
- [Blisqy - Time-based blind SQLi](https://github.com/JohnTroony/Blisqy)
- [Leviathan - Wide Range Mass Audit](https://github.com/leviathan-framework/leviathan)
- [SQLScan](https://github.com/Cvar1984/sqlscan)

### Phishing attack tools
- [Autophisher](https://github.com/CodingRanjith/autophisher)
- [PyPhisher](https://github.com/KasRoudra/PyPhisher)
- [AdvPhishing](https://github.com/Ignitetch/AdvPhishing)
- [Setoolkit](https://github.com/trustedsec/social-engineer-toolkit)
- [SocialFish](https://github.com/UndeadSec/SocialFish)
- [HiddenEye](https://github.com/Morsmalleo/HiddenEye)
- [Evilginx3](https://github.com/kgretzky/evilginx2)
- [I-See-You (Location via phishing)](https://github.com/Viralmaniar/I-See-You)
- [SayCheese (Webcam grab)](https://github.com/hangetzzu/saycheese)
- [QR Code Jacking](https://github.com/cryptedwolf/ohmyqr)
- [BlackEye](https://github.com/thelinuxchoice/blackeye)
- [ShellPhish](https://github.com/An0nUD4Y/shellphish)
- [Thanos](https://github.com/TridevReddy/Thanos)
- [QRLJacking](https://github.com/OWASP/QRLJacking)
- [Maskphish](https://github.com/jaykali/maskphish)
- [BlackPhish](https://github.com/iinc0gnit0/BlackPhish)
- [dnstwist](https://github.com/elceef/dnstwist)

### Web Attack tools
- [Web2Attack](https://github.com/santatic/web2attack)
- Skipfish
- [SubDomain Finder (Sublist3r)](https://github.com/aboul3la/Sublist3r)
- [CheckURL](https://github.com/UndeadSec/checkURL)
- [Sub-Domain TakeOver](https://github.com/edoardottt/takeover)
- [Dirb](https://gitlab.com/kalilinux/packages/dirb)
- [Nuclei](https://github.com/projectdiscovery/nuclei) ★ new
- [ffuf](https://github.com/ffuf/ffuf) ★ new
- [Feroxbuster](https://github.com/epi052/feroxbuster) ★ new
- [Nikto](https://github.com/sullo/nikto) ★ new
- [wafw00f](https://github.com/EnableSecurity/wafw00f) ★ new
- [Katana](https://github.com/projectdiscovery/katana) ★ new

### Post exploitation tools
- [Vegile - Ghost In The Shell](https://github.com/Screetsec/Vegile)
- [Chrome Keylogger](https://github.com/UndeadSec/HeraKeylogger)
- [pwncat-cs](https://github.com/calebstewart/pwncat) ★ new

### Forensic tools
- Autopsy
- Wireshark
- [Bulk extractor](https://github.com/simsong/bulk_extractor)
- [Disk Clone / Image Acquire (Guymager)](https://guymager.sourceforge.io/)
- [Toolsley](https://www.toolsley.com/)
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) ★ new
- [Binwalk](https://github.com/ReFirmLabs/binwalk) ★ new

### Payload creation tools
- [The FatRat](https://github.com/Screetsec/TheFatRat)
- [Brutal](https://github.com/Screetsec/Brutal)
- [Stitch](https://nathanlopez.github.io/Stitch)
- [MSFvenom Payload Creator](https://github.com/g0tmi1k/msfpc)
- [Venom Shellcode Generator](https://github.com/r00t-3xp10it/venom)
- [Spycam](https://github.com/indexnotfound404/spycam)
- [Mob-Droid](https://github.com/kinghacker0/Mob-Droid)
- [Enigma](https://github.com/UndeadSec/Enigma)

### Exploit framework
- [RouterSploit](https://github.com/threat9/routersploit)
- [WebSploit](https://github.com/The404Hacking/websploit)
- [Commix](https://github.com/commixproject/commix)
- [Web2Attack](https://github.com/santatic/web2attack)

### Reverse engineering tools
- [Androguard](https://github.com/androguard/androguard)
- [Apk2Gold](https://github.com/lxdvs/apk2gold)
- [JadX](https://github.com/skylot/jadx)

### DDOS Attack Tools
- [DDoS Script (36+ methods)](https://github.com/the-deepnet/ddos)
- [SlowLoris](https://github.com/gkbrk/slowloris)
- [Asyncrone | SYN Flood DDoS](https://github.com/fatihsnsy/aSYNcrone)
- [UFOnet](https://github.com/epsylon/ufonet)
- [GoldenEye](https://github.com/jseidl/GoldenEye)
- [SaphyraDDoS](https://github.com/anonymous24x7/Saphyra-DDoS)

### Remote Administrator Tools (RAT)
- [Pyshell](https://github.com/knassar702/pyshell)

### XSS Attack Tools
- [DalFox](https://github.com/hahwul/dalfox)
- [XSS Payload Generator](https://github.com/capture0x/XSS-LOADER)
- [Extended XSS Searcher](https://github.com/Damian89/extended-xss-search)
- [XSS-Freak](https://github.com/PR0PH3CY33/XSS-Freak)
- [XSpear](https://github.com/hahwul/XSpear)
- [XSSCon](https://github.com/menkrep1337/XSSCon)
- [XanXSS](https://github.com/Ekultek/XanXSS)
- [XSStrike](https://github.com/UltimateHackers/XSStrike)
- [RVuln](https://github.com/iinc0gnit0/RVuln)

### Steganography tools
- SteganoHide
- [StegoCracker](https://github.com/W1LDN16H7/StegoCracker)
- [Whitespace](https://github.com/beardog108/snow10)

### Other tools
#### SocialMedia Bruteforce
- [AllinOne SocialMedia Attack](https://github.com/Matrix07ksa/Brute_Force)
- [Facebook Attack](https://github.com/Matrix07ksa/Brute_Force)
- [Application Checker](https://github.com/jakuta-tech/underhanded)

#### Android Hacking tools
- [Keydroid](https://github.com/F4dl0/keydroid)
- [MySMS](https://github.com/papusingh2sms/mysms)
- [Lockphish](https://github.com/JasonJerry/lockphish)
- [DroidCam / WishFish](https://github.com/kinghacker0/WishFish)
- [EvilApp](https://github.com/crypticterminal/EvilApp)

#### IDN Homograph Attack
- [EvilURL](https://github.com/UndeadSec/EvilURL)

#### Email Verify tools
- [Knockmail](https://github.com/4w4k3/KnockMail)

#### Hash cracking tools
- [Hash Buster](https://github.com/s0md3v/Hash-Buster)

#### Wifi Deauthenticate
- [WifiJammer-NG](https://github.com/MisterBianco/wifijammer-ng)
- [KawaiiDeauther](https://github.com/aryanrtm/KawaiiDeauther)

#### SocialMedia Finder
- [Find SocialMedia By Facial Recognition](https://github.com/Greenwolf/social_mapper)
- [Find SocialMedia By UserName](https://github.com/xHak9x/finduser)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [SocialScan](https://github.com/iojw/socialscan)

#### Payload Injector
- [Debinject](https://github.com/UndeadSec/Debinject)
- [Pixload](https://github.com/chinarulezzz/pixload)

#### Web crawling
- [Gospider](https://github.com/jaeles-project/gospider)

#### Mix tools
- Terminal Multiplexer (tilix)
- [Crivo](https://github.com/GMDSantana/crivo)


## Installation

**Requires Python 3.10+**

```bash
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool
chmod -R 755 .
sudo python3 install.py
```

Then run:
```bash
sudo hackingtool
```

## Docker

```bash
# Build image
docker build -t hackingtool .

# Run
docker-compose up -d

# Interact
docker exec -it hackingtool bash
```

## Requirements

- Python 3.10+
- Linux (Kali, Parrot, Ubuntu) or macOS
- Go 1.21+ (for nuclei, ffuf, amass, httpx, katana, dalfox)
- Ruby (for haiti)

Install Python deps:
```bash
pip install -r requirements.txt
```


#### Thanks to all original authors of the tools used in hackingtool

**Please don't use for illegal activity.**

## Social Media
[![Twitter](https://img.shields.io/twitter/url?color=%231DA1F2&label=follow&logo=twitter&logoColor=%231DA1F2&style=flat-square&url=https%3A%2F%2Ftwitter.com%2F_Zinzu07)](https://twitter.com/_Zinzu07)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&link=https://github.com/Z4nzu/)](https://github.com/Z4nzu/)

##### Your favourite tool is not listed? [Suggest it here](https://forms.gle/b235JoCKyUq5iM3t8)
