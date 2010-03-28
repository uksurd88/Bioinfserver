#!/usr/bin/perl
  
  # index.pl
  use CGI;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session ( '-ip_match' );
  
  $session = CGI::Session->load();
  $q = new CGI;
  
  if($session->is_expired)
  {
      print $q->header(-cache_control=>"no-cache, no-store, must-revalidate");
      print "Your has session expired. Please login again.";
 print "<br/><a href='login.pl>Login</a>";
  }
  elsif($session->is_empty)
  {
      print $q->header(-cache_control=>"no-cache, no-store, must-revalidate");
      print "You have not logged in";
  }
  else
  {
      print $q->header(-cache_control=>"no-cache, no-store, must-revalidate");
      print "<h2>Welcome";
      print "<a href='login.pl?action=logout'>Logout";
  }
