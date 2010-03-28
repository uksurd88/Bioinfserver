#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);
# decalarations
my $q = new CGI;
my $session=$q->param('session');
my $uservalue=$q->param('uservalue');
my $uservariable=$q->param('uservariable');
my @bugusercol = `bugsess mkndur $session $uservariable $uservalue`;
# basic html starts for outputting
print "Content-Type: text/html\n\n";
print "bugsess mkndur $session $uservariable $uservalue 2>/dev/null"; 
print @bugusercol;
print "<hr size='2.5'>";
