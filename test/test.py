if __name__ == '__main__':
<<<<<<< HEAD
    import mainlib as ml
    import items.channel as channel
    import items.video as video
=======
    import Yfetch.mainlib as ml
    import Yfetch.items.channel as channel
    import Yfetch.items.video as video
>>>>>>> e802eb5c26bad80aef0086b007cf54a9252bcbe8

    video_id = 'BvpAeRGnkJ4'
    channel_id = 'UCnYMOamNKLGVlJgRUbamveA'
    channel_link = ['https://www.youtube.com/user/chemssouvideo',
                    'https://www.youtube.com/channel/UCnoN3upJZ1DPFgX9Y0CA8SA']
    video_link = 'https://www.youtube.com/watch?v=6zge0N962aw'

<<<<<<< HEAD
=======

>>>>>>> e802eb5c26bad80aef0086b007cf54a9252bcbe8
    print('\n\n** test the IDs extraction **')

    # test the IDs extraction
    print(ml.extractChannelId(channel_link[0]))
    print(ml.extractChannelId(channel_link[1]))
    print(ml.extractVideoId(video_link))

    print('\n\n** test the creation of data for a video and a channel **')

    # test the creation of data for a video and a channel
<<<<<<< HEAD
    ml.makeChannel(True, channel_id)  # for channel
    ml.makeVideo(video_id)  # for video
=======
    ml.makeChannel(True, channel_id) # for channel
    ml.makeVideo(video_id) #for video
>>>>>>> e802eb5c26bad80aef0086b007cf54a9252bcbe8

    print('\n\n** test the load of the data from the files **')

    # test the load of the data from the files
<<<<<<< HEAD
    print(video.videoAllData(video_id))  # load the video data
    print(channel.channelAllData(channel_id))  # channel the video data
=======
    print(video.videoAllData(video_id)) # load the video data
    print(channel.channelAllData(channel_id))  # channel the video data
>>>>>>> e802eb5c26bad80aef0086b007cf54a9252bcbe8
