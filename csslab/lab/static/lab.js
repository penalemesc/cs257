//If its not inverted it inverts it
invertion = false;
document.getElementById('mouseOverPara').onmouseover = function() {
  if (invertion == false){
  	this.style.webkitFilter = "invert(100%)";
    invertion = true;
  }
	else {
  	this.style.webkitFilter = "invert(0)";
    invertion = false;
  }
};


