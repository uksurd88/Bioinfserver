#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


# decalarations
my $q = new CGI;
my $display= $q-> param('display');
my $filename = $q-> param('filename');
my @bugshow;
my $historyfile = ">>/home/ss533/public_html/cgi-bin/userhistory/$filename.txt";
open (HISTORY,$historyfile);
# basic html starts for outputting
print "Content-Type: text/html\n\n";
print (HISTORY "$display\n");
print "<b style='color:navy'>$display</b>";
