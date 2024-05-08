function rSentece(){
	
}

colourButton = document.getElementById("colourButton");
function backgColorChange(){
	if (invertion == false){
  	colourButton.style.webkitFilter = "invert(100%)";
    invertion = true;
  }
	else {
  	colourButton.style.webkitFilter = "invert(0)";
    invertion = false;
  }
}