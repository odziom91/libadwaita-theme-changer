# libadwaita-theme-changer
Theme changer for Libadwaita

## Disclaimer!
Use this script at your own risk!
## How it works?
It just create simlinks between .themes and .config folder with assets and GTK 4.0 theme CSS files.

## Requirements
Python 3≥
Theme must be prepared for GTK 4.0.<br/>
In ``~/.theme``, go to your current theme directory and it should be ``gtk-4.0`` and ``assets`` directories.

## How to use?
1. Download Python script from git:
```
git clone https://github.com/odziom91/libadwaita-theme-changer.git
cd libadwaita-theme-changer
```
2. Add run permissions to file:
```
chmod +x libadwaita-tc.py
```
3. Run script:
```
python3 libadwaita-tc.py
```

## How to reset to default Adwaita theme?
Run script with --reset parameter:
```
./libadwaita-tc.py --reset
```

## Contact
Polish Discord channel "Polska Społeczność Linuxa": https://discord.gg/AnG2Kv6axS
