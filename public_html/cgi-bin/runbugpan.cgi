#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


# decalarations
my $q = new CGI;
my $runoption = $q -> param('runoption');
my $runbugpan;
# basic html starts for outputting
print "Content-Type: text/html\n\n";
if (defined $runoption) {
$runbugpan = `/home/ss533/.cabal/bin/runbugpan $runoption`;
}
print "<pre>$runbugpan</pre>";
