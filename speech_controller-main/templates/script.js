//var grammar = '#JSGF V1.0; grammar vectors; public <vector> = right | left | back | forward ;'
var recognizer = new webkitSpeechRecognition();
//var speechRecognitionList = new SpeechGrammarList();
//speechRecognitionList.addFromString(grammar, 1);
//recognizer.grammars = speechRecognitionList;


recognizer.interimResults = true;

recognizer.lang = 'ru';

//recognition.continuous = true;

//navigator.mediaDevices.getUserMedia({ audio: true })

recognizer.onresult = function (event) {
  var result = event.results[event.resultIndex];
  if (result.isFinal) {
    //alert('Вы сказали: ' + result[0].transcript);
    send('финал');
    send(result[0].transcript);

    //result.forEach(element => send(element.transcript));
  } else {
    send(result[0].transcript);
    //alert('Промежуточный результат: '+result[0].transcript);
  }
    setTimeout(function() {
      recognizer.start();
    }, (1));

};


//recognizer.onerror = function (event) {
//  alert(event.error);
//};

function speech () {
  recognizer.start();
}
let socket = new WebSocket("ws://192.168.1.40:3333");
//let socket = new WebSocket("ws://127.0.0.1:3333");

socket.onopen = function(e) {
  //socket.send("data");
};

//socket.onerror = function(error) {
//  alert(`[error] ${error.message}`);
//};


function send (text) {
  socket.send(text);
}

