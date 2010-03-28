<?php
  $email = $_REQUEST['email'] ;
  $message = $_REQUEST['message'] ;

  mail( "yourname@example.com", "Feedback Form Results",
    $message, "From: $email" );
  header( "Location: http://www.example.com/thankyou.html" );
?>
