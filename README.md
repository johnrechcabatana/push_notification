## Push Notification via PushBullet
Description:
Push notification will help the users to get updated even they have not login yet to the website.
This app will notify the user that has a pushbullet in the extension browser about the saved, submitted, or cancelled document of every user.
## Example output

![image](https://github.com/johnrechcabatana/push_notification/assets/54884098/9f996535-8fb9-4275-bf71-fb1b171be29a)


## Installation (ERPNext)
1. pip install pushbullet.py
2. bench get-app https://github.com/johnrechcabatana/push_notification.git
3. bench --site install-app push_notification

## Setup PushBullet
1. goto PushBUllet
2. Fill up all fields
3. check the enable
4. list all document to be included in the notification see example image below

## Example
![image](https://github.com/johnrechcabatana/push_notification/assets/54884098/786706fa-cfde-4eda-b988-ea1f96a5d738)


## Add PushBullet addon extension Firefox/Chrome
FireFox
https://addons.mozilla.org/en-US/firefox/addon/pushbullet/
Chrome
https://chrome.google.com/webstore/detail/pushbullet/chlffgpmiacpedhhbkiomidkjlcfhogd?utm_source=ext_app_menu

Signup and get the access token here https://www.pushbullet.com/#settings/account

## NOTE
To apply this notification for every users.
Every user needs to install/addon PushBullet for their desire browser and login in the same account in where generated the accesstoken

https://youtu.be/Co4uuGzc_fs
#### License

MIT
