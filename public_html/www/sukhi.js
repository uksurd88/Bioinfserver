function changeSession() {
	var sessionName=$("sessionchooser").value;
	new Ajax.Updater('showSession', '/cgi-bin/show.cgi', {
  		parameters: { session: sessionName }});

}

function askQuery() {
var sessionName=$("sessionchooser").value;
var queryString=$("queryString").value;
	new Ajax.Updater('showQuery','/cgi-bin/ask.cgi', {
	parameters: { session:sessionName, query:queryString }});
}
