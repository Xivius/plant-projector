const axios = require("axios");
const bodyParser = require('body-parser');
const express = require("express");
const fs = require('fs');
const mysql2 = require('mysql2');
const path = require('path');

const app = express();

app.set("view engine", "ejs");
app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

app.post('process/img', (req, res) => {
  
})

app.listen(8080, () => {
  console.log("Listening on port: 8080");
})
