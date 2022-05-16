#!/bin/python3.10

############################################
#
# Libadwaita Theme Changer
# created by OdzioM
#
############################################

import sys
import os

ThemeItems = ["gtk-4.0/gtk.css", "gtk-4.0/gtk-dark.css", "gtk-4.0/assets", "assets"]

def removeIfExists(path):
    if os.path.islink(path):
        print(path)
        os.remove(path)

def removeCurrentTheme(conf_dir):
    for item in ThemeItems:
        removeIfExists(os.path.join(conf_dir, item))

def setNewTheme(theme_dir, conf_dir):
    for item in ThemeItems:
        os.symlink(os.path.join(theme_dir, item), os.path.join(conf_dir, item))

if __name__ == "__main__":
    abs_home_dir = os.getenv('HOME')
    rel_config_dir = ".config"
    rel_themes_dir = ".themes"
    abs_config_dir = os.path.join(abs_home_dir, rel_config_dir)
    abs_themes_dir = os.path.join(abs_home_dir, rel_themes_dir)
    if "--reset" in sys.argv:
        print(f'\n***\nResetting theme to default!\n***\n')
        removeCurrentTheme(abs_config_dir)
    else:
        all_themes = os.listdir(abs_themes_dir)
        print("Select theme: ")
        for i, theme in enumerate(all_themes):
            print(f'{i+1}. {theme}')
        print("Anything else to exit")
        chk = input("Your choice: ")
        if chk.isdigit() and int(chk) <= len(all_themes):
            chk_value = int(chk)-1
            chk_theme = all_themes[chk_value]
            print(f'\n***\nChose {chk_theme}\n***\n')
            print("Removing previous theme...")
            removeCurrentTheme(abs_config_dir)
            print("Installing new theme...")
            setNewTheme(os.path.join(abs_themes_dir, chk_theme), abs_config_dir)
            print("Done.")
        else:
            print("Bye bye!")
