import requests
from os import path
import os
import certifi
from cairosvg import svg2png


def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True, verify=False)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def main():
  print("Download undowloadable files from Daan")
  base_url = input("Enter base url: ")
  book_name = input("Enter book name: ")
  if not path.isdir('./output/'):
    os.mkdir('./output/')
  dir_path = './output/' + book_name

  if not path.isdir(dir_path):
    os.mkdir(dir_path)

  i = 1
  while is_downloadable(base_url + str(i)):
    i += 1
    url = base_url + str(i)
    img = requests.get(base_url + str(i), verify=False)
    file_path = dir_path + '/page-%d.jpg' % i
    svg2png(bytestring=img.content, write_to=file_path)
  
  print('Pages downloaded successfully !')

  
main() 
