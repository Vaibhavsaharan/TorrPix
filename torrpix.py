import requests
import subprocess,sys

def main():
    print("\n****************************WELCOME TO TORRPIX**************************\nAfter making choice here, press ? to switch between movie and TV section \n")
    choicemain = -1
    while choicemain != 1 and choicemain != 2 :
        try:
            choicemain = int(input("\nType 1 to watch movie or type 2 to watch tv series : "))
        except :
            print("\nPlease type either 1 or 2")
    if choicemain == 1 :
        watchmovie()
    else :
         watchtv()      
 
    

def watchmovie():
    movie_name = input("\nEnter the movie name : ")
    if(movie_name == "?"):
        watchmovie()
    elif (movie_name == "-2"):
        quit()
    print(f"\nSearching for '{movie_name}' ....")
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
    torrent_results = requests.get(base_url).json()
    index = 1
    magnet= []
    #print(torrent_results)
    for result in torrent_results:
        print(result['name'], result['type'])
        if 'movie' in result['type'].lower():
            print(index,") (",result['size'],") ",result['name'], "| seeds : ",result['seeder'], " leechers : ",result['leecher'])
            index+=1
            magnet.append(result['magnet'])

    choice = int(input("\nChoose your input\nSR No. : To stream movie\n   0   : Input another movie\n  -1   : Exit TorrPix\n   ?   : To watch tv series\n"))
    if choice == 0:
        watchmovie()
    elif choice == -1:
        quit()
    elif choice == -2:
        watchtv()
    magnet_link = magnet[choice-1]
    webtorrent_stream(magnet_link)

def watchtv():
    tv_series_name = input("\nEnter the TV series name : ")
    if(tv_series_name == "?"):
        watchmovie()
    elif (tv_series_name == "-2"):
        quit()
    print(f"\nSearching for '{tv_series_name}' ....")
    base_url = f"https://api.sumanjay.cf/torrent/?query={tv_series_name}"
    torrent_results = requests.get(base_url).json()
    index = 1
    magnet= []
    #print(torrent_results)
    for result in torrent_results:
        if 'tv shows' in result['type'].lower():
            print(index,") (",result['size'],") ",result['name'], "| seeds : ",result['seeder'], " leechers : ",result['leecher'])
            index+=1
            magnet.append(result['magnet'])
    if(index != 1):
        choice = int(input("\nChoose your input\nSR No. : To stream tv series\n   0   : Input another tv series\n  -1   : Exit TorrPix\n  ?   : To watch movie\n"))
        if choice == 0:
            watchtv()
        elif choice == -1:
            quit()
        elif choice == -2:
            watchmovie()
        magnet_link = magnet[choice-1] 
        webtorrent_stream(magnet_link)
    else:
        print(f"\nTV series : {tv_series_name} not found ")
        moviecount = 0
        for res in torrent_results:
            if 'movies' in res['type'].lower():
                moviecount+=1
        if(moviecount != 0):
            print(f" but found {moviecount} results in movies section\n")
        else:
            print("\n")
        watchtv()



def webtorrent_stream(magnet_link):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    cmd.append('--vlc')
    
    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd,shell=True)

if __name__ == "__main__":
    main()
