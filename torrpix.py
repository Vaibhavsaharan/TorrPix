import requests
import subprocess,sys

def main():
    movie_name = input("\nEnter the movie name : ")
    print(f"\nSearching for {movie_name} ....")
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
    torrent_results = requests.get(base_url).json()
    index = 1
    magnet= []
    #print(torrent_results)
    for result in torrent_results:
        if 'movie' in result['type'].lower():
            print(index,") (",result['size'],") ",result['name'], "| seeds : ",result['seeder'], " leechers : ",result['leecher'])
            index+=1
            magnet.append(result['magnet'])

    choice = int(input("\nChoose your input\nSR No. : To stream movie\n   0   : Input another movie\n  -1   : Exit TorrPix\n"))
    if choice == 0:
    	main()
    elif choice == -1:
    	quit()
    magnet_link = magnet[choice-1]
 
    webtorrent_stream(magnet_link)



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
