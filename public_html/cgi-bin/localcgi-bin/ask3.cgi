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
my @bugask1;
my @bugask2;
my $bugask1;
my $bugask2;
my $i=0;
my $session=$q-> param ('session');
my $line;
my $query = $q-> param ('query');
# basic html starts for outputting
print "Content-Type: text/html\n\n";
@bugask1 = `bugsess ask1 $session '$query'`;
@bugask2 = `bugsess ask1 $session '$query' -g 2>/dev/null`;
if ($query=~/^\w*\d*\s+/)
{
print "<kbd> @bugask2 </kbd>";
}
else 
{
print "<kbd> @bugask1 </kbd>";
}
print "<hr size=2.5>";


