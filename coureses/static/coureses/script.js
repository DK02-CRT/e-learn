let startTime;
console.log("JS załadowany");
document.getElementById("time").value = 1;
function zadania() {
console.log("JS załadowany");
    document.querySelector(".task").style.display = "block";
    startTime = Date.now();
}

document.querySelector("form").addEventListener("submit", function(){
    console.log("Start quizu");
    let seconds = Math.floor((Date.now() - startTime)/1000);
    document.getElementById("time").value = seconds;
    
    console.log("czas:", seconds);
    console.log(document.getElementById("time").value);
});