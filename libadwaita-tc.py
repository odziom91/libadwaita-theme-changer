#!/bin/python3

############################################
#
# Libadwaita Theme Changer
# created by OdzioM
#
############################################

import sys
import os
import subprocess as sp


if __name__ == "__main__":
    try:
        home_dir = os.getenv('HOME')
        config_dir = "/.config"
        themes_dir = "/.themes"
        if "--reset" in sys.argv:
            print(f'\n***\nResetting theme to default!\n***\n')
            sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/gtk.css'])
            sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/gtk-dark.css'])
            sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/assets'])
            sp.run(["rm", f'{home_dir}{config_dir}/assets'])
        else:
            all_themes = str(sp.run(["ls", f'{home_dir}{themes_dir}/'], stdout=sp.PIPE).stdout.decode("UTF-8")).split()
            print("Select theme: ")
            for i, theme in enumerate(all_themes):
                print(f'{i+1}. {theme}')
            print("e. Exit")
            chk = input("Your choice: ")
            match chk:
                case "e":
                    print("Bye bye!")
                case _:
                    chk_value = int(chk)-1
                    chk_theme = all_themes[chk_value]
                    print(f'\n***\nChoosed {chk_theme}\n***\n')
                    print("Removing previous theme...")
                    sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/gtk.css'])
                    sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/gtk-dark.css'])
                    sp.run(["rm", f'{home_dir}{config_dir}/gtk-4.0/assets'])
                    sp.run(["rm", f'{home_dir}{config_dir}/assets'])
                    print("Installing new theme...")
                    sp.run(["ln", "-s", f'{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/gtk.css', f'{home_dir}{config_dir}/gtk-4.0/gtk.css'])
                    sp.run(["ln", "-s", f'{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/gtk-dark.css', f'{home_dir}{config_dir}/gtk-4.0/gtk-dark.css'])
                    sp.run(["ln", "-s", f'{home_dir}{themes_dir}/{chk_theme}/gtk-4.0/assets', f'{home_dir}{config_dir}/gtk-4.0/assets'])
                    sp.run(["ln", "-s", f'{home_dir}{themes_dir}/{chk_theme}/assets', f'{home_dir}{config_dir}/assets'])
                    print("Done.")
    except ValueError as e:
        print("Incorrect value! Please try again!")