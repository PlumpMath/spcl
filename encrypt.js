"use strict";

var sjcl = require("./sjcl");

var key = [0, 0, 0, 0];
var plaintext = "The rain in Spain stays mainly in the plain.";

var ctString = sjcl.encrypt(key, plaintext);
var ctJSON = JSON.parse(ctString);

console.warn("[encrypt.js] IV:", ctJSON.iv);
var ivBitArray = sjcl.codec.base64.toBits(ctJSON.iv);
console.warn("[encrypt.js] IV length:", sjcl.bitArray.bitLength(ivBitArray));

var ctPretty = JSON.stringify(ctJSON, null, "  ");
console.log(ctPretty);