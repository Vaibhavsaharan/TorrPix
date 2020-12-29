# TorrPix
A torrent streaming application that streams torrent directly to vlc media player.

## Screenshots
![TorrPix ss](https://github.com/Vaibhavsaharan/TorrPix/blob/main/source/TorrPix.png)

## Prerequisites
TorrPix uses Webtorrent-CLI to stream to vlc.
It can be installed using npm

### Linux
Please make sure you have python3 installed on your unix machine.
```
pip install -r requirements.txt
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
sudo npm install webtorrent-cli -g
```
### Windows
- Install python3.9 from windows store
- Install nodejs from [here](https://nodejs.org/en/download/)
- Install git from [here](https://git-scm.com/downloads)
- Install webtorrent-cli in command promt by typing
```
npm install webtorrent-cli -g
```


## Streaming Your movie

```
python3 torrpix.py

