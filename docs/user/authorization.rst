
======================
Authorization
======================

.. note::
  Before you use `HSpotipy`_, you have to set up your web server by yourself.
  After that, your users can access your server and log in to their Spotify account.

All content in this section can be found in `Web API Tutorial - Beginner's Tutorial <https://developer.spotify.com/web-api/tutorial/>`_ .


Step 1 : Create Spotify App
===============================

Please follow `Web API Tutorial`_ to set up your account, register your application,
get your client ID and Secret Key and set up your local website via JaveScript.

Set up Account and Application
---------------------------------
 - Set up your account : `Spotify Developer Website <https://developer.spotify.com/>`_
 - Register your application : `Spotify My Applications`_

After registering your application, you can get and set your:
 - Client ID
 - Client Secret Key
 - Redirect URL , to test locally, set to http://localhost:8888/callback

Try Web Service Environment
---------------------------------

Mac OX Install node.js
^^^^^^^^^^^^^^^^^^^^^^^^

Follow http://blog.teamtreehouse.com/install-node-js-npm-mac or simply enter:

.. code-block:: bash
  brew install node # install
  node -v           # check version
  node xxx.js       # run script

Keep follow `Web API Tutorial`_ and `Spotify Web API Authorization JaveScript Example`_ to set up your
web service environment.


Run OAuth example locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download `OAuth examples <https://github.com/spotify/web-api-auth-examples>`_, the code of the OAuth examples depends on the packages express,request and querystring.
Download and install the dependencies running the following command.

.. code-block:: bash
  git clone https://github.com/spotify/web-api-auth-examples.git
  cd web-api-auth-examples/
  npm install


To run the web example, open ``authorization_code/app.js``, set the Client ID, Client ID and Redirect URL as http://localhost:8888/callback.
.. code-block:: bash
  cd authorization_code
  node app.js

Open http://localhost:8888 , the users can log in or sign up their account, just like how users do in Spotify website.

User can now get the oAuth info
 - Access token
 - Refresh token


Step 2: Python
======================

Open `Spotipy Authorized requests <http://spotipy.readthedocs.io/en/latest/#authorized-requests>`_ .

 - The ``Authorization Code flow`` This method is suitable for long-running applications which the user logs into once. It provides an access token that can be refreshed.
 - The ``Client Credentials flow`` The method makes it possible to authenticate your requests to the Spotify Web API and to obtain a higher rate limit than you would


Previous example just show how to use OAuth on web browser



.. _Spotipy: https://github.com/plamere/spotipy
.. _GitHub: https://github.com/zsdonghao/haospotipy
.. _HSpotipy: https://github.com/zsdonghao/hspotipy/

.. _Web API Tutorial: https://developer.spotify.com/web-api/tutorial/
.. _Web API Authorization Guide: https://developer.spotify.com/web-api/authorization-guide/
.. _Spotify My Applications: https://developer.spotify.com/my-applications
.. _Spotify Developer Authorization Guide: https://developer.spotify.com/web-api/authorization-guide/
.. _Spotify Web API Authorization JaveScript Example: https://github.com/spotify/web-api-auth-examples
