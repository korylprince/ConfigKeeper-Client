
ConfigKeeper-Client
https://github.com/korylprince/ConfigKeeper-Client

#Installing#

Copy client.py to any location you wish. Then create a config using the config.def as a base.

If you have any issues or questions, email the email address below, or open an issue at:
https://github.com/korylprince/ConfigKeeper-Client/issues

#Usage#

config.def explains each option. Create your own config and run:
client.py /path/to/config

The client logs to stdout as well as syslog.

I suggest you use a cron job to run the client at regular intervals. Alternatively you could run it every time you change a config.

Remember that the user you run client.py with must have access to the files in your config.

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
