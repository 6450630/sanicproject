# -*- coding: utf-8 -*-
from sanicapp.createapp import CreateApp

app = CreateApp()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, access_log=False,debug=True,auto_reload=True)