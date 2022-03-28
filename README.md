# libadwaita-theme-changer
Theme changer for Libadwaita

## Disclaimer!
Use this script at your own risk!
## How it works?
It just create simlinks between .themes and .config folder with assets and GTK 4.0 theme CSS files.

## Requirements
Theme must be prepared for GTK 4.0.<br/>
In downloaded theme directory should be ``gtk-4.0`` and ``assets`` directories.

## How to use?
1. Download Python script from git:
```
git clone https://github.com/odziom91/libadwaita-theme-changer.git
```
2. Add run permissions to file:
```
chmod +x libadwaita-tc.py
```
3. Run script:
```
./libadwaita-tc.py
```

## How to reset to default Adwaita theme?
Run script with --reset parameter:
```
./libadwaita-tc.py --reset
```

## Contact
Polish Discord channel "Polska Społeczność Linuxa": https://discord.gg/tfsUgwPyVx