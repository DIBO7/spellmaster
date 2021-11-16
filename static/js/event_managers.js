let fileForm = document.getElementsByTagName('form')[0] //which is the first and only (only atleast at the time of commenting)

let fileInput = fileForm.getElementsByTagName('input')[0];

fileInput.addEventListener("change", handleFile, false);


let allowedFileType = [
	"text/plain",
]

function handleFile(){
	const docToRead = this.files

	if (docToRead.length === 1 && allowedFileType.includes(docToRead[0].type)) {
		submitButton = fileForm.getElementsByTagName('button')[0]
		submitButton.classList.remove("inactive");
	}else{
		submitButton = fileForm.getElementsByTagName('button')[0]
		submitButton.classList.add("inactive");
	}
}

//TO DO NEXT is that the report-warpper acknowledges that file can be read and rewritten and "press proceed to begin reading"