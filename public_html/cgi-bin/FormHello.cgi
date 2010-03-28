#!/usr/local/bin/perl
 print "Content-type: text/html\n\n";
 print "Hello World.\n";
 print "Heres the form info:<P>\n";
 my($buffer);
 my(@pairs);
 my($pair);
 read(STDIN,$buffer,$ENV{'CONTENT_LENGTH'});
 @pairs = split(/&/, $buffer);
 foreach $pair (@pairs)
   {
   print "$pair<BR>\n"
   }
print "<P>Note that further parsing is\n";
print "necessary to turn the plus signs\n";
print "into spaces and get rid of some\n";
print "other web encoding.\n";
hell
