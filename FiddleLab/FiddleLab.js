colourButton = document.getElementById("colourButton");
function randNum(){
	let x = Math.random() * 10000;
  document.getElementById("randNum").innerHTML = x;
}

//Invertion is needed as that way we have a way to start a sort of microloop that
//Checks which colours it has and if it is inverted then it does the reverse.
//If its not inverted it inverts it
invertion = false;
function bColorChange(){
	if (invertion == false){
  	colourButton.style.webkitFilter = "invert(100%)";
    invertion = true;
  }
	else {
  	colourButton.style.webkitFilter = "invert(0)";
    invertion = false;
  }
}

function rSentence(){
	uName = document.getElementById("username").value;
  let x = Math.random() * 1000;
  document.getElementById("randomSentence").innerHTML = "Hi! " + uName + " Your Rando Number is: " + x;
}