#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# My declarations
my $q = new CGI;
my $userquery = $q -> param('userquery');
my $filename = $q -> param('filename');
my @userfile;
my $userfile = ">>/var/usersheets/$filename.txt"; # let the angles be '2' in number for appending to the file
open (USER,$userfile);
# basic html starts for outputting
print "Content-Type: text/html\n\n";
# bugsess query
print (USER "$userquery\n");
