document.onload=init();
var matrix = "";

function init(){
	var cells = document.getElementsByTagName("td");
	for ( i = 0;i<cells.length;i++){
		cells[i].onclick =function(){ activateCell(this)};
	}
}

function activateCell(cell){
	console.log(cell);
	
	if (cell.className != "active"){
		cell.className = "active";
	}
	else{
		cell.className = "";
	}
	serialize();
	send();
}

function serialize(){
	var cells = document.getElementsByTagName("td");
	matrix = "";
	for(i = 0; i < cells.length;i++){
		if (cells[i].className != "active"){
			matrix += "0";
		}
		else{
			matrix += "1";
		}
		
	}
	matrix += "E";
}

function send(url){
	var xhttp;
  xhttp=new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log(xhttp.responseText);
    }
  };
  xhttp.open("GET", 'api/0.1/send/?matrix='+matrix, true);
  xhttp.send();
}

