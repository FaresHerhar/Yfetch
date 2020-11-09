# the api key associated to your account to use
API_KEY = "YOUR API KEY"

#  to extract the data about a channel by user name
CHANNEL_DATA_USER = "https://www.googleapis.com/youtube/v3/channels?part=snippet%2Cstatistics&\
forUsername={}&maxResults=1&key={}"

#  to extract the data about a channel by channel id
CHANNEL_DATA_ID = "https://www.googleapis.com/youtube/v3/channels?part=snippet%2Cstatistics&\
id={}&maxResults=1&key={}"

# to extract the data about a video by video id
VIDEO_DATA_ID = "https://www.googleapis.com/youtube/v3/videos?part=\
snippet%2CcontentDetails%2Cstatistics&id={}&fields=items(id%2Csnippet\
(channelId%2CchannelTitle%2CpublishedAt%2Ctitle)%2Cstatistics\
(dislikeCount%2ClikeCount%2CviewCount))&key={}"

# the channel videos list
CHANNEL_TOP10 = "https://www.googleapis.com/youtube/v3/search?part=snippet&\
channelId={}&maxResults=11&order=viewCount&fields=items%2Fid%2FvideoId&key={}"

# the full path of where the data will be stored in, every thing
DATA_PATH = '/home/fares/youtubeData/'

# the path where the videos data is stored
VIDEO_PATH = DATA_PATH + 'video/'

# the path where the channel data is stored
CHANNEL_PATH = DATA_PATH + 'channel/'
