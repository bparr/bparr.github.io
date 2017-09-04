
// Avoiding spambots (we don't want to be their friends)
function isJavascriptRunningOrNot() {
	var instructions = document.getElementById("contact-instructions");

	var newInstructions = 'You can contact us by filling out the form below or by sending us an email at ';
	var a = "con";
	newInstructions += "<a hr" + "e";
	var b="phnur";
	newInstructions += "f=\"mai";
	var c="om";
	newInstructions += "lto:";
	var foo = "tact";
	var bar = "sery.html"
	newInstructions += a + foo + "@" + b + bar + c + "\">";
	newInstructions += a + foo + "@" + b + bar + c + "<\/a>.";

	instructions.innerHTML = newInstructions;
}

window.onload = isJavascriptRunningOrNot;
