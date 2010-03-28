#!/usr/bin/perl
use CGI;
my $q = new CGI;
my $theuser = $q->param( 'user' );
$theuser = '' unless $theuser;
print "Content-Type: text/html\n\n";
print "<html>\n";
print "<head>\n";
print "<title>CGI/Perl Test </title>\n";
print "</head>\n\n";
print "<body>\n\n";
print "Hello, world!<br><br>\n";
print "Your name: $theuser<br><br>\n";
my $date = `/bin/date`;
chomp( $date );
print "date: $date<br>\n\n";
print "</body>\n";
print "</html>\n";
