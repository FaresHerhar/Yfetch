import requests
import json

from Yfetch.config import *
import Yfetch.managedata as md


def getVideoById(video_id):
	'''
	this function for getting the basic data about a video by
	the video's id.
	data:
		*	statistics.
		* 	basic data(name, id, ....)
	'''
	URL = Video_DATA_ID.format(video_id, API_KEY)
	html = requests.get(URL)

	return html.text


def videoStatsData(video_id):
	'''
	extract the neccesary data about the video nedded in our statistics
	the out put is the following:
	a dictionary of this form ::

	{'dislikeCount': '190', 'likeCount': '2096091', 'viewCount': '204096646'}
	'''

	# load the data from the storage location, look for DATA_PATH in config.py
	data = md.loadData(VIDEO_PATH + video_id + '.json')

	return data['items'][0]['statistics']


def videoBasicData(video_id):
	'''
	extract the basic data about the video nedded just to identify
	the out put is the following:
	a dictionary of this form ::

	{'videoTitle': 'Les femmes EN Algérie . Anes Tina . المرأة في الجزائر',
	'videoId': 'hkX1Q4nZJHw', 'createdAt': '2016-03-07T17:55:50.000Z'}
	'''

	# load the data from the storage location, look for DATA_PATH in config.py
	data = md.loadData(VIDEO_PATH + video_id + '.json')
	
	dic = {}

	# get the video id and title
	dic['videoId'] = data['items'][0]['id']
	dic['videoTitle'] = data['items'][0]['snippet']['title']
	dic['createdAt'] = data['items'][0]['snippet']['publishedAt']
	dic['channelId'] = data['items'][0]['snippet']['channelId']
	dic['channelTitle'] = data['items'][0]['snippet']['channelTitle']


	return dic


def videoAllData(video_id):
	'''
	this one is a combinations of both channelBasicData() and channelStatsData()
	it returns all the data about he channel.
	with this following format:

	{'statistics': {'dislikeCount': '5837', 'likeCount': '43726',
	'viewCount': '1997007'}, 'basic': {'videoId': 'hkX1Q4nZJHw',
	'videoTitle': 'Les femmes EN Algérie . Anes Tina . المرأة في الجزائر',
	'createdAt': '2016-03-07T17:55:50.000Z'}}
	'''

	# load the data from the storage location, look for DATA_PATH in config.py
	data = md.loadData(VIDEO_PATH + video_id + '.json')

	dic = {}
	dic['basic'] = {}

	# get the video id and title
	dic['basic']['videoId'] = data['items'][0]['id']
	dic['basic']['videoTitle'] = data['items'][0]['snippet']['title']
	dic['basic']['createdAt'] = data['items'][0]['snippet']['publishedAt']
	dic['basic']['channelId'] = data['items'][0]['snippet']['channelId']
	dic['basic']['channelTitle'] = data['items'][0]['snippet']['channelTitle']

	dic['statistics'] = data['items'][0]['statistics']

	return dic


def getTop10VideoIds(channel_id):
	'''
	to collect the most 10 viewed videos of a channel.
	you can change the number. see config.py

	put in mind the pageToken, because google's api, can only
	hold (50 reselts/page), be carefull. :)

	see exemple.py, to see the out come of this function.
	'''
	# send the request
	URL = CHANNEL_TOP10.format(channel_id, API_KEY)
	html = requests.get(URL)

	for item in json.loads(html.text)['items']:
		yield item['id']['videoId']

