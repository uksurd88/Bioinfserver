#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);
# Fetching url from perl
#use Data::Dumper;
#require HTTP::Request;
#require LWP::UserAgent;
#my $request = HTTP::Request->new(GET => 'http://google.com/');
#my $ua = LWP::UserAgent->new;
#my $response = $ua->request($request);
#print $response->as_string();
# decalarations
my $q = new CGI;
my $session = $q -> param('session');
our $date;
my @bugshow;
my $line;
@bugshow = `/home/ss533/.cabal/bin/bugsess show $session 2>/dev/null`;
# basic html starts for outputting
print "Content-Type: text/html\n\n";
foreach $line(@bugshow)
{
$line =~/^\w+\s+\w+:(.+\d$)/;
$date=$1;
print "<h4><center><b style='color:#008000'>The selected session <b style='color:#B22222'>'$session'</b> was started on <b style='color:#B22222'>$date.</b></center></h4>";
last;
}
print "<hr size='2.5'>";
