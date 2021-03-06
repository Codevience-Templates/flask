##
# @file
#   File for Flask application.
#
# @copyright
#   BSD 2-Clause License
#
#   Copyright (c) 2022, Codevience <codevience@gmail.com>
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#   ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#   LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#   LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
#   OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
#   DAMAGE.
#
# @per specification
#   EditorConfig is awesome: https://EditorConfig.org
#
##
from flask import Flask
import yaml

config = dict()
with open("config.yaml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
HOST_IP = config['host']['ip']
HOST_PORT = config['host']['port']

app = Flask(
    import_name=__name__,
    static_url_path=None,
    static_folder='static',
    static_host=None,
    host_matching=False,
    subdomain_matching=False,
    template_folder='templates',
    instance_path=None,
    instance_relative_config=False,
    root_path=None
    )


@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host=HOST_IP, port=HOST_PORT, debug=True, load_dotenv=False)
