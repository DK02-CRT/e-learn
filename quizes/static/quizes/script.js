let startTime = Date.now();
console.log("JS załadowany");

document.querySelector("form").addEventListener("submit", function(){
    document.querySelector(".task").style.display = "block";
    console.log("Start quizu");
    let seconds = Math.floor((Date.now() - startTime)/1000);
    console.log("czas:", seconds);
    document.getElementById("time").value = seconds;
    document.getElementById("startTime").value = startTime;
    
    console.log(document.getElementById("time").value);
});