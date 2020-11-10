# TwitterSelenium

It's a selenium based twitter client that you can post tweets with.  
It's aimed for bot accounts without API keys.  
If all you want to do is to post stuff, then this is the right tool for you.  
I hope to improve it as the time goes on, it works in a very basic way as of right now.

# Usage
```py
# Create an instance
client = TwitterClient()

# Login with your username and password
client.login('twitter_username', 'twitter_password')

# Post a tweet without media
client.tweet(text = 'Hi! This tweet is sent from an API-less client.')

# Post a tweet with media
# You can post up to 4 pictures
client.tweet(text = 'some dank memes', media = ['~/pic1.jpg', '~/pic2.png'])

# More examples
client.tweet(media = ['~/some.gif''])
client.tweet(media = ['~/some_video.mp4'])

# You can close the client once you make sure that the upload is done
time.sleep(5)
client.quit()
```
