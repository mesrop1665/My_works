import requests
url = 'https://r4---sn-cxxapox-x8oz.googlevideo.com/videoplayback?expire=1581862921&ei=qftIXt_UCdKUyAW967i4Ag&ip=46.70.42.130&id=o-ABTlIcIglsNsa12IZOdAvSEw1YcvQxZ5ep1TtuwrKA9k&itag=22&source=youtube&requiressl=yes&mm=31,29&mn=sn-cxxapox-x8oz,sn-n8v7kn7s&ms=au,rdu&mv=m&mvi=3&pl=21&initcwndbps=458750&vprv=1&mime=video/mp4&ratebypass=yes&dur=398.779&lmt=1581786766319063&mt=1581841257&fvip=4&fexp=23842630&c=WEB&txp=7316222&sparams=expire,ei,ip,id,itag,source,requiressl,vprv,mime,ratebypass,dur,lmt&sig=ALgxI2wwRAIgcaE0WUSmN7Afb8T8UplzCTwuOTqbElKDo3EHHfUVGv8CIBIwDhd02Of75tzVr2PVYe4TAWzF7-l25WvDfZQzhFji&lsparams=mm,mn,ms,mv,mvi,pl,initcwndbps&lsig=AHylml4wRAIgP_n9O7ZR6erTFeQ27gU6ZIDUGi593897ZrtKOFIAU1gCIDMmkFZAIxoGJ4kFqf39_fmIRoD_KX1atGcCbQ3uY5CO'

r = requests.get(url,stream=True)

with open('index.mp4','bw') as t:
    for s in r.iter_content(8192):
        t.write(s)