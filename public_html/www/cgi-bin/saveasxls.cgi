#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


# decalarations
my $q = new CGI;
my $session = $q-> param('session');
my $module = $q-> param('module');
my $xlsfile = $q-> param('xlsfile');
my $saveasxls=">>/var/www/cgi-bin/xls/$xlsfile.xls";
my @saveasxls;
open (XLS,$saveasxls);
# basic html starts for outputting
print "Content-Type: text/html\n\n";
print (XLS "$session\t$module\n");
print "<hr size='2.5'>";
