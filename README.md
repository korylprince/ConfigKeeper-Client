ConfigKeeper-Client
https://github.com/korylprince/ConfigKeeper-Client

#Installing#

I run this on Ubuntu servers. Keep that in mind.

Copy client.py to any location you wish. Then create a config using the config.def as a base.

Requires the watchdog module:

sudo pip install watchdog

Included is an init script that should work on Ubuntu/Debian systems.

Copy configkeeper-client.sh to /etc/init.d/

Copy configkeeper-client to /usr/bin/

Copy config.def to /etc/configkeeper-client (file)

Afterwards run

sudo update-rc.d configkeeper-client defaults

If you have any issues or questions, email the email address below, or open an issue at:
https://github.com/korylprince/ConfigKeeper-Client/issues

#Usage#

config.def explains each option. Create your own config and run:
configkeeper-client /path/to/config

Alternatively you can run it as a service as described above.

The client logs to stdout as well as syslog.

The client will send each file specified in the config when you first run, then will monitor each file for changes and send that file on a change.

You can specify files or directories in the list, but I recommend you specify only files so that temporary files do not fill up your list.

#Copyright Information#

All code is Copyright 2012 Kory Prince (korylprince at gmail dot com.) This code is licensed under the GPL v3 which is included in this distribution. If you'd like it licensed under another license then send me an email.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
