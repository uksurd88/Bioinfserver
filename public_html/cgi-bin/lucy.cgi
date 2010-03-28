   1.  use CGI qw/:standard/;
   2. print
   3. header,
   4. start_html('Simple Script'),
   5. h1('Simple Script'),
   6. start_form,
   7. "What's your name? ",textfield('name'),p,
   8. "What's the combination?",
   9. checkbox_group(-name=>'words',
  10. -values=>['eenie','meenie','minie','moe'],
  11. -defaults=>['eenie','moe']),p,
  12. "What's your favorite color?",
  13. popup_menu(-name=>'color',
  14. -values=>['red','green','blue','chartreuse']),p,
  15. submit,
  16. end_form,
  17. hr,"\n";
  18.
  19. if (param) {
  20. print
  21. "Your name is ",em(param('name')),p,
  22. "The keywords are: ",em(join(", ",param('words'))),p,
  23. "Your favorite color is ",em(param('color')),".\n";
  24. }
  25. print end_html;
