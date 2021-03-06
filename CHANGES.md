Changelog for Django on Openshift
===

This Project is a fork of [openshift-django17] by [John Flynn Matthew].
For the license and more details, read the README.md file.

###Version 2.0 - Say Hi to `Django on OpenShift`; a seperate, fun filled fork!
* Adds support to Django 1.8.x LTS
* Introduces a unpluggable demo app.
* Replaces the hardcoded versioning with dynamic versions of the live environment packages.
* Adds bootstrap (3.3.4) via cdn as the default css framework.
* Adds jQuery (1.3.2) via cdn as the default JavaScript library.
* Formats code as per PEP8 recommendations.

###Version 1.3.2 (12/31/2014 - Happy New Year (I need to work on non-holidays too).
* Move where wsgi.py is located, so that HTTP redirection works as published by Red Hat.
* Update README.md to reflect above, and add mention on how to redirect to HTTPS.

###Version 1.3.1 (12/24/2014 - Merry Christmas / Happy New Year)
* update settings.py to account for templates (Fixes #8), thanks to Bill K for this one.
* update README.md to reflect new instructions for above.

###Version 1.3 (11/6/2014)
* update settings.py to allow for either PostgreSQL or MySQL.
* started tagging releases in git.

###Version 1.2 (11/1/2014)
* Allow for static file distribution via /static folder and STATICFILES_DIR directive (thanks to just10minutes).

###Version 1.1
* Fix some Python 3.x compatibility bugs
* Optimize wsgi.py usage, use stock django wsgi.py file instead of manually created one.
* create requirements.txt for local usage, remove django 1.7x out of setup.py.

###Version 1.0
Intial release to github.
* Ready to use for local development.
* Easy to push to Openshift.
* Works with  PostgreSQL.
* Minimal changes to default django 1.7 installation.
* Names follow the django 1.7x tutorial.
* Uses new folder layout from Openshift March 2014 release.
* Allows for debug mode on Openshift with the help of an environment variable.


[openshift-django17]:https://github.com/jfmatth/openshift-django17
[John Flynn Matthew]:https://github.com/jfmatth/