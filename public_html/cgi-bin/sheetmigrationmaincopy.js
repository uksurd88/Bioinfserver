/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*Author : Sukhdeep Singh
email : vanbug@gmail.com
Organization : University of Leicester, United Kingdom

Description :  A script designed for migrating with in the cells of the dynamic spreadsheet via keyboard using the Keyboard Events 
defined in the prototype library of javascript.
Usage Policy : Using this script for educational purposes is recommended but for commercial purposes it should be asked from author also 
before amending or selling. If passed, it should be passed in its original form with author's name on the top.
@CopyRight Sukhdeep Singh
*/
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	function migrate(e) {
	cellid(e);
	 var key = e.which || e.keyCode;
		if (firsttimeselect>0) {
			var rowcount = (numberofRows+2);// 2 is added because 2 rows are there of Mean and Standard Deviation
			currentcell = currentcell;
			currentcellid = currentcell.substring(0,4);
			var mymatch = /(\d$)/;
			var currentcellidnumber = currentcell.match(mymatch);
			currentcellidnumber = parseInt(currentcellidnumber[0]);
				for (var z=0;z<rowcount;z++) {
					if (currentcellidnumber==z) 
					nextcellnumber = currentcellidnumber+1;
					else 
					nextcellnumber = currentcellidnumber-1;
				}
			var nextcell = currentcellid+nextcellnumber;
		
			switch (key) {
   				case Event.KEY_UP: {
					if (currentcellid == "name") {
						$(nextcell).style.border = "7px inset white";
						$(currentcell).style.border = "1px solid white";
						var currentcellvalue = $(nextcell).innerHTML;
							new Ajax.Updater('detailask','/cgi-bin/migrationsessionshow.cgi',{
							parameters:{session:currentcellvalue}});
							currentcell = nextcell;
					}
						else if (currentcellid == "date") {
							$(nextcell).style.border = "7px inset white";
							$(currentcell).style.border = "1px solid white";
							var currentcellvalue = $("name"+(currentcellidnumber-1)).innerHTML;
								new Ajax.Updater('detailask','/cgi-bin/migrationdateshow.cgi',{
								parameters:{session:currentcellvalue}});
									currentcell = nextcell;
						}
							else if (currentcellid == "mode") {
								$(nextcell).style.border = "7px inset white";
								$(currentcell).style.border = "1px solid white";
								var currentcellvalue = $("mode"+(currentcellidnumber-1)).innerHTML;
								var sessionname = $("name"+(currentcellidnumber-1)).innerHTML;
									new Ajax.Updater('detailask','/cgi-bin/migrationmoduleshow.cgi',{
									parameters:{module:currentcellvalue,session:sessionname}});
									currentcell = nextcell;
							}
								else if(currentcellid == "qvry") {
								var nextcell = "qvry"+(currentcellidnumber-1)+'_'+userquerycolumns;
								}
				}
     				break;
   				case Event.KEY_LEFT: {
	    				if (currentcellid == "mode") {
						var migratecell="date";
						var newcell = migratecell+currentcellidnumber;
						$(newcell).style.border = "7px inset white";
						$(currentcell).style.border = "1px solid white";
						var currentcellvalue = $("name"+currentcellidnumber).innerHTML;
						currentcell =newcell;
							new Ajax.Updater('detailask','/cgi-bin/migrationdateshow.cgi',{
							parameters:{session:currentcellvalue}});
					}
						else if (currentcellid == "date") {
							var migratecell="name";
							var newcell = migratecell+currentcellidnumber;
							$(newcell).style.border = "7px inset white";
							$(currentcell).style.border = "1px solid white";
							var currentcellvalue = $(newcell).innerHTML;
							currentcell =newcell;
								new Ajax.Updater('detailask','/cgi-bin/migrationsessionshow.cgi',{
								parameters:{session:currentcellvalue}});
						}
							else if (currentcellid == "qvry") {
								var migratecell = "mode";
								alert(currentcellidnumber);
								var newcell = (migratecell+(currentcellidnumber-1));
								$(newcell).style.border = "7px inset white";
								$(currentcell).style.border = "1px solid white";
								var currentcellvalue = $("name"+(currentcellidnumber-1)).innerHTML;
									new Ajax.Updater('detailask','/cgi-bin/migrationmoduleshow.cgi',{
									parameters:{session:currentcellvalue}});
									currentcell = newcell;
							}
    				}
			     break;
			     case Event.KEY_RIGHT: {
 					if (currentcellid == "name") {
						var migratecell="date";
						var newcell = migratecell+currentcellidnumber;
						$(newcell).style.border = "7px inset white";
						$(currentcell).style.border = "1px solid white";
						var currentcellvalue = $(currentcell).innerHTML;
							new Ajax.Updater('detailask','/cgi-bin/migrationdateshow.cgi',{
							parameters:{session:currentcellvalue}});
							currentcell =newcell;
					}
						else if (currentcellid == "date") {
							var migratecell="mode";
							var newcell = migratecell+currentcellidnumber;
							$(newcell).style.border = "7px inset white";
							$(currentcell).style.border = "1px solid white";
							var currentcellvalue = $(newcell).innerHTML;
							var sessionname = $("name"+currentcellidnumber).innerHTML;
								new Ajax.Updater('detailask','/cgi-bin/migrationmoduleshow.cgi',{
								parameters:{module:currentcellvalue,session:sessionname}});
								currentcell =newcell;
						}
							else if (currentcellid == "mode") {
								var migratecell=("qvry"+currentcellidnumber+'_'+userquerycolumns);
								var newcell = migratecell;
								$(newcell).style.border = "7px inset white";
								$(currentcell).style.border = "1px solid white";
								var currentcellvalue = $(migratecell).innerHTML;
								var session = $("name"+currentcellidnumber).innerHTML;
								var userquery = $("userquery"+userquerycolumns).value;
									if (currentcellvalue != "<i>Query Result</i>") {
									new Ajax.Updater('detailask','/cgi-bin/sessions2.cgi',{
									parameters:{session:session,query:userquery}});
									}
									currentcell=newcell;
				// This condition can be made true to fetch the image or histogram of user query as its value is contained in currentcellvalue
				//else if (currentcellvalue != "<i>Query Result</i>" && migratecell ==)
							}
     				}
				break;
				case Event.KEY_DOWN: {
					nextcellnumber = (currentcellidnumber+1);
					var newcell = currentcellid+(nextcellnumber);
    					if (currentcellid == "name"){
						$(newcell).style.border = "7px inset white";
						$(currentcell).style.border = "1px solid white";
						var currentcellvalue = $(newcell).innerHTML;
							new Ajax.Updater('detailask','/cgi-bin/migrationsessionshow.cgi',{
							parameters:{session:currentcellvalue,name:currentcellid}});
					}	
						else if (currentcellid == "date") {
							$(newcell).style.border = "7px inset white";
							$(currentcell).style.border = "1px solid white";
							var sessionfetchcell = "name"+(currentcellidnumber+1);
							var currentcellvalue = $(sessionfetchcell).innerHTML;
								new Ajax.Updater('detailask','/cgi-bin/migrationdateshow.cgi',{
								parameters:{session:currentcellvalue}});
						}
							else if (currentcellid == "mode") {
								$(newcell).style.border = "7px inset white";
								$(currentcell).style.border = "1px solid white";
								var currentcellvalue = $("mode"+(currentcellidnumber+1)).innerHTML;
								var sessionname = $("name"+(currentcellidnumber+1)).innerHTML;
									new Ajax.Updater('detailask','/cgi-bin/migrationmoduleshow.cgi',{
									parameters:{module:currentcellvalue,session:sessionname}});
							}
								else if (currentcellid == "qvry") {
									var newcell = currentcellid+(nextcellnumber)+'_'+userquerycolumns;
									$(newcell).style.border = "7px inset white";
									$(currentcell).style.border = "1px solid white";
									nextcellnumber++;
								}
									currentcell=newcell;
				cell = newcell;
				selectcell(e,cell);
				}
			}
		}
	}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
