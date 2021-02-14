window.onload = function main() {
  var main = document.querySelector('main');
  var location = document.getElementById('location');
  var snap = document.getElementById('snap');
  var video = document.getElementById('video');
  const constraints = {
    video : {
      facingMode: {
        ideal: "environment"
      }
    }
  }

  if (!navigator.mediaDevices || !navigator.mediaDevices.enumerateDevices) {
    location.innerHTML = "Error Occured: Back camera not supported.");
    return;
  }

  navigator.mediaDevices.enumerateDevices()
  .then(function(devices) {
    var cameras = [];
    devices.forEach(function (device) {
      if (device.kind === 'videoInput') {
        cameras.push(device);
      }
    });
    
  })
  .catch(function(err) {
    console.log(err.name + ": " + err.message);
  });

  // Access camera
  if (navigator.mediaDevices) {
    if (navigator.mediaDevices.getUserMedia) {
      // { audio: true }` would capture audio too
      navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
        video.srcObject = stream;
        video.play();
      });
    } else { // Standard
      navigator.getUserMedia(constraints, function (stream) {
        video.src = stream;
        video.play();
      }, errBack);
    }
  } else if (navigator.webkitGetUserMedia) { // WebKit-prefixed
      navigator.webkitGetUserMedia(constraints, function (stream) {
        video.src = window.webkitURL.createObjectURL(stream);
        video.play();
      }, errBack);
    } else if (navigator.mozGetUserMedia) { // Mozilla-prefixed
      navigator.mozGetUserMedia(constraints, function (stream) {
        video.src = window.URL.createObjectURL(stream);
        video.play();
      }, errBack);
    };

  // Take Photo
  snap.addEventListener("click", (e) => {
    e.preventDefault();
    if (navigator.)
    var canvas = document.createElement('canvas');
    canvas.width = video.offsetWidth;
    canvas.height = video.offsetHeight;
    var context = canvas.getContext('2d');
    context.drawImage(video, 0, 0);
    var dataURL = canvas.toDataURL().split('base64,')[1];
    var req = new XMLHttpRequest();
    req.open("POST", "https://127.0.0.1:8000/analyze");
    req.overrideMimeType("application/json");

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        req.overrideMimeType("application/json");
        req.send(JSON.stringify({x: longitude, y: latitude, img: dataURL}));
      });
    } else {
      location.innerHTML = "Error Occured: Geolocation is not supported by this browser.";
    }
  });
}
