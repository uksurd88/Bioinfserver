
/*
 * Toggles the rows from EDIT mode to VIEW mode. 
 * Invoked on clicking the 'SAVE' button in last column. 
 */
function makeRowViewable(rowNumber,id) {
        var table = document.all ? document.all[id]  : document.getElementById ? document.getElementById(id) : null;
        var editableRowNumber = rowNumber + 1 ;
        var nonEditableRowNumber = editableRowNumber -1 ;
        table.rows[editableRowNumber].style.display = "none" ;
        table.rows[nonEditableRowNumber].style.display = "block" ;  
}

/*
 * Toggles the rows from view mode to edit mode. 
 * Invoked on clicking the 'EDIT' button in last column. 
 */
function makeRowEditable(rowNumber,id) {
        var table = document.all ? document.all[id]  : document.getElementById ? document.getElementById(id) : null;
        var editableRowNumber = rowNumber + 1 ;
        var nonEditableRowNumber = editableRowNumber -1 ;
        table.rows[editableRowNumber].style.display = "block" ;
        table.rows[nonEditableRowNumber].style.display = "none" ;
}

