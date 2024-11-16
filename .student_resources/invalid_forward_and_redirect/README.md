# Invalid Forward and Redirect

Invalid (or unvalidated) forwards and redirects are a form of user controlled input where a web application accepts untrusted input that could cause the web application to redirect. Because the domain name in the modified link is identical to the trusted domain name, phishing attempts may have a more trustworthy appearance.

This vulnerability is often combined with a CSRF, man in the middle or a website spoofing as a more complex threat vector.

```http
https://www.trustedwebsite.com/examples/example.php?url=http://malicious.com
```

| Protocol | subdomain | domain             | path     | endpoint     | parameters               |
| -------- | --------- | ------------------ | -------- | ------------ | ------------------------ |
| https    | www       | trustedwebsite.com | examples | example.html | url=http://malicious.com |

## How to penetrate test for this vulnerability

1. Look for forms collecting URL's that are rendered on the front end, enter a malicious URL and see if validates and renders.
2. Look for frontend URL, path or endpoint parameter passing and construct a URL to an untrusted domain and test if the site will redirect.

## How to countermeasure this vulnerability

1. Code review
2. Explicitly declare URL in the backend code and do not allow URLS to be manipulated by input.
3. Validate inputs, if a form requires URL's use regular expressions to explicitly define the URL specifications (HTTPS, subdomains, domains, paths and endpoints were possible) and exclusions ( >, <, ?, etc). This is particularly important if the input will be rendered on the front end or processed in the backend.
4. Update backend languages (early versions of asp.net are vulnerable)