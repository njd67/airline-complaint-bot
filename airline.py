from urllib.parse import quote_plus

import praw
from textblob import TextBlob 

airlines = ["frontier", "alaska", "allegiant","american",
"delta","hawaiian","jetblue","spirit","united",
"spirit"]

airline_terms = ["airline","flight","delayed","canceled","airlines","air","airplane","airport","bag fees"]


def main():
    reddit = praw.Reddit('bot')
    subreddit = reddit.subreddit("AirlineBotTesting")
    for comment in subreddit.stream.comments():
        process_comments(comment)


def process_comments(comment):
    airline_complaint = ''
    lower_body = comment.body.lower()
    for airline in airlines:
        if airline in lower_body:
            airline_complaint = airline
    if airline_complaint == '':
        return
    airline_term = False
    for airline in airline_terms:
        if airline in lower_body:
            airline_term = True
            break
    if not airline_term:
        return
    analysis = TextBlob(comment.body) 
    
    if analysis.sentiment.polarity < -0.1:
        comment.reply("Replying to: {}".format(submission.title))

    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print("Replying to: {}".format(submission.title))
            submission.reply(reply_text)
            # A reply has been made so do not attempt to match other phrases.
            break


if __name__ == "__main__":
    main()