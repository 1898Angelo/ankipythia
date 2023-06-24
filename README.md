<p align="center">
  <img src="https://i.imgur.com/ZHrVy1k.png">
</p>

# ANKIPYTHIA
Barebones flashcard app built on Tkinter and inspired by the official Anki app - https://apps.ankiweb.net/

- Create decks and add cards!
- Lightweight (The windows executable is only 8Mb!).
- Cross-platform (Any OS that can run Python 3).
- SQLite is used as the database to store decks and cards locally.

![Animation](https://github.com/1898Angelo/ankipythia/assets/123282394/a594b86a-a496-49e3-9dce-532fc7d5909f)


## DEPENDENCIES
```
customtkinter>=5.1.3
platformdirs>=2.6.2
```

- SQLite binaries are necessary to run the program. They are already included within the repository, but you can download them yourself from:
>https://www.sqlite.org/download.html

- On Linux, you might have to download Tkinter library packages separately.
>https://tecadmin.net/how-to-install-python-tkinter-on-linux/

## HOW TO
### ... RUN IT ON WINDOWS
Download the executable from the releases section and run it! or if you prefer to run it from the source code, follow the steps below.

### ... RUN IT ON OTHER OPERATING SYSTEMS 
After installing the Python dependencies and SQLite binaries, clone or download the repository as a zip file; from the terminal, move into the directory and execute main.py.
```
(if cloning repo with git) git clone https://github.com/1898Angelo/ankipythia.git
cd ankipythia
main.py
```
### ... INSTALL PYTHON DEPENDENCIES
From the terminal set the cwd to the directory where you downloaded (cloned) the repo and run:
```
pip install -r requirements.txt
```
### ... DELETE DATABASE
Your decks and their respective cards are stored within the current user's data directory:
- On windows
```
C:\Users\YourUserName\AppData\Local\Ankipythia
```
- On MacOS
```
/Users/YourUserName/Library/Application Support/Ankipythia
```
- On Linux
```
/home/YourUserName/.local/share/Ankipythia
```
