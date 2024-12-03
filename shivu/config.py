class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7053677913"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1002362489227
    TOKEN = "7659917863:AAE1S3Vwwk5P-YkfGXCJKlr5q30uhHP-ymU"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "ShadowAuctionTrade"
    UPDATE_CHAT = "Shadow_auction"
    BOT_USERNAME = "ManhwaGrabberBot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
