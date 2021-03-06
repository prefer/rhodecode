.. _changelog:

Changelog
=========


1.3.0 (**XXXX-XX-XX**)
======================

:status: in-progress
:branch: beta

news
----

 
fixes
-----


1.2.2 (**2011-10-17**)
======================

news
----

- #226 repo groups are available by path instead of numerical id
 
fixes
-----

- #259 Groups with the same name but with different parent group
- #260 Put repo in group, then move group to another group -> repo becomes unavailable
- #258 RhodeCode 1.2 assumes egg folder is writable (lockfiles problems)
- #265 ldap save fails sometimes on converting attributes to booleans, 
  added getter and setter into model that will prevent from this on db model level
- fixed problems with timestamps issues #251 and #213
- fixes #266 Rhodecode allows to create repo with the same name and in 
  the same parent as group
- fixes #245 Rescan of the repositories on Windows
- fixes #248 cannot edit repos inside a group on windows
- fixes #219 forking problems on windows

1.2.1 (**2011-10-08**)
======================

news
----


fixes
-----

- fixed problems with basic auth and push problems 
- gui fixes
- fixed logger

1.2.0 (**2011-10-07**)
======================

news
----

- implemented #47 repository groups
- implemented #89 Can setup google analytics code from settings menu
- implemented #91 added nicer looking archive urls with more download options
  like tags, branches
- implemented #44 into file browsing, and added follow branch option
- implemented #84 downloads can be enabled/disabled for each repository
- anonymous repository can be cloned without having to pass default:default
  into clone url
- fixed #90 whoosh indexer can index chooses repositories passed in command 
  line
- extended journal with day aggregates and paging
- implemented #107 source code lines highlight ranges
- implemented #93 customizable changelog on combined revision ranges - 
  equivalent of githubs compare view 
- implemented #108 extended and more powerful LDAP configuration
- implemented #56 users groups
- major code rewrites optimized codes for speed and memory usage
- raw and diff downloads are now in git format
- setup command checks for write access to given path
- fixed many issues with international characters and unicode. It uses utf8
  decode with replace to provide less errors even with non utf8 encoded strings
- #125 added API KEY access to feeds
- #109 Repository can be created from external Mercurial link (aka. remote 
  repository, and manually updated (via pull) from admin panel
- beta git support - push/pull server + basic view for git repos
- added followers page and forks page
- server side file creation (with binary file upload interface) 
  and edition with commits powered by codemirror 
- #111 file browser file finder, quick lookup files on whole file tree 
- added quick login sliding menu into main page
- changelog uses lazy loading of affected files details, in some scenarios 
  this can improve speed of changelog page dramatically especially for 
  larger repositories.
- implements #214 added support for downloading subrepos in download menu.
- Added basic API for direct operations on rhodecode via JSON
- Implemented advanced hook management

fixes
-----

- fixed file browser bug, when switching into given form revision the url was 
  not changing
- fixed propagation to error controller on simplehg and simplegit middlewares
- fixed error when trying to make a download on empty repository
- fixed problem with '[' chars in commit messages in journal
- fixed #99 Unicode errors, on file node paths with non utf-8 characters
- journal fork fixes
- removed issue with space inside renamed repository after deletion
- fixed strange issue on formencode imports
- fixed #126 Deleting repository on Windows, rename used incompatible chars. 
- #150 fixes for errors on repositories mapped in db but corrupted in 
  filesystem
- fixed problem with ascendant characters in realm #181
- fixed problem with sqlite file based database connection pool
- whoosh indexer and code stats share the same dynamic extensions map
- fixes #188 - relationship delete of repo_to_perm entry on user removal
- fixes issue #189 Trending source files shows "show more" when no more exist
- fixes issue #197 Relative paths for pidlocks
- fixes issue #198 password will require only 3 chars now for login form
- fixes issue #199 wrong redirection for non admin users after creating a repository
- fixes issues #202, bad db constraint made impossible to attach same group 
  more than one time. Affects only mysql/postgres
- fixes #218 os.kill patch for windows was missing sig param
- improved rendering of dag (they are not trimmed anymore when number of 
  heads exceeds 5)
    
1.1.8 (**2011-04-12**)
======================

news
----

- improved windows support

fixes
-----

- fixed #140 freeze of python dateutil library, since new version is python2.x
  incompatible
- setup-app will check for write permission in given path
- cleaned up license info issue #149
- fixes for issues #137,#116 and problems with unicode and accented characters.
- fixes crashes on gravatar, when passed in email as unicode
- fixed tooltip flickering problems
- fixed came_from redirection on windows
- fixed logging modules, and sql formatters
- windows fixes for os.kill issue #133
- fixes path splitting for windows issues #148
- fixed issue #143 wrong import on migration to 1.1.X
- fixed problems with displaying binary files, thanks to Thomas Waldmann
- removed name from archive files since it's breaking ui for long repo names
- fixed issue with archive headers sent to browser, thanks to Thomas Waldmann
- fixed compatibility for 1024px displays, and larger dpi settings, thanks to 
  Thomas Waldmann
- fixed issue #166 summary pager was skipping 10 revisions on second page


1.1.7 (**2011-03-23**)
======================

news
----

fixes
-----

- fixed (again) #136 installation support for FreeBSD


1.1.6 (**2011-03-21**)
======================

news
----

fixes
-----

- fixed #136 installation support for FreeBSD
- RhodeCode will check for python version during installation

1.1.5 (**2011-03-17**)
======================

news
----

- basic windows support, by exchanging pybcrypt into sha256 for windows only
  highly inspired by idea of mantis406

fixes
-----

- fixed sorting by author in main page
- fixed crashes with diffs on binary files
- fixed #131 problem with boolean values for LDAP
- fixed #122 mysql problems thanks to striker69 
- fixed problem with errors on calling raw/raw_files/annotate functions 
  with unknown revisions
- fixed returned rawfiles attachment names with international character
- cleaned out docs, big thanks to Jason Harris

1.1.4 (**2011-02-19**)
======================

news
----

fixes
-----

- fixed formencode import problem on settings page, that caused server crash
  when that page was accessed as first after server start
- journal fixes
- fixed option to access repository just by entering http://server/<repo_name> 

1.1.3 (**2011-02-16**)
======================

news
----

- implemented #102 allowing the '.' character in username
- added option to access repository just by entering http://server/<repo_name>
- celery task ignores result for better performance

fixes
-----

- fixed ehlo command and non auth mail servers on smtp_lib. Thanks to 
  apollo13 and Johan Walles
- small fixes in journal
- fixed problems with getting setting for celery from .ini files
- registration, password reset and login boxes share the same title as main 
  application now
- fixed #113: to high permissions to fork repository
- fixed problem with '[' chars in commit messages in journal
- removed issue with space inside renamed repository after deletion
- db transaction fixes when filesystem repository creation failed
- fixed #106 relation issues on databases different than sqlite
- fixed static files paths links to use of url() method

1.1.2 (**2011-01-12**)
======================

news
----


fixes
-----

- fixes #98 protection against float division of percentage stats
- fixed graph bug
- forced webhelpers version since it was making troubles during installation 

1.1.1 (**2011-01-06**)
======================
 
news
----

- added force https option into ini files for easier https usage (no need to
  set server headers with this options)
- small css updates

fixes
-----

- fixed #96 redirect loop on files view on repositories without changesets
- fixed #97 unicode string passed into server header in special cases (mod_wsgi)
  and server crashed with errors
- fixed large tooltips problems on main page
- fixed #92 whoosh indexer is more error proof

1.1.0 (**2010-12-18**)
======================

news
----

- rewrite of internals for vcs >=0.1.10
- uses mercurial 1.7 with dotencode disabled for maintaining compatibility 
  with older clients
- anonymous access, authentication via ldap
- performance upgrade for cached repos list - each repository has it's own 
  cache that's invalidated when needed.
- performance upgrades on repositories with large amount of commits (20K+)
- main page quick filter for filtering repositories
- user dashboards with ability to follow chosen repositories actions
- sends email to admin on new user registration
- added cache/statistics reset options into repository settings
- more detailed action logger (based on hooks) with pushed changesets lists
  and options to disable those hooks from admin panel
- introduced new enhanced changelog for merges that shows more accurate results
- new improved and faster code stats (based on pygments lexers mapping tables, 
  showing up to 10 trending sources for each repository. Additionally stats
  can be disabled in repository settings.
- gui optimizations, fixed application width to 1024px
- added cut off (for large files/changesets) limit into config files
- whoosh, celeryd, upgrade moved to paster command
- other than sqlite database backends can be used

fixes
-----

- fixes #61 forked repo was showing only after cache expired
- fixes #76 no confirmation on user deletes
- fixes #66 Name field misspelled
- fixes #72 block user removal when he owns repositories
- fixes #69 added password confirmation fields
- fixes #87 RhodeCode crashes occasionally on updating repository owner
- fixes #82 broken annotations on files with more than 1 blank line at the end
- a lot of fixes and tweaks for file browser
- fixed detached session issues
- fixed when user had no repos he would see all repos listed in my account
- fixed ui() instance bug when global hgrc settings was loaded for server 
  instance and all hgrc options were merged with our db ui() object
- numerous small bugfixes
 
(special thanks for TkSoh for detailed feedback)


1.0.2 (**2010-11-12**)
======================

news
----

- tested under python2.7
- bumped sqlalchemy and celery versions

fixes
-----

- fixed #59 missing graph.js
- fixed repo_size crash when repository had broken symlinks
- fixed python2.5 crashes.


1.0.1 (**2010-11-10**)
======================

news
----

- small css updated

fixes
-----

- fixed #53 python2.5 incompatible enumerate calls
- fixed #52 disable mercurial extension for web
- fixed #51 deleting repositories don't delete it's dependent objects


1.0.0 (**2010-11-02**)
======================

- security bugfix simplehg wasn't checking for permissions on commands
  other than pull or push.
- fixed doubled messages after push or pull in admin journal
- templating and css corrections, fixed repo switcher on chrome, updated titles
- admin menu accessible from options menu on repository view
- permissions cached queries

1.0.0rc4  (**2010-10-12**)
==========================

- fixed python2.5 missing simplejson imports (thanks to Jens Bäckman)
- removed cache_manager settings from sqlalchemy meta
- added sqlalchemy cache settings to ini files
- validated password length and added second try of failure on paster setup-app
- fixed setup database destroy prompt even when there was no db


1.0.0rc3 (**2010-10-11**)
=========================

- fixed i18n during installation.

1.0.0rc2 (**2010-10-11**)
=========================

- Disabled dirsize in file browser, it's causing nasty bug when dir renames 
  occure. After vcs is fixed it'll be put back again.
- templating/css rewrites, optimized css.