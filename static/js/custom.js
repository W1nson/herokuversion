

function filterSelectionSingle(c) {
	var x, i;	
  // toggleSingle();
	x = document.getElementsByClassName(("filterTr"));
	if (c == "all") c = "";
	
	for (i = 0; i < x.length; i++) {
	  w3AddClass(x[i], "showtr");
	  if (x[i].className.indexOf(c) > -1) w3RemoveClass(x[i], "showtr");
	  
	}
  }

function filterSelection(c) {
  var x, i;  
  // toggle();
  x = document.getElementsByClassName(("filterTr"));
  if (c == "all") c = "";
  
  for (i = 0; i < x.length; i++) {
	w3AddClass(x[i], "showtr");
    if (x[i].className.indexOf(c) > -1) w3RemoveClass(x[i], "showtr");
	
  }
}

// Show filtered elements
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}



