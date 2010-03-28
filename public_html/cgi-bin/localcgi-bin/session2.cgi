#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);
# basic html starts for outputting
print "Content-Type: text/html\n\n";
system(" bugsess show 5d8 >/var/www/session.txt\n");
system(" bugsess show 5d8");
print <<END_HTML;
<center>
<form action="framestest.html" method="post"> 
<input type="submit" name="goback" value="Return to home page">
</center>
END_HTML


