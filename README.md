# markdown-image-clipboard
----
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT](https://img.shields.io/github/license/wisehackermonkey/markdown-image-clipboard.svg)](https://github.com/wisehackermonkey/markdown-image-clipboard/blob/master/LICENSE)
<!-- <img src="assets/NNNNNNNNNNNNN" width="400"> -->
<h2 align="center">Add images from a phone to markdown documentation with ease</h2>

<h4 align="center">This app requires you have a pushbullet account</h4>
<!-- 

# Quick start
### __________________
##### __________________________
```bash
``` -->

# Summary
<!-- ### -  *[Quick start](#Quick-start)* -->
<!-- ### -  *[Installation](#Installation)* -->
<!-- ### -  *[For developers](#For-developers)* -->
<!-- ### -  *[Contributors](#Contributors)* -->
### -  *[License](#License)*


<!-- 
# Installation
```bash
``` 
-->

<!-- ----------------- -->
<!-- # Screenshots -->
<!-- - <img src="assets/_____________" width="400">  -->
<!-- -  -->


<!-- SETUP -->

-----------------
# For developers
<!-- ### 
```bash
```  -->
### Dev log
```bash
how to interact with pushbullet api
curl --header 'Access-Token: <your_access_token_here>' \
     https://api.pushbullet.com/v2/users/me

bash
PUSHBULLETAPI="<your_access_token_here>"
curl --header  "Access-Token: ${PUSHBULLETAPI}" https://api.pushbullet.com/v2/users/me

# how to get latest push from user (i want the image from the user)
curl --header  "Access-Token: ${PUSHBULLETAPI}" https://api.pushbullet.com/v2/pushes
``` 
### what data im looking for
```bash
{
    "accounts": [],
    "blocks": [],
    "channels": [],
    "chats": [],
    "clients": [],
    "contacts": [],
    "devices": [],
    "grants": [],
    "pushes": [
        {
            "active": true,
            "iden": "ujwPGnFffbgsjBhE2rsE9c",
            "created": 1613451908.3619251,
            "modified": 1613451909.6910138,
            "type": "file",
            "file_name": "711VBTMInpL._SL1600_.jpg",
            "file_type": "image/jpeg",
            "file_url": "https://dl3.pushbulletusercontent.com/mSnwSJ89SX78Cl9igkkTAyaRXO2Qf1KC/711VBTMInpL._SL1600_.jpg",
            "image_width": 1600,
            "image_height": 1200,
            "image_url": "https://lh3.googleusercontent.com/lYODfrKgRm9nyN0x6hw-SL583g7GnC5aR3Ybx0DmEMgVMa3A0CjC32txRMEQnTjoFHQNjVQG0OHEb1irBUkjtzjCZXT2VItv_WxSwN3V"
        },
    ]
}

pushes[first one ]?.image_url 
```
### how to connect to pushbullet websocket for realtime updates
```bash
$Env:PUSHBULLETAPI="<your_access_token_here>"
python -m websockets wss://stream.pushbullet.com/websocket/$env:PUSHBULLETAPI

python -m websockets wss://stream.pushbullet.com/websocket/$env:PUSHBULLETAPI 
```



# Product definition
- component
    - data
        - url of photo
        - image data
        - date
    - copy to clipboard
    - pull from pushbullet api image url

- Behavor
    - copy photo to clipboard



-----------------
# Contributors

[![](https://contrib.rocks/image?repo=wisehackermonkey/markdown-image-clipboard)](https://github.com/wisehackermonkey/markdown-image-clipboard/graphs/contributors)

##### Made with [contributors-img](https://contrib.rocks).

-----------------
# License
#### MIT © wisehackermonkey
[![MIT](https://img.shields.io/github/license/wisehackermonkey/markdown-image-clipboard.svg)](https://github.com/wisehackermonkey/markdown-image-clipboard/blob/master/LICENSE).

```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
______________________
```

















<!-- ---------------------------------- -->
<!-- FULL -->
<!-- ---------------------------------- -->

<!-- # markdown-image-clipboard -->
----
<!-- 
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT](https://img.shields.io/github/license/wisehackermonkey/markdown-image-clipboard.svg)](https://github.com/wisehackermonkey/markdown-image-clipboard/blob/master/LICENSE)
<img src="assets/NNNNNNNNNNNNN" width="400">
<h2 align="center">____________________</h2>
<h4 align="center">________________________</h4>
 -->

<!-- 

# Quick start
### __________________
##### __________________________
```bash
```

 -->


<!-- 

# Summary
### -  *[Quick start](#Quick-start)*
### -  *[Live Demo](#Live-demo)*
### -  *[Installation](#Installation)*
### -  *[Screenshots](#Screenshots)*
### -  *[License](#License)*
### -  *[Features](#Features)*
### -  *[For developers](#For-developers)*
### -  *[Todo](#TODO)*
### -  *[Related](#Related)*
### -  *[Contributors](#Contributors)*
 -->



-----------------
<!-- <img src="assets/KKKKKKKKKKK" width="400"> -->
<!-- # [Live Demo](https://www._____________.com) -->





<!-- 
# Installation
### 
```bash
``` -->




<!-- 

-----------------
# Screenshots
- <img src="assets/_____________" width="400"> 
- 
 -->



<!-- 

# Features
- [x] ______
- [ ] ______


 -->


<!-- 
-----------------
# For developers
### 
```bash
```
 -->





<!-- -----------------
# TODO
- [x] ___________
- [ ] ___________ -->

<!-- 
-----------------
# Built with
- #### ________________
 -->





<!-- -----------------
# Related 
### [_________](https://www.____________.com)
 -->





<!-- 
-----------------
# Contributors

[![](https://contrib.rocks/image?repo=wisehackermonkey/markdown-image-clipboard)](https://github.com/wisehackermonkey/markdown-image-clipboard/graphs/contributors)

##### Made with [contributors-img](https://contrib.rocks).

-----------------
# License
#### MIT © wisehackermonkey
[![MIT](https://img.shields.io/github/license/wisehackermonkey/markdown-image-clipboard.svg)](https://github.com/wisehackermonkey/markdown-image-clipboard/blob/master/LICENSE)
 -->

```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
______________________
```

<!-- ---------------------------------- -->
<!-- EXTRAS -->
<!-- ----------------------------------- -->
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<!-- 
[![Javascript](https://img.shields.io/badge/Javascript-Enabled-lightgreen.svg)](https://shields.io/) 
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![Python](https://img.shields.io/badge/Python-Enabled-<COLOR>.svg)
![P5.js](https://img.shields.io/badge/P5.js-Enabled-pink.svg)
[![Generic badge](https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.svg)](https://shields.io/)
[![GitHub release](https://img.shields.io/github/release/wisehackermonkey/markdown-image-clipboard.svg)](https://GitHub.com/wisehackermonkey/markdown-image-clipboard/releases/)
[![GitHub tag](https://img.shields.io/github/tag/wisehackermonkey/markdown-image-clipboard.svg)](https://GitHub.com/wisehackermonkey/markdown-image-clipboard/tags/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/wisehackermonkey/markdown-image-clipboard.svg)](https://GitHub.com/wisehackermonkey/markdown-image-clipboard/pull/)
[![Website perso.crans.org](https://img.shields.io/website-up-down-green-red/http/www.orancollins.com.svg)](http://www.orancollins.com/) 
    -->

<!-- 
# https://yuml.me/diagram/plain/activity/draw
### (start)->[AAAAAAAA]<aaaaa->(BBBBBB)->(end) 

# Diagram
## 
```bash
```
 -->

<!-- 

# List
- 
- 
- 



# Toggle List
<details>
<x>____________</x>
<x>____________</x>
<x>____________</x>
</details>

# Keyboard Commnand
### <kbd>Command/ctrl + R</kbd> 

# Installation
### 
```bash
cd ~
git clone https://github.com/wisehackermonkey/markdown-image-clipboard.git
cd markdown-image-clipboard
pip install -r requirements.txt
npm install
```

# Docker
### Build
```bash
cd ~
git clone https://github.com/wisehackermonkey/markdown-image-clipboard.git
cd markdown-image-clipboard
docker build -t wisehackermonkey/markdown-image-clipboard:latest .  
```
### Run
```bash
docker run -it --rm --name wisehackermonkey/markdown-image-clipboard:latest  
```
### Docker-compose
```bash
docker-compose build
docker-compose up 
```



# Publish Docker Image
```bash
docker build -t wisehackermonkey/markdown-image-clipboard:latest .
docker login
docker push wisehackermonkey/markdown-image-clipboard:latest
```

 -->