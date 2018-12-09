document.onload=init();

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
}