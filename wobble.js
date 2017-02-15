var cir01;
var cirArr = [];
function setup() {
  createCanvas(720, 400);
  cirArr = new cir(width/2,height/2);
  cirArr = new cir (50,50);
  
}

function draw() {
  background(200);
  
  // Draw a circle
  stroke(50);
  fill(100);
  
  cir01.add_direction(5);
  cir01.set_pos();
  cir01.display();
  cir02.add_direction(5);
  cir02.set_pos();
  cir02.display();
  
}

function cir(x,y){
    this.x = x;
    this.y = y;
    this.direction = 90;
    this.speed = 1;
    
    this.set_direction = function(new_dir){
      this.direction = new_dir;
    }
    
    this.add_direction = function(delta_dir){
      this.direction += delta_dir;
    }
    
    this.set_pos = function() {
      this.x += (math.cos(radians(this.direction))*this.speed);
      text(((math.cos(radians(this.direction))*this.speed).toString()),50,50,100,100);
      this.y += (math.sin(radians(this.direction))*this.speed);
    }
    
    this.display = function() {
      ellipse(this.x, this.y, 10,10);
    }
}