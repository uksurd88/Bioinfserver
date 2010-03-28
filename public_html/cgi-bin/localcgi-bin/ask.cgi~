#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# My declarations
my $q= new CGI;
my $ask;
my @buglist;
my $i=0;
my $session=$q-> param ('session');
my $line;
my $query = $q-> param ('query');
# basic html starts for outputting
print "Content-Type: text/html\n\n";
@buglist = `bugsess list`;
foreach $line (@buglist)
{
$line =~ /(\w+)/;
$i++;
}
print $query;	
print `bugsess ask1 $session '$query'`;
print "Success";


