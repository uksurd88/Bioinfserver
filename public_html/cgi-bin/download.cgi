#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# my decalarations
my $q = new CGI;
my $username = $q -> param('username');
my $userquery = $q -> param('userquery');
my $filename = $q -> param('filename');
my $selectedfile = $q -> param('selectedfile');
my $columncount =$q -> param('columncount');
my $locatedfile = "/home/ss533/public_html/cgi-bin/usersheets/$selectedfile";
my $i=($columncount+1);
my @filedata;
my $filedata;
# HTML for ouputting
print "Content-Type: text/javascript\n\n";
# Fetching userfile data in File handle for pattern match
open (FH,$locatedfile);
@filedata = <FH>;
foreach $filedata(@filedata)
{
	$filedata =~/^(.+)/;
	print 'ins();';
	print  '$("userquery'.$i.'").value="'.$1.'";'; # complexity resolved
	print 'result(0,'.$i.');';
		$i++;
}
print "columncountcheck=$i;";
close FH;

