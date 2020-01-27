import items.channel as channel
import items.video as video
import managedata as md
import config as config
import urllib.request
import json


def makeVideo(video_id):
    '''
    to initialise the file that is named after the video id, extracting the data
    of the video and storing it  into a file.
    i store the date for statical reasons and also to avoid  Quota over using.
    True if thing works, else if there is some thing wrong;
    most of the times, there is some thing wrong either with the Video_id, or a dead
    API_KEY.
    '''

    try:
        data = video.getVideoById(video_id)
        md.dumpData(config.VIDEO_PATH + video_id + '.json', data)

        return True

    except :
        return False


def makeChannel(is_id, channel_id):
    '''
    a function to intilise the channel's data, create a file under the id
    of the channel as a name of the file, then store the data about the channel
    into the file called    {channel_id}.json.
    in each file that describes a chanel you will find the previos file as an id
    of the channel.
    '''

    # to determine if it is a id, or the string that defines the owner
    # if yes : get the data.
    # if not : get the data then get the id too.
    if is_id:
        data = channel.getChannelById(channel_id)
        channel_id = channel_id

    else:
        data = channel.getChannelForUserName(channel_id)
        channel_id = json.loads(data)['items'][0]['id']

    # create the id file for the channel.
    md.dumpData(config.CHANNEL_PATH + channel_id + '.json', data)

    return channel_id


def extractChannelId(channel_link):
	'''
	this function is used to extract the channel's id, of the channels owner idf.
	it return using yield as a generator in order to smouth data passing,
	also for memory usage.
	True :: means by channel's id.
	False :: means by channel's owner.

	the out come is in the following format:
		if it is a 'channel':
				return True, 'the channel's ID'

			if it is by 'user':
				return False, 'the user string'

	link = https://www.youtube.com/user/chemssouvideo
	owner_id = chemssouvideo

	link = https://www.youtube.com/channel/UCnoN3upJZ1DPFgX9Y0CA8SA
	channel_id = UCnoN3upJZ1DPFgX9Y0CA8SA

	:param channel_link:
	:return channel_id | owner_id:
	'''
	try:
		# decomposing the link.
		channel_link = channel_link.split('/')

		# identify either is a channels id, or channels owner
		if channel_link[-2] == 'channel':
			return True, channel_link[-1]

		if channel_link[-2] == 'user':
			return False, channel_link[-1]
	# in case an empty line.
	except Exception as e:
		pass


def extractVideoId(video_link):
	'''
	this function is used for extracting the video id from a youtube video_link
	link = https://www.youtube.com/watch?v=6zge0N962aw
	video_id = 6zge0N962aw

	:param video_link:
	:return video_id:
	'''
	try:
		return video_link.split('=')[1]

	# in case an empty line.
	except Exception as e:
		pass


def getChannelImg(channel_id):
	'''
	in the project i am working on, i need the pic of the youtube channel.
	this function rtrieve the image, and stores it into the file that describes
	the channel.
	'''
	# get the link to downdload the image.
	link = channel.channelBasicData(channel_id)['pic']

	# create the image file. 
	open(config.DATA_PATH + '/data' + channel_id + '_' +'pic.jpg', 'w').close()


	try:
		# download the file a store ir into the created file.
		urllib.request.urlretrieve(link, config.DATA_PATH + '/' + channel_id + '/' + 'pic.jpg')
	except Exception as e:
		raise e
