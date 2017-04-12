from time import time

from download import setup_download_dir, get_links, download_link

CLIENT_ID = 'f777f3cc4b04fe6'

def main():
   ts = time()
   download_dir = setup_download_dir()
   links = [l for l in get_links(CLIENT_ID)]
   for link in links:
       #print('downloading ', link, '...')
       download_link(download_dir, link)
   print('Took {}s'.format(time() - ts))

if __name__ == '__main__':
   main()