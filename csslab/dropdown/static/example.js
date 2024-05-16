// Change the Name displayed in the Text when the Dropdown changes
function updateName() {

    dropdown = document.getElementById("last_name");
   
    the_name = document.getElementById("bold_name");
    the_name.innerHTML = dropdown.value;
    
}

//When the button is clicked, add a new option to the dropdown
function addDropdownItem() {

    // This page has more information about changing
    // HTML <select> objects in JavaScript
    // https://www.w3schools.com/jsref/met_select_add.asp

    dropdown = document.getElementById("last_name");

    first_name = document.getElementById("first_input").value;
    last_name = document.getElementById("last_input").value;

    new_option = document.createElement("option");
    new_option.text = last_name;
    new_option.value = first_name + " " + last_name;
    dropdown.add(new_option);

    // This code is commented out to actually insert the new values
    //    ... Into the database

    //URL = "/insert/" + first_name + "/" + last_name;
    //fetch(URL)
    
}


