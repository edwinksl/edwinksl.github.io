Title: Set up website with Pelican, Google Domains and Netlify
Date: 2017-06-19
Tags: pelican, google domains, netlify, custom domains

### Prelude

The GitHub repository, or repo for short, for this website is located at <https://github.com/edwinksl/edwinksl.github.io>. Issues, pull requests, comments and suggestions are welcome!

### Introduction

This website is set up using [Pelican](https://blog.getpelican.com/) as the [static site generator](https://www.staticgen.com/), [Google Domains](https://domains.google/) for registering a custom domain and [Netlify](https://www.netlify.com/) for hosting the website. The choice of a static site generator is arbitrary and I picked Pelican because it is written in Python and is the most active among various Python static site generators that I am aware of. The main motivation for using Netlify instead of GitHub Pages is because GitHub Pages does not support SSL for custom domains. See this epic [GitHub issue](https://github.com/isaacs/github/issues/156) for complaints and workarounds regarding this problem.

This post seeks to summarize the steps for setting up a website using Pelican, Google Domains and Netlify, and is based on the following excellent documentation, guides and tutorials:

1. Pelican's [documentation](http://docs.getpelican.com/en/stable/)
2. Netlify's guides for [hosting a Pelican website on Netlify](https://www.netlify.com/blog/2015/10/15/a-step-by-step-guide-pelican-on-netlify/) and [setting up a custom domain](https://www.netlify.com/blog/2016/03/14/setting-up-your-custom-domain/)
3. Netlify's documentation for [continuous deployment](https://www.netlify.com/docs/continuous-deployment/) and [enabling HTTPS](https://www.netlify.com/docs/ssl/)

The instructions are given for Ubuntu, specifically Ubuntu 17.04, but they should generalize well to other Linux distributions and operating systems.

### Custom domain

1. Register for a custom domain. I registered mine at Google Domains, so the instructions for this post are based on that. The procedures for setting up a custom domain with Netlify are slightly different for different domain name registrars, which we will discuss later.

### Pelican

1. We will use a [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments), which is commonly abbreviated as virtualenv, to manage the Python dependencies. Therefore, we first install `virtualenv`:

        sudo apt update
        sudo apt install virtualenv

2. Create and activate a virtualenv in the Git repo for the website. My Git repo is located at `~/git/edwinksl.github.io/`, so the commands are:

        cd ~/git/edwinksl.github.io/
        virtualenv venv -p python3.6  # create a virtualenv for Python 3.6
        source venv/bin/activate

    If you prefer Python 3.5, change `python3.6` to `python3`. If you prefer Python 2.7, omit `-p python3.6` and run just `virtualenv venv`. Remember to add `venv/` to `.gitignore` as we are not interested in keeping it under version control. The `pip` that is shipped with Ubuntu can be [buggy](https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1579181), so I usually [force-upgrade `pip`](https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1579181/comments/3) right after activating a new virtualenv as follows:

        pip install -U --force-reinstall pip

3. Use `pip` to install `pelican` and other optional packages, namely `Markdown` and `typogrify`:

        pip install pelican Markdown typogrify

4. Follow either the [quickstart tutorial](http://docs.getpelican.com/en/stable/quickstart.html) or the [detailed documentation](http://docs.getpelican.com/en/stable/) to set up Pelican and write content. The basic workflow consists of running `make devserver` to serve the website locally at <http://localhost:8000/>, iterate content writing and finally running `make stopserver` to stop the development server.


5. In the root of the Git repo, add a file named `CNAME` that contains the custom domain. In my case, `CNAME` contains `www.edwinksl.com`.

6. Ensure that `CNAME` is copied to the root of the `output` directory by adding the following lines to `pelicanconf.py`:

        STATIC_PATHS = ['../CNAME']
        EXTRA_PATH_METADATA = {'../CNAME': {'path': 'CNAME'}}

7. If you are not using themes and plugins, please skip this step. If you are using themes and plugins, please visit <http://docs.getpelican.com/en/stable/settings.html#themes> and <http://docs.getpelican.com/en/stable/plugins.html#plugins> respectively for how to specify them in `pelicanconf.py`. For Netlify to build and deploy the website, all the themes and plugins used need to reside in the Git repo. Because the Git repos for [themes](https://github.com/getpelican/pelican-themes) and [plugins](https://github.com/getpelican/pelican-plugins) exist outside the website Git repo, we have to include them in our website Git repo using either Git subtrees or submodules. You can google "git subtree vs submodules" for various opinions on which to use, but I personally prefer subtrees, so that is what we will use here. A quick tutorial for using subtrees can be found at <https://www.atlassian.com/blog/git/alternatives-to-git-submodule-git-subtree>. We first fork the `pelican-themes` and `pelican-plugins` GitHub repos and add remotes for them. We then use the `git subtree add -P` command to add the directories for themes and plugins. The commands required are:

        git remote add pelican-themes https://github.com/edwinksl/pelican-themes.git
        git remote add pelican-plugins https://github.com/edwinksl/pelican-plugins.git
        git subtree add -P pelican-themes pelican-themes master --squash
        git subtree add -P pelican-plugins pelican-plugins master --squash

    Lastly, we update `.gitignore` to only put the used themes and plugins under version control. In my case, I use the `pelican-bootstrap3` theme and `render_math` and `i18n_subsites` plugins, therefore the lines to be added to `.gitignore` are:

        pelican-themes/*
        !pelican-themes/pelican-bootstrap3/

        pelican-plugins/*
        !pelican-plugins/render_math/
        !pelican-plugins/i18n_subsites/

    To update the themes and plugins, we do `git subtree pull -P` as follows:

        git subtree pull -P pelican-themes pelican-themes master --squash
        git subtree pull -P pelican-plugins pelican-plugins master --squash

8. Netlify requires `requirements.txt` for building the website, which can be generated by running:

        pip freeze > requirements.txt

    If you notice that `requirements.txt` contains `pkg-resources==0.0.0`, which is a [bug](https://askubuntu.com/q/854249/15003), then run the following [command](https://askubuntu.com/a/854254/15003) instead:

        pip freeze | grep -v "pkg-resources" > requirements.txt

9. By default, Netlify uses [Python 2.7.4](https://www.netlify.com/docs/continuous-deployment/#set-node-ruby-or-python-version) to build the website. We instead want to use the latest version of Python 3 that is available in Netlify, which is 3.5.2. To do so, we add a file named `runtime.txt` that contains `3.5.2`.

10. Finally, we can run `tree -a -L 1` to see how the structure of the root directory looks like. In my case, it looks like:

        .
        ├── CNAME
        ├── content
        ├── develop_server.sh
        ├── fabfile.py
        ├── .git
        ├── .gitignore
        ├── LICENSE.md
        ├── Makefile
        ├── node_modules
        ├── output
        ├── package-lock.json
        ├── pelicanconf.py
        ├── pelican.pid
        ├── pelican-plugins
        ├── pelican-themes
        ├── publishconf.py
        ├── __pycache__
        ├── README.md
        ├── .remarkrc -> /home/edwinksl/.remarkrc
        ├── requirements.txt
        ├── runtime.txt
        ├── srv.pid
        └── venv

    You will notice that there are several files and directories that we have not talked about, but they are beyond the scope of this post.

### Netlify

1. Visit [Netlify](https://www.netlify.com/) and follow the instructions at <https://www.netlify.com/blog/2015/10/15/a-step-by-step-guide-pelican-on-netlify/> from the section "Connecting to Netlify" onwards; the sections that come before this have been already been covered in greater detail in this post. The only modification I have made to these instructions is to use `make publish` instead of `pelican content` as the build command so that the settings in `publishconf.py` are taken into account.
2. Follow the instructions at <https://www.netlify.com/blog/2016/03/14/setting-up-your-custom-domain/> to connect Netlify with the custom domain. For instructions specific to Google Domains, see <https://www.netlify.com/blog/2016/03/14/setting-up-your-custom-domain/#googledomains>. Note that the correct IPv4 address to use is `104.198.14.52`, which unfortunately is contradicted by what is shown in the erroneous screenshots. Here is a screenshot of my custom resource records in Google Domains:

    ![Custom resource records]({filename}/images/custom_resource_records.png)

3. Turn on SSL for the website by following the instructions at <https://www.netlify.com/docs/ssl/>. After you have verified that SSL works, I suggest turning on "Force TLS connections", which ["will both set a redirect from http to https, and add `Strict Transport Security` headers to all requests"](https://www.netlify.com/docs/ssl/#forcing-ssl).

### Bells and whistles

1. Visit [Qualys SSL Server Test](https://www.ssllabs.com/ssltest/) to analyze how well SSL is configured on the website. We should expect to see an overall rating of A+.
2. Set up [Google Analytics](https://analytics.google.com/). For the `pelican-bootstrap3` theme, add the tracking ID and turn on [automatic cookie domain configuration](https://developers.google.com/analytics/devguides/collection/analyticsjs/cookies-user-id#automatic_cookie_domain_configuration) by adding the following lines to `publishconf.py`:

        GOOGLE_ANALYTICS_UNIVERSAL = 'UA-100873462-1'  # use your own tracking ID here
        GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto'

3. Connect [Google Search Console](https://www.google.com/webmasters/tools/) to Google Analytics and [set the preferred domain](https://support.google.com/webmasters/answer/44231), which is `www.edwinksl.com` in my case.
