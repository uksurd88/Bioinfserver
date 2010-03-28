#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# decalarations
my $q = new CGI;
my $session = $q -> param('session');
my $bugshot1= `sleep 5;import -window root bugshot1.png`;
# basic html starts for outputting
print "Content-Type: text/html\n\n";
print $bugshot1;
print "<hr size='2.5'>";
