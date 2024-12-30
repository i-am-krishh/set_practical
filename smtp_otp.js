// wnup papw fjvj hxiz

let min = 100000;
let max = 999999;
function otpgen(max, min){
    return Math.floor((Math.random() * max) + min);
}

const otp=otpgen(max,min);
console.log(otp);

const nodemailer = require('nodemailer');


async function sendMail() {


    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'wagh.krushna2004@gmail.com',
            pass: 'wnup papw fjvj hxiz'
        }
    })
    const mailInfo = {
        
        from: 'wagh.krushna2004@gmail.com',
        to: 'krushnasnotes@gmail.com',
        subject: 'Your otp is ' + otp,
        text: "otp seccessfully created",
        html:`
            <h1>Welcome</h1>
            <hr />
            <h2>Your OTP is ${otp}</h2>
            <b>Please do not share it with anyone</b>
            <hr />
        `
    }
    try {
        const getmail = await transporter.sendMail(mailInfo);
        console.log('Email sent successfully')
    } catch (error) {
        console.log('Email send failed with error:', error)
    }
}
sendMail()