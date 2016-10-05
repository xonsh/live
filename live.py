import os

from flask import Flask, url_for

app = Flask("xonsh-live")

BASE = """
<!doctype html>
<html>
<head>
  <link rel="stylesheet" href="static/xterm.js/dist/xterm.css" />
  <link rel="stylesheet" href="static/xterm.js/addons/fullscreen/fullscreen.css" />
  <script src="static/xterm.js/dist/xterm.js"></script>
  <script src="static/xterm.js/addons/attach/attach.js"></script>
  <script src="static/xterm.js/addons/fit/fit.js"></script>
  <script src="static/xterm.js/addons/fullscreen/fullscreen.js"></script>
  <script src="static/xterm.js/addons/linkify/linkify.js"></script>

        <style>
            body {
                color: #111;
            }
            #terminal {
                max-width: 900px;
                margin: 0 auto;
            }
            #terminal a {
                color: #fff;
            }
        </style>
</head>
  <body>
    <div id="terminal"></div>
    <script>
      var term = new Terminal();
      term.open(document.getElementById('#terminal'));
      term.fit();
      term.write('Hello from http://google.com \033[1;3;31mxterm.js\033[0m $ ')
      term.linkify();
    </script>
  </body>
</html>
"""

@app.route("/")
def base():
    return BASE

if __name__ == "__main__":
    app.run()