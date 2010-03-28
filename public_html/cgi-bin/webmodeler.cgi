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
my $blastoutput;
my $input;
my $a=0;
my $q= new CGI;

# user name is inputted
my $name = $q-> param ('name');
# user email is inputted
my $email = $q-> param ('email');
# organisation is inputted
my $organization = $q-> param ('organization');
# user sequence is inputted
my $seq = $q->param( 'seq' );
# getting the system date
my $date;
$date = `/bin/date`;
chomp( $date );

# checking the name, email and organization text field
if ($name eq "Sukhdeep Singh") {
die("Please fill out your name please you cant be me !!");
}
if ($email eq 'vanbug@gmail.com') {
die "Thats my email please fill yours !!";
}
if ($organization eq 'University of Leicester') {
die "Don't be lazy please fill your organization where you work or study !!";
}

# running the counter script which enables the visitor counter
my $counter ="/home/ss533/public_html/cgi-bin/counter.txt";
open (COUNTER,$counter);
my $a=<COUNTER>;
$a++;
open (COUNTER,">$counter");
print COUNTER $a;

# storing the user details in a new csv file
my $user = "/home/ss533/public_html/cgi-bin/user.csv";
open(USER,">>$user");
#print USER "NAME\t\t EMAIL\t\t ORGANIZATION\t\t\t DATE\n";
print USER "$a.$name\t $email\t $organization\t $date\n";

# if no sequence is entered the default message is printed
$seq = '' unless $seq;

# removing illegal characters from sequence viz, spaces and digits and special characters
$seq =~ s/\s*\d*\W*//g;

# converting the sequence to uppercase for searching in blast database
$seq = uc($seq);

# basic html starts for outputting
print "Content-Type: text/html\n\n";
print "<html>\n";
print "<head>\n";
print "<title>Output Window </title>\n";
print "</head>\n\n";
print "<h2>$name!! \nThank you for submitting form and using my Webmodeller</h2>";
print "<body>\n\n";
print "Your sequence: <KBD>$seq</KBD><br><br>\n";

# storing the input sequence in a new file
$input = "/home/ss533/public_html/cgi-bin/model.txt";
open(INPUT,">$input");
print INPUT "\>model\n$seq";

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

#checking for template name
if (defined($templatename) && $templatename ne ""){
print "The template found out for your sequence is $templatename\n\n";
}
else
{
print "No siginficant hits found for your sequence\n\n";
}


# protein name is changed from uppercase to lowercase to fetch correct sequence from ftp.
$templatename=lc($templatename);

# regex or matching pattern for the sequence of most significant protein
# first part of seq
while ($_=<FH>) {
if($_ =~ /^Sbjct: \w+\s\s(\w+\w+)/){             # work here to remove digit 
$templateseq1=$1;
last;
}
}

# second part of seq
while ($_=<FH>) {
if($_ =~ /^Sbjct: \w+\s\s(\w+\w+)/){
$templateseq2=$1;
last;
}
}

# concatenation used for joining the 2 parts of sequence to get complete sequence
$templateseq = $templateseq1.$templateseq2;

# for printing of multiple sequence fasta file for alignment
my $multipleseq="/home/ss533/public_html/cgi-bin/multipleseq.fas";
open MULTI,">$multipleseq";
my $seqq;
my @seq;
my $i=1;
print MULTI "\>model\n$templateseq\n";
while (($_=<FH>)&& ($i<10)) {
if($_ =~ /^Sbjct: \w*\s\s(\w+\w+)/){  
$seqq=$1;
print MULTI "\>$i\n$seqq\n";
$i++;
}
}
#second part of seq
my $seqqq;
while (($_=<FH>)&& ($i<6)) {
if($_ =~ /^Sbjct: \w+\s\s(\w+\w+)/){
$seqqq=$1;
print MULTI "\>$i\n$seqqq\n";
$i++;
}
}
close (MULTI);
system ("/usr/bin/clustalw multipleseq.fas");

# storing protein pdb file link in variable
my $protein= "ftp://ftp.wwpdb.org/pub/pdb/data/structures/all/pdb/pdb"."$templatename".".ent.gz";
# downloading its sequence using wget
system("wget $protein");

# gunzipping the pdb file
system("gunzip /home/ss533/public_html/cgi-bin/*.ent.gz");
# renaming the file to template for modeler
system("mv /home/ss533/public_html/cgi-bin/*.ent template.pdb");

# opening the sequence with pymol only for offline
#system ("/usr/bin/pymol");

# storing the template pdb file into a variable
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

open(TEMP,$temp);

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
#system ("/usr/bin/mod9v4 run.py");

# date variable is use to print system date
print "<br><br><br>Date: $date<br>\n\n";
print "<form>";
print "</FORM>";

## my area
# Create the CGI object
my $query = new CGI;

# Output the HTTP header
print $query->header ( );

# Process form if submitted; otherwise display it
if ( $query->param("go") )
{
  process_form ( );
}
else
{
  display_form ( );
}

sub process_form
{
  if ( validate_form ( ) )
  {
    print <<END_HTML;
    <html><head><title>Thank You</title></head>
    <body>
   Blast
    </body></html>
END_HTML
  }
}

sub validate_form
{
  my $your_request = $query->param("your_request");
  
  my $error_message = "";

  $error_message .= "Please specify your request<br>" if ( !$your_request );
  

  if ( $error_message )
  {
    # Errors with the form - redisplay it and return failure
    display_form ( $error_message, $your_request);
    return 0;
  }
  else
  {
    # Form OK - return success
    return 1;
  }
}

sub display_form
{
  my $request = shift;

  # Remove any potentially malicious HTML tags
  #$your_name =~ s/<([^>]|\n)*>//g;

  # Build "selected" HTML for the "Your Sex" radio buttons
  my $blast     = $request eq "blast"    ? "checked" : "";
  my $modeller  = $request eq "modeller" ? "checked" : "";
  my $alignment = $request eq "alignment"? "checked" : "";
  my $clustal   = $request eq "clustal"  ? "checked" : "";
    # Display the form
  print <<END_HTML;
  <html>
  <head><title>Form Validation</title></head>
  <body>

  <form action="reports.html" method="post">
  <input type="hidden" name="submit" value="Submit">
  <input type="radio" name="Blast report" value="blast"$blast>          Blast Report
  <input type="radio" name="Modeller report" value="modeller"$modeller> Modeller Report
  <input type="radio" name="Alignment file" value="alignment"$alignment>Alignment Report
  <input type="radio" name="Clustal report" value="clustal"$clustal">   Clustal Report
  </p>
  <input type="submit" name="go" value="go">
</form> 
  </body></html>
END_HTML

}
print ("Please wait while modeller is running...\n");
#system ("/usr/bin/mod9v4 run.py") ;
print ("The job is finished");
print "<HR>";
print "Thanks for visiting my page.<br> $name you are $a th visitor of my website.<br> <b>Total Visits : $a</b>";
print "<marquee><font face=andy><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br> Created by <b>Sukhdeep Singh</b> Webmodeller v 1.0</font></marquee>";
print "</body>\n";
print "</html>\n";
