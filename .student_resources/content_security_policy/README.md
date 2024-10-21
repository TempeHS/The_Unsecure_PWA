# Content Security Policy

Content Security Policy (CSP) can significantly reduce the risk and impact of cross-site scripting attacks in modern browsers. A CSP has been a W3C recommendation since 2016 and is now the industry standard in securing web applications.

More information on CSP: [w3c documentation](http://www.w3.org/TR/CSP2/)

## To add a Content Security Policy header to your Flask application

### Installation
Install the extension using pip or easy_install. [Pypi Link](https://pypi.python.org/pypi/flask-csp)

```bash
$ pip install flask-csp
```

## Usage
Add the csp_header(...) decorator after the app.route(...) decorator to create a csp header on each route. The decorator can either be passed no value (Add default policies) or custom values by a dict (Add custom policies). For more information on the default policies, see "Change Default Policies" below.

### Add default header
```python
    @app.route('/', methods=['POST', 'GET'])
    @app.route('/index.html', methods=['GET'])
    @csp_header({
    "default-src": "'self'",
    "script-src": "'self'",
    "img-src": "http: https: data:",
    "object-src": "'self'",
    "style-src": "'self'",
    "media-src": "'self'",
    "child-src": "'self'",
    "connect-src": "'self'",
    "base-uri": "",
    "report-uri": "/csp_report",
    "frame-ancestors": 'none'
    })
    def index():
        #index implementation
```

### Create an app route for CSP reports

```python
    @app.route('/csp_report',methods=['POST'])
    def csp_report():
        with open('csp_reports', "a") as fh:
            fh.write(request.data.decode()+"\n")
        return 'done'
```
