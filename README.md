# ckanext-simplesso

A CKAN extension that enables single sign-on (SSO) on your CKAN site using
simple HTTP headers in the request.


Installation
------------

ckanext-simplesso has been tested against CKAN 2.4.1.

To install, activate your CKAN virtualenv and then do:

    git clone 'https://github.co/jorabra/ckanext-simplesso.git'
    cd ckanext-simple
    pip install -e . (or alternatively equivalent) python setup.py develop 

Then add 'simplesso' to the ckan.plugins line in your CKAN config file, for example:

    ckan.plugins = resource_proxy stats datastore simplesso
    
Also make sure you have `ckan.simplesso.header_parameter` and `ckan.simplesso.email_domain` set correctly in your config file, for example:

    ckan.simplesso.header_parameter = my_header_parameter_name
    ckan.simplesso.email_domain = my_email_domain

Finally, restart your web server.

