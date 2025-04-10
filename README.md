# IP Calculator 🖥️🔢

![Banner](https://i.imgur.com/example.png) *ASCII art banner from the program*

## 📝 Description
This is a Python-based IP Calculator that provides detailed network information when given an IP address with CIDR notation. The tool calculates various network properties and offers additional networking utilities.

## ✨ Features
- Calculate network address, broadcast address, and subnet mask
- Determine IP class (A, B, C, D, E) and type (Private/Public/Reserved)
- Show host range and total available hosts
- Additional networking tools:
  - Ping hosts
  - DNS resolution (nslookup)
  - Traceroute functionality

## 📥 Installation
1. Ensure you have Python 3.x installed
2. Clone this repository or download the files
3. Install required dependencies:
   ```bash
   pip install prettytable
   ```

## 🚀 Usage
Run the program with:
```bash
python main.py
```

### Main Functionality
Enter an IP address with CIDR notation when prompted:
```
(IP) -> 192.168.1.0/24
```

### Available Commands
| Command | Description |
|---------|-------------|
| `about` | About this program |
| `clear`/`cls` | Clear the console |
| `exit` | Exit the program |
| `help` | Show help message |
| `version` | Show version |
| `logo`/`banner` | Show the ASCII art banner |
| `ping <hostname>` | Ping a hostname |
| `nslookup <hostname>` | Resolve a hostname |
| `tracert <hostname>` | Trace route to a hostname |

## 📊 Example Output
```
+-------------------+-------------------------------+
| Property          | Value                         |
+-------------------+-------------------------------+
| IP Address        | 192.168.1.0/24                |
| Network Address   | 192.168.1.0                   |
| Net-ID bit        | 24                            |
| Host-IP bit       | 8                             |
| Total Hosts       | 254                           |
| Class             | Private/C                     |
| Broadcast Address | 192.168.1.255                 |
| NetMask           | 255.255.255.0                 |
| Wildcard Mask     | 0.0.0.255                     |
| Host Range        | 192.168.1.1 - 192.168.1.254   |
+-------------------+-------------------------------+
```

## 🛠️ Dependencies
- Python 3.x
- `prettytable` library
- Standard Python libraries: `ipaddress`, `os`, `sys`, `time`

## 📜 License
This project is open-source and available for personal and educational use.

## 🙋‍♂️ Author
Created by @coluich

## 🔄 Version
Current version: 1.0.0