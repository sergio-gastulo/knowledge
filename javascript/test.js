i = 0;


function handleEnter(event){
    if (event.key === "Enter"){
        getString();
        i++;
    }
}

function getString(){
    
    let userInput = document.getElementById("userInput").value;

    let message = document.createElement("p");

    message.textContent = `your ${i}th word was ${userInput}`;

    document.getElementById("message").append(message);
    document.getElementById("userInput").value = "";

}