const music = new Audio('sabredeluz.mp3');
const music1 = new Audio('sabredeluzF.mp3');
function mouseOver() { 
    music.play(); 
    music1.pause();
    music1.currentTime = 0;
}
function mouseLeave(){
    music1.play();
    music.pause();
    music.currentTime = 0;
    
}