var myMenuItems = [
  {
    name: 'Add Query Column',
    className: 'add query column', 
    callback:function() {
      ins();
    }
  },{
    name: 'Add User Column',
    className: 'add user column', 
    callback: function() {
      usercol();
    }
  },{
    name: 'Calculate Statistics', 
    className: 'stats',
    callback:function() {
    recalcStats();
    }
  },{
    name: 'Save',
    className: 'save',
    callback: function() {
      savecheck();
    }
  },{
  name: 'Reset',
  className:'reset',
  callback:function(){
  resetsheet();
  }
  }
]

