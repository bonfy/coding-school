# Slack App 开发


## 入门文档

* [https://api.slack.com/](API门户)
* [Step1: Hello World Incoming Webhook](https://api.slack.com/tutorials/slack-apps-hello-world)
* [Step2: Messages](https://api.slack.com/docs/messages)


## Step1

```
curl -X POST \
-H 'Content-type: application/json' \
--data '{"text": "This is posted to #general and comes from *monkey-bot*.", "channel": "#test", "link_names": 1, "username": "monkey-bot", "icon_emoji": ":monkey_face:", {
    "attachments": [
        {
            "fallback": "New ticket from Andrea Lee - Ticket #1943: Can't reset my password - https://groove.hq/path/to/ticket/1943",
            "pretext": "New ticket from Andrea Lee",
            "title": "Ticket #1943: Can't reset my password",
            "title_link": "https://groove.hq/path/to/ticket/1943",
            "text": "Help! I tried to reset my password but nothing happened!",
            "color": "#7CD197"
        }
    ]
}}' \
https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX

```

## Step2 Message

还可以访问 [MessageBuilder](https://api.slack.com/docs/messages/builder) 预览