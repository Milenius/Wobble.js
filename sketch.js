var angle = 0;
var slider;
var slider2;

function setup() {
  createCanvas(1000, 1000);
  slider = createSlider(0, TWO_PI, PI / 4, 0.01);
  slider2 = createSlider(0, 300, 150, 1);
}

function draw() {
  background(51);
  stroke(255);
  translate(width/2, height);
  angle += 0.01;
  branch(slider2.value());
}

function branch(len) {
  line(0, 0, 0, -len);
  
  translate(0, -len);
  if (len > 8) {
    push();
    rotate(angle);
    branch(len * 0.67);
    pop();
    push();
    rotate(-angle);
    branch(len * 0.67);
    pop();
  }
}