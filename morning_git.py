import json
import requests
import wget
import os

url = 'https://www.instagram.com/explore/tags/morningfromthewild/?__a=1'
r = requests.get(url).content.decode('UTF-8')
l = json.loads(r)
DIR = ''# directory you want to save your pictures in
images_in_dir = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) - 2

number_of_images = l['graphql']['hashtag']['edge_hashtag_to_media']['count']

image_diff = number_of_images - images_in_dir;

#for data in l['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
#    image_url = data['node']['display_url']
#    filename = data['node']['taken_at_timestamp']
#    wget.download(image_url, out='E:\jaipur 2k21\wallpaper')
#    print(image_url)
i = 0

while i < image_diff:
    image_url = l['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['display_url']
    filename = l['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['display_url']
    wget.download(image_url, out=DIR)
    i = i + 1
    print(image_url)
