#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# basic html starts for outputting
print "Content-Type: text/html\n\n";
print <<END_HTML;
<html>
<head>
<title> Insect brain signal data </title>
<br><br>
<center>
<H1>BUGPAN </H1>
<frameset rows="25%,50%,25%">
</frameset>
<form action="sessions.cgi" method="post" target="blank">
<input type="submit" name="sessions" value="Check Sessions">
</form>
</body>
</html>
END_HTML


