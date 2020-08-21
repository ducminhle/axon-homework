import time
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST_NAME='localhost'
PORT=80

class Server(BaseHTTPRequestHandler):
  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  def process_json(self):
    reponse = requests.get('http://therecord.co/feed.json')
    feed = reponse.json()

    names = str(feed["author"]["name"]).split(" and ")

    for name in names:
      for item in feed["items"]:
        for key in list(item.keys()):
          index = feed["items"].index(item)
          feed["items"][index][key] = str(item[key]).replace(name, "")
    
    return json.dumps(feed).encode("utf8")
      
  def do_HEAD(self):
    self._set_headers()

  def do_GET(self):
    self._set_headers()

    self.wfile.write(self.process_json())

if __name__ == "__main__":
  httpd = HTTPServer((HOST_NAME, PORT), Server)
  print(time.asctime(), "Start Server - %s:%s"%(HOST_NAME, PORT))
  httpd.serve_forever()
