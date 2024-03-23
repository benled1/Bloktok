import reddit_interface


reddit_data = reddit_interface.request_data("https://www.reddit.com/r/AmItheAsshole/comments/1blrz8c/aita_for_sleeping_in_on_my_gfs_birthday/")

print(reddit_interface.get_post_title(reddit_data))
print(reddit_interface.get_post_body(reddit_data))
