// alert("Hello C4T4, I'm a JS script");
console.log("Hello, this is C4T logging");
var title = "Bye bye";
console.log(title);

var m = 23;
m -= 1;
console.log(m);

function foo() {
    // setTimeout(foo, 3000);
    console.log("Bar");
}

console.log("Start");

setTimeout(foo, 3000);

var minutes = 25;
var seconds = 0;
var timer_minutes = document.getElementById("timer_minutes");
var timer_seconds = document.getElementById("timer_seconds");
function runner() {
    
    if (seconds == 0) {
        if (minutes == 0) {
            console.log("Out of time");
            var btnStart = document.getElementById("btn_start");
            btnStart.disabled = fail;
        } else {
            minutes -= 1;
            seconds = 59;
            setTimeout(runner, 1);
        }   
    } else {
        seconds -= 1;
        setTimeout(runner, 1);
        
    } 
    
    if (minutes <10) {  
        timer_minutes.innerHTML = "0" + minutes;} 
    else{
        timer_minutes.innerHTML = minutes;
    }
        if (seconds <10) {
            timer_seconds.innerHTML = "0" + seconds;}
    else {
        timer_seconds.innerHTML = seconds;
    }
   
    console.log(minutes);
    console.log(seconds); 

}

function onStartClick() {
    var titleContent = document.getElementById("title_content");
    titleContent.innerHTML = "Timer Running";
    var btnStart = document.getElementById("btn_start");
    btnStart.disabled = true;
    minutes = 25;
    seconds = 0;
    runner();
}

function onStopClick() {
    alert("Stop Clicked");
}

