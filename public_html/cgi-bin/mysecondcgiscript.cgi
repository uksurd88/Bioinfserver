#!/bin/sh

echo "Content-type: text/html"
echo
echo "Hello, world!"

<form name="hello" method="post" action="/cgi-bin/hello.sh">
  <input type="submit" value="Run it!" />
</form>
