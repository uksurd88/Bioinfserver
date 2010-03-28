// Author: Sukhdeep Singh
//  email: ss533@le.ac.uk

// JavaScript file containing functions using prototype

// Function insert to insert new column for query
var counter;

function ins() {
	var i;
	var toprow=$("sesRow");
	colcount=colcount+1;
	var topitem='<td><input type="text" onChange="result(0)" id="userquery'+colcount+'"></input>';
	toprow.insert({Bottom:topitem});
	for (i=0;i<numberofRows;i++)
	{
	var row=$("sessRow"+i);
	var item='<td id="query'+i+'_'+colcount+'"><i>Query Result</i></td>';
	row.insert({Bottom:item});
	}
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function usercol() {
	var i;
	var topII=$("sesRow");
	colcount=colcount+1;
	topII.insert({Bottom:'<td><input type="text" id="usercol'+colcount+'" value="         User Column"></input>'});
	for (i=0;i<numberofRows;i++)
	{
	var rowII=$("sessRow"+i);
	var item='<td><input type="text" id="usercol'+i+'_'+colcount+'" ></input></td>';
	rowII.insert({Bottom:item});
	}
//alert(item.value);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function saving() {
var userquery=$("userquery"+colcount).value;
for (i=0;i<numberofRows;i++)
{
var useroutput=$("query"+i+'_'+colcount).innerHTML;
}
alert(useroutput);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function result(rowNumber) {
var query=$("userquery"+colcount).value;
new Ajax.Request('/cgi-bin/ask2.cgi', {
	method : 'get',
	parameters : {query:query,session:sessionName[rowNumber]},
	onSuccess: processResponse,
					});
counter=rowNumber;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function processResponse(resp) {
	$('query'+counter+'_'+colcount).update(resp.responseText);
	if(counter<numberofRows) result(counter+1);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function changeSession() {
	var sessionName=$("sessionchooser").value;
	new Ajax.Updater('showSession', '/cgi-bin/show.cgi', {
  		parameters: { session: sessionName }});

}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function askQuery() {
alert(sessionName[1]);
	//new Ajax.Updater('showQuery','/cgi-bin/ask.cgi', {
	//parameters : {query:query,session:sessionName[rowNumber]},
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
