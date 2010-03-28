#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI qw(:cgi);
# Outputs any errors to the browser window
use CGI::Carp qw(fatalsToBrowser)


print "Content-Type: text/html";
print <<END_HTML;
<input type="text" id="text">Hello</input>
END
