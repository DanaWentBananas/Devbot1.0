const mqtt = require("mqtt")
const express = require("express")
const app = express();

const client = mqtt.connect("mqtt://44.202.67.39", {
  username: 'caruser', 
  password: 'caruser333' 
});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/button1', (req, res) => {
  client.publish('move', '1');
  console.log("message published!")
});

app.get('/button2', (req, res) => {
  client.publish('move', '2');
  console.log("message published!")
});

app.get('/button3', (req, res) => {
  client.publish('move', '3');
  console.log("message published!")
});

app.get('/button4', (req, res) => {
  client.publish('move', '4');
  console.log("message published!")
});

speed=50

app.get('/button5', (req, res) => {
  if(speed>99){
    console.log("done!")
  }
  else{
    speed+=1
    client.publish('move', String(speed));
  }
});

app.get('/button6', (req, res) => {
  if(speed<20){
    console.log("done!")
  }
  else{
    speed-=1
    client.publish('move', String(speed));
  }
});

app.get('/invbtn', (req, res) => {
  client.publish('move', 'stop');
});

// Start the server on port 8080
app.listen(8080, () => {
  console.log('Server listening on port 8080');
});
