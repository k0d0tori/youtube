import requests
import concurrent.futures

urls = [
    r'https://images.pexels.com/photos/5331915/pexels-photo-5331915.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    r'https://images.pexels.com/photos/5942618/pexels-photo-5942618.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
    r'https://images.pexels.com/photos/4616839/pexels-photo-4616839.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
    r'https://images.pexels.com/photos/6027878/pexels-photo-6027878.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
    r'https://images.pexels.com/photos/5997877/pexels-photo-5997877.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
    r'https://images.pexels.com/photos/4969985/pexels-photo-4969985.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
    r'https://images.pexels.com/photos/5893103/pexels-photo-5893103.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
    r'https://images.pexels.com/photos/5599758/pexels-photo-5599758.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    r'https://images.pexels.com/photos/5720776/pexels-photo-5720776.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    r'https://images.pexels.com/photos/5493655/pexels-photo-5493655.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
    r'https://images.pexels.com/photos/5491067/pexels-photo-5491067.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
    r'https://images.pexels.com/photos/4906286/pexels-photo-4906286.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
]


def downloads(image):
	i = requests.get(image).content
	name = str(image.split('/')[4]) + '.jpg'
	with open(name, 'wb') as f:
		f.write(i)
		print(f'{name} has been downloaded')


with concurrent.futures.ThreadPoolExecutor() as exec:
	exec.map(downloads, urls)