var MongoClient = require('mongodb').MongoClient;
var nodemailer = require('nodemailer');
var fs = require('fs');
var ini = require('ini');
var config = ini.parse(fs.readFileSync('./config.ini', 'utf-8'))
var email_address, email_addresses = config.email_addresses.array;
var max_temp = config.temperatures.maximum;
var min_temp = config.temperatures.minimum;

       
MongoClient.connect("mongodb://127.0.0.1/env_mon", function(err, db) {
    var dbo = db.db("env_mon");
    dbo.collection("senseentries_archives").find().sort({"created": -1}).limit(1).toArray(function(err, result) {
	    var temperature = result[0].temperature
	
	    if (temperature >= max_temp || temperature <= min_temp) {
            var rounded_temp = Math.round(temperature)
            var subject  = `Lawrence Temp Alert: ${rounded_temp} Degrees`;
            var message = `The Lawrence OIT area temperature is ${rounded_temp} degrees.`;
            var transOptions = {
                    host: 'mail.ivytech.edu',
                    port: 25,
                    secure: false,
                    igonreTLS: true
            };
            var transporter = nodemailer.createTransport(transOptions);

            for (email_address of email_addresses){
                var mainOptions = {
                        from: 'envmon@ivytech.edu',
                        to: email_address,
                        subject: subject,
                        text: message
                };
                transporter.sendMail(mainOptions);
	        }
       	}    
    });
    db.close();
});
