# discord-loggarr
A shitty docker app to centralize logging for my home lab to a discord server using webhooks, 
optionally combined with user requests applications like overseerr to provide status on downloads


## how to run the development build
note: if you dont have the `docker-compose.yml`, `.env` or `my-discord-loggarr.xml` files youll 
have to create them

### using using docker / docker-compose
1. Copy `docker-compose.example.yml` to your `docker-compose.yml`
2. Edit `docker-compose.yml` and set your `HOST_PORT` to a port available on your system 
    note: only needed if your webhooks are not coming from the same docker network as this container
3. Copy `.env.example` to `.env` and fill in your Discord token/channel
4. Run: `docker-compose up` or whatever method you use to run your containers

### using unraid 
if you wish to use the unraids built in ui and handling (like pulling updates) you can manually add
the example xml template to your /boot/config/plugins/dockerMan/template-user/ folder
1. copy `my-discord-loggarr.example.xml` to your `my-discord-loggarr.xml`
2. move `my-discord-loggarr.xml` to `/boot/config/plugins/dockerMan/template-user/`
3. in the docker tab on unraid, click "add container"
4. the discord-loggar template should show up in the template dropdown, select it
5. fill in the required values
and just like that its running just like any other unraid docker container :3