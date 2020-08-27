var i = 0;
var txt = 'Copyright © Pawel Pelech 2019';
var speed = 50;

function animateFooter() {
  if (i < txt.length) {
    document.getElementById("animated_footer").innerHTML += txt.charAt(i);
    i++;
    setTimeout(animateFooter, speed);
  }
}