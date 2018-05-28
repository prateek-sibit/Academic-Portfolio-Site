// Selecting publications to display based on clicked button
// button has an attribute 'year'
// 1. create 'year' list which can vary from (1985,2018)
// 2. assign to each year in this range with a click event
// 3. on click event -> toggle the li object with the same year

var year = [];

for(var i=1985;i<=2018;i++)
{
  year.push(i);
}

// Selectors to use
// $("li.2008") : Selects publication in the list
// $(".btn.btn-primary.btn-sm.2008") : selects the button clicked on

year.forEach(function(element){
  $(".btn.btn-primary.btn-sm."+element).click(function(){
      // add clicked button to active class
      $("ol li").hide()
      $("li."+element).show();
  });
});

$("#disp_all").click(function(){
  // on click of all apply show() to all year li's
  year.forEach(function(element){
        $("li."+element).show();
  });
});
