#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


# decalarations
my $userfiles;
my @userfiles;
my $historyfile;
my @historyfile;
my $xlsfiles;
my @xlsfiles;
# basic html starts for outputting
print "Content-Type: text/html\n\n";
@userfiles = `ls /home/ss533/public_html/cgi-bin/usersheets/*.txt`;
@historyfile= `ls /home/ss533/public_html/cgi-bin/userhistory/*.txt`;
@xlsfiles=`ls /home/ss533/public_html/cgi-bin/xls/*.xls`;
print "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<b>Browse Userfiles</b> ";
print "<select id=\"download_chooser\" onChange=\"downloading();\">";
foreach $userfiles(@userfiles){
$userfiles =~/^.+\/usersheets\/(.+)/;
print "<option>$1</option>";
}
print "</select>";
print "<b> Browse Historyfiles </b>";
print "<select id=\"historyfilechooser\" onChange=\"downloadhistoryfile();\">";
foreach $historyfile(@historyfile){
$historyfile =~/^.+\/userhistory\/(.+)/;
print "<option>$1</option>;"
}
print "</select>";
print "<select id =\"xlsfileschooser\" onChange=\"downloadxlsfile();\">";
foreach $xlsfiles(@xlsfiles){
$xlsfiles=~/.+\/xls\/(.+)/;
print "<option>$1</option>";
}
print "</select>";


