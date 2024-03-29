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
# The next two lines will add the 'ghc' compiler in path of server as we are setting the enviromental variable PATH fo it.
my $path=$ENV{'PATH'};
$ENV{'PATH'}='/usr/local/bin:/usr/bin:/bin:/home/ss533/ghc/bin/';
# basic html starts for outputting
print "Content-Type: text/html\n\n";
# /home/ss533/.cabal/bin/bugsess query
$bugask = `/home/ss533/.cabal/bin/bugsess ask1 $sessionName '$query' -g 2>/dev/null`; #2>/dev/null sends the error messages to the blackhole.
if ($bugask=~/^<img\ssrc="\/(\w*\d*)\/(\w*\d*)\/(\w*\d*)\/(\w*\d*)\/(.+)\/(.+)"/) {

	`mkdir -p /home/ss533/public_html/cgi-bin/histogram/$5`;
	`cp /home/ss533/bugdir/www/$5/$6 /home/ss533/public_html/cgi-bin/histogram/$5/`;
	print `chmod 777 /home/ss533/public_html/cgi-bin/histogram/$5/$6`;
	print "<img src='http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/histogram/$5/$6' onclick='detailask(\"".$query."\",\"".$sessionName."\");'/>";
	}
###################################################################################
# for the case of signals
#	file:///home/ss533/bugdir/www/cb108bb1c7b20d7b0498/plots1.html 
	elsif ($bugask=~/^file\:\/\/\/\w+\/\w+\/\w+\/\w+\/(.+)\/(.+)/){
		$sessionfolder=$1;
		$plothtmlfile = $2;
		if ($i==0) {
			`rm -rf /home/ss533/public_html/cgi-bin/bugpandata/ecVoltage/*`;
		}
			`mv  -f /home/ss533/bugdir/www/$1 /home/ss533/public_html/cgi-bin/bugpandata/ecVoltage/`; 
			`chmod 644 /home/ss533/public_html/cgi-bin/bugpandata/ecVoltage/$1/* >/dev/null`;#sending outputs to null a kind of blackhole absorbs everything
			my $graphfile=`ls /home/ss533/public_html/cgi-bin/bugpandata/ecVoltage/$1/`;
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
