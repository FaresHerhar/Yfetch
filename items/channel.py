import requests

from Yfetch.config import *
import Yfetch.managedata as md


def getChannelForUserName(user_name):
	'''
	this function for getting the basic data about achannel by
	its owner'r name.
	data:
		*	statistics.
		* 	basic data(name, id, ....)

	the output is a string.
	'''
	URL = CHANNEL_DATA_USER.format(user_name, API_KEY)
	html = requests.get(URL)

	return html.text


def getChannelById(channel_id):
	'''
	this function for getting the basic data about achannel by
	the channel's id.
	data:
		*	statistics.
		* 	basic data(name, id, ....)

	the output is a string.
	'''
	URL = CHANNEL_DATA_ID.format(channel_id, API_KEY)
	html = requests.get(URL)

	return html.text


def channelStatsData(channel_id):
	'''
	extract the neccesary data about the cannel nedded in our statistics
	the out put is the following:
	a dictionary of this form ::

	{'videoCount': '190', 'subscriberCount': '2096091', 'viewCount': '204096646'}
	'''

	# load the data from the storage location, look for DATA_PATH in config.py
	data = md.loadData(CHANNEL_PATH + channel_id + '.json')
	
	# get statistics data and delete the ungonna used ones
	dic = data['items'][0]['statistics']
	dic.pop('commentCount')
	dic.pop('hiddenSubscriberCount')

	return dic


def channelBasicData(channel_id):
	'''
	extract the basic data about the cannel nedded just to identify
	the out put is the following:
	a dictionary of this form ::

	{'createdAt': '2011-09-20T13:33:46.000Z', 'channelTitle': 'Anes Tina',
	'country': 'DZ', 'channelId': 'UCHCsGx9byqxSw6f1JQVBk6Q',
	 'pic' : 'the url, with a size of 240x240'}
	'''

	# load the data from the storage location, look for DATA_PATH in config.py
	data = md.loadData(CHANNEL_PATH + channel_id + '.json')
		
	dic = {}

	# get the channel id and title
	dic['channelId'] = data['items'][0]['id']
	dic['channelTitle'] = data['items'][0]['snippet']['title']
	dic['createdAt'] = data['items'][0]['snippet']['publishedAt']
	dic['pic'] = data['items'][0]['snippet']['thumbnails']['medium']['url']

	# the country is not always provided
	try:
		dic['country'] = data['items'][0]['snippet']['country']
	except:
		dic['country'] = ''

	return dic


def channelAllData(channel_id):
	'''
	this one is a combinations of both channelBasicData() and channelStatsData()
	it returns all the data about he channel.
	with this following format:

	{'statistics': {'viewCount': '204096646', 'subscriberCount': '2096091',
	 'videoCount': '190'}, 'basic': {'pic': 'https://yt3.ggpht.com/a-/AAuE7mBMNlex
	 3hbyn_a7qGuYDLvT7jsq2Mkh-6Ul6Q=s240-mo-c-c0xffffffff-rj-k-no',
	 'channelId': 'UCHCsGx9byqxSw6f1JQVBk6Q', 'channelTitle': 'Anes Tina',
	 'country': 'DZ', 'createdAt': '2011-09-20T13:33:46.000Z'}}

	'''

	# load the data from the storage location, look for DATA_PATH in config.py
	data = md.loadData(CHANNEL_PATH + channel_id + '.json')
		
	dic = {}
	dic['basic'] = {}


	# get statistics data and delete the ungonna used ones
	dic['statistics'] = data['items'][0]['statistics']
	dic['statistics'].pop('commentCount')
	dic['statistics'].pop('hiddenSubscriberCount')



	# get the channel id and title
	dic['basic']['channelId'] = data['items'][0]['id']
	dic['basic']['channelTitle'] = data['items'][0]['snippet']['title']
	dic['basic']['createdAt'] = data['items'][0]['snippet']['publishedAt']
	dic['basic']['pic'] = data['items'][0]['snippet']['thumbnails']['medium']['url']

	# the country is not always provided
	try:
		dic['basic']['country'] = data['items'][0]['snippet']['country']
	except:
		dic['basic']['country'] = ''

	return dic