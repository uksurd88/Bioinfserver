#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);
# basic html starts for outputting
print "Content-Type: text/html\n\n";
system("/home/ss533/.cabal/bin/bugsess show 72c >/var/www/session.txt\n");
system("/home/ss533/.cabal/bin/bugsess show 72c ");
print <<END_HTML;
<html>
<head>
<title> Session 1 </title>
<br><br>
<center>
<form action="framestest.html" method="post"> 
<input type="submit" name="goback" value="Return to home page">
</center>
</body>
</html>
END_HTML
