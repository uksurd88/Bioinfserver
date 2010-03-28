#!/usr/bin/perl

# loading usual development settings
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# declaring variables
my @i;
my $i;
my $templateseq;
my $templateseq1;
my $templateseq2;
my $templatename;
my $digits_basedir;
my $count_file;
my $place;
my $Write;
my $count;
my @chiffres;
my $q = new CGI;
my $blastoutput;
my $input;

# user sequence is inputted
my $seq = $q->param( 'seq' );

# if no sequence is entered the default message is printed
$seq = '' unless $seq;

# basic html starts
print "Content-Type: text/html\n\n";
print "<html>\n";
print "<head>\n";
print "<title>Output Window </title>\n";
print "</head>\n\n";
print "<body>\n\n";
print "Hello <br><br>\n";
print "Your sequence: $seq<br><br>\n";
print "REMOTE_ADDR = $ENV{'REMOTE_ADDR'}\n\n";

# storing the input sequence in a new file
$input = "/home/ss533/public_html/cgi-bin/model.txt";
open(INPUT,">$input");
print INPUT $seq;

# running blast on local server
system ("/home/ss533/blast-2.2.20/bin/blastall -p blastp -i model.txt -d pdb.fasta -o r.txt");

# storing the result of blast in local variable
$blastoutput = "/home/ss533/public_html/cgi-bin/r.txt";

# opening filename or printing error messsage
open(FH,$blastoutput) or die "Cannot open $blastoutput :$! ";

# regex or matching pattern for most significant hit
while ($_=<FH>) {
if($_ =~ /^gi\|\d+\|pdb\|(\w\w\w\w)\|/){
$templatename=$1;
last;
}
}

# printing the template name
print "The tepmlate found out for your sequence is $templatename\n";
# protein name is changed from uppercase to lowercase to fetch correct sequence from ftp.
$templatename=lc($templatename);

# regex or matching pattern for the sequence of significant protein
# first part of seq
while ($_=<FH>) {
if($_ =~ /^Sbjct: \w+\s\s(\w+\w+)/){             # work here to remove digit 
$templateseq1=$1;
last;
}
}

# second par of seq
while ($_=<FH>) {
if($_ =~ /^Sbjct: \w+\s\s(\w+\w+)/){
$templateseq2=$1;
last;
}
}

# concatenation used for joining the 2 parts of sequence to get complete sequence
$templateseq = $templateseq1.$templateseq2;
#print $templateseq;

# storing protein pdb file link in variable
my $protein= "ftp://ftp.wwpdb.org/pub/pdb/data/structures/all/pdb/pdb"."$templatename".".ent.gz";
# downloading its sequence using wget
system("wget $protein");

# gunzipping the pdb file
system("gunzip /home/ss533/public_html/cgi-bin/*.ent.gz");
# renaming the file to template for modeler
system("mv /home/ss533/public_html/cgi-bin/*.ent template.pdb");

# opening the sequence with pymol
#system ("/usr/bin/pymol");


my $temp = "/home/ss533/public_html/cgi-bin/template.pdb";
my $firstresidue;
my $lastresidue;
my $lastresidue1;
my $lastresidue2;
my $firstnumber;
my $lastnumber;
my $lastnumber1;
my $lastnumber2;
my $HETATM;
open(TEMP,$temp) or print "No Significant Hits found \n\n";

while ($_=<TEMP>) {
if($_=~ /^ATOM\s+\d+\s+\w+\s+\w+\s(\w)\s+(\d)/){
#print "$1\n";
$firstresidue = $1;
$firstnumber = $2;
last;
}
}
while ($_=<TEMP>) {
if($_=~ /^ATOM\s+\d+\s+\w+\s+\w+\s(\w)\s+(\d+)/){
#print "$1\n";x	x	
$lastresidue1 = $1;
$lastnumber1 = $2;
}
}


while ($_=<TEMP>) {
if($_=~ /^(HETATM)\s+\d+\s+\w+\d+\s+\w+\s+(\w)(\d+)/){
#print "$1\n";
$HETATM=$1;
$lastresidue2 = $2;
$lastnumber2= $3;
last;
}
}
if (defined($HETATM) && $HETATM ne ""){
$lastresidue=$lastresidue2;
$lastnumber=$lastnumber2;
}
else {
$lastresidue=$lastresidue1;
$lastnumber=$lastnumber1;
}
print $lastresidue1;
print $lastresidue2;

print "$firstresidue\n";
print "$lastresidue\n";
print "$firstnumber\n";
print "$lastnumber";



# making ali file for modeler
my $fastafile ="/home/ss533/public_html/cgi-bin/alignment.ali";
open(FILE,">$fastafile");
# printing the template sequence in ali file
print FILE ">P1;template\nstructureX:template:$firstnumber:$firstresidue:$lastnumber:$lastresidue:.:.:.:.\n$templateseq\/$templateseq\/*\n\n";
# printing the model sequence in the ali file
print FILE ">P1;model \nsequence:model:.:.:.:.:.:.:.:.\n$seq\/$seq\/*";


# removing template file after every run so as to print error message if no hit is found
#system ("rm template.pdb");

# closing of file handle
close(TEMP);

# running modeller
system ("/usr/bin/mod9v4 run.py");

# date variable is use to print system date
my $date = `/bin/date`;
chomp( $date );
print "\n\ndate: $date<br>\n\n";

## my area
print "<HR>";
print "<marquee><font face=andy><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br> Created by <b>Sukhdeep Singh</b> Webmodeller v 1.0</font></marquee>";
print "</body>\n";
print "</html>\n";
