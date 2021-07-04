import os
from twilio.rest import Client

# Get the twilio client specific values from env
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
TO_WHATSAPP_NUMBER  = os.environ['TO_WHATSAPP_NUMBER']
FROM_WHATSAPP_NUMBER = "+14155238886"

# Get the github event specific values from env
GITHUB_SERVER_URL = os.getenv("GITHUB_SERVER_URL")
REPOSITORY = os.getenv("GITHUB_REPOSITORY")
GITHUB_ACTOR = os.getenv("GITHUB_ACTOR")
GITHUB_EVENT_NAME = os.getenv("GITHUB_EVENT_NAME")
EVENT_NAME = os.getenv("GITHUB_EVENT_NAME")
PR_NUMBER = os.getenv("INPUT_PR_NUMBER")
PR_TITLE=os.getenv("INPUT_PR_TITLE")
PR_BODY=os.getenv("INPUT_PR_BODY")
ISSUE_TITLE  = os.getenv("INPUT_ISSUE_TITLE")
ISSUE_NUMBER = os.getenv('INPUT_ISSUE_NUMBER')
ISSUE_BODY = os.getenv('INPUT_ISSUE_BODY')
REPO_FORK_COUNT = os.getenv('INPUT_REPO_FORK_COUNT')
REPO_WATCH_COUNT = os.getenv('INPUT_REPO_WATCH_COUNT')

repo_url = f"{GITHUB_SERVER_URL}/{REPOSITORY}"
response = f"Hello there, \n"

# Process the event and prepare Whatsapp message payload
media_url_for_avatar = [f"{GITHUB_SERVER_URL}/{GITHUB_ACTOR}.png"]
if GITHUB_EVENT_NAME == "push":
    response += f"There is a new *push* in your repository *{REPOSITORY}* by *{GITHUB_ACTOR}*.\n\n"
    response += f"*Repository URL*: {repo_url}"
elif GITHUB_EVENT_NAME == "pull_request":
    pr_url = f"{repo_url}/pull/{PR_NUMBER}"
    response += f"A new event was triggered for a *Pull Request* in your repository *{REPOSITORY}*.\n\n"
    response += f"*PR Number*: ```#{PR_NUMBER}```\n"
    response += f"*PR Title* : ```{PR_TITLE}```\n"
    response += f"*PR User*  : ```{GITHUB_ACTOR}```\n"
    response += f"*PR Body*  : _{PR_BODY}_\n\n"
    response += f"*Check it out*: {pr_url}\n"
    response += f"*Repository URL*: {repo_url}"
elif GITHUB_EVENT_NAME == "issues":
    issue_url = f"{repo_url}/issues/{ISSUE_NUMBER}"
    response += f"A new event was triggered for an *Issue* in your repository *{REPOSITORY}*.\n\n"
    response += f"*Issue Number*: ```#{ISSUE_NUMBER}```\n"
    response += f"*Issue Title* : ```{ISSUE_TITLE}```\n"
    response += f"*Issue User*  : ```{GITHUB_ACTOR}```\n"
    response += f"*Issue Body*  : _{ISSUE_BODY}_\n\n"
    response += f"*Check it out*: {issue_url}\n"
    response += f"*Repository URL*: {repo_url}"
elif GITHUB_EVENT_NAME == "fork":
    response += f"Your repository *{REPOSITORY}* was forked by *{GITHUB_ACTOR}*.\n"
    response += f"Current fork count: *{REPO_FORK_COUNT}*\n\n"
    response += f"*Repository URL*: {repo_url}"
elif GITHUB_EVENT_NAME == "watch":
    response += f"Your repository *{REPOSITORY}* is now watched by *{GITHUB_ACTOR}*.\n"
    response += f"Current watch count: *{REPO_WATCH_COUNT}*\n\n"
    response += f"*Repository URL*: {repo_url}"
else:
    response += f"A new *{GITHUB_EVENT_NAME}* event was triggered by *{GITHUB_ACTOR}* in your repository *{REPOSITORY}*\n\n"
    response += f"*Repository URL*: {repo_url}"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
                              body='THIS is MY notification from GitHub via Twilio-Jimmmy the Virgin Slayer',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:'+os.environ['TO_WHATSAPP_NUMBER']
                          )

print("Message ID:",message.sid)
