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

Then add 'simplesso' to the ckan.plugins line in your CKAN config file, for
example:

    ckan.plugins = resource_proxy stats datastore simplesso
    
Also make sure you have `ckan.simplesso.header_parameter` and
`ckan.simplesso.email_domain` set correctly in your config file, for example:

    ckan.simplesso.header_parameter = my_header_parameter_name
    ckan.simplesso.email_domain = my_email_domain

Finally, restart your web server.


Notes
-----

- CKAN default user management pages lets users change both username and email.
  The plugin uses username to establish if SSO user already has a CKAN account.

- Note that usernames "must be purely lowercase alphanumeric (ascii) characters
  and these symbols: -\_". The plugin handles this only by lowercasing the
  username.


TODO
----

- Handle SSO usernames with all kinds of symbols that CKAN doesn't support.

- Remove all register, login and logout functionality if the use case is to
  only accept SSO users and anonymous users.
