#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# My declarations
my $q = new CGI;
my $i;
my $query = $q -> param('query');
my $sessionName = $q -> param('session');
my $i=$q->param('i');
my $bugask;
my $wantedfile;
my @plotfile;
my $plotfile;
my $graphimage;
my $sessionfolder;
my $plothtmlfile;
# basic html starts for outputting
print "Content-Type: text/html\n\n";
# bugsess query
$bugask = `bugsess ask1 $sessionName '$query' -g 2>/dev/null`; #2>/dev/null sends the error messages to the blackhole.

if ($bugask=~/^<img\ssrc="\/var\/bugpan\/www\/(.+)\/(.+)"/) {
	`mkdir -p /var/www/histogram/$1`;
	`cp /var/bugpan/www/$1/$2 /var/www/histogram/$1/`;
	print `chmod 644 /var/www/histogram/$1/$2`;
	print "<img src='/histogram/$1/$2' onclick='detailask(\"".$query."\",\"".$sessionName."\");'/>";
	}
###############################################################################	
	elsif ($bugask=~/^file\:\/\/\/\w+\/\w+\/\w+\/(.+)\/(.+)/){
		$sessionfolder=$1;
		$plothtmlfile = $2;
		if ($i==0) {
			`rm -rf /var/www/cgi-bin/bugpandata/ecVoltage/*`;
		}
			`mv  -f /var/bugpan/www/$1 /var/www/cgi-bin/bugpandata/ecVoltage/`; 
			`chmod 644 bugpandata/ecVoltage/$1/* >/dev/null`;					#sending outputs to null a kind of blackhole absorbs everything
			my $graphfile=`ls bugpandata/ecVoltage/$1/`;
				if ($graphfile=~/(\d*\w*.\d*\w*)/){
				$graphimage= $1;
				}
			print "<span><img src='bugpandata/ecVoltage/$sessionfolder/$graphimage' WIDTH=100 HEIGHT=50 ALIGN='LEFT' ALT='No plot for this session' 
			onclick='detailask(\"".$query."\",\"".$sessionName."\",\"".$sessionfolder."\",\"".$plothtmlfile."\");'><br>.......</img></span>";
	}
else 
{
print $bugask;
}
