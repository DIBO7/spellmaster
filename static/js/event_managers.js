let fileForm = document.getElementsByTagName('form')[0] //which is the first and only (only atleast at the time of commenting)

let fileInput = fileForm.getElementsByTagName('input')[0];

let allowedFileType = [
	"text/plain",
]

let outputArea = document.getElementById('report-wrapper');

fileInput.addEventListener("change", handleFile, false);


const displayToUser = function(text){
	let newline = document.createElement("BR")
	let newSpan = document.createElement("SPAN");
	newSpan.appendChild(document.createTextNode(text))

	outputArea.appendChild(newline);
	outputArea.appendChild(newSpan);
}


function handleFile(){
	const docToRead = this.files

	if (docToRead.length === 1 && allowedFileType.includes(docToRead[0].type)) {
		submitButton = fileForm.getElementsByTagName('button')[0]
		submitButton.classList.remove("inactive");
		submitButton.disabled = false;

		displayToUser(`${docToRead[0].name} is readable!, press "proceed" to continue`)

	}else{
		submitButton = fileForm.getElementsByTagName('button')[0]
		submitButton.classList.add("inactive");
		submitButton.disabled = true;

		displayToUser(`${docToRead[0].name} is not supported at the moment! try a different file type!`)
	}
}

//TO DO NEXT is that the report-warpper acknowledges that file can be read and rewritten and "press proceed to begin reading"