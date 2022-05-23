import * as util from "./utilities.js";

/////////////
//variables//
/////////////

const senderName = document.querySelector("#name");
const senderEmail = document.querySelector("#email");
const senderMessage = document.querySelector("#message");
const submitBtn = document.querySelector("#submit-btn");
const invalidDiv = document.querySelector("#invalid-field");
const successDiv = document.querySelector("#success-field");

let classessOnError = util.classessOnError;
let classessOnSuccess = util.classessOnSuccess;
let exclamationImgAddress = util.exclamationImgAddress;
let checkMarkImgAddress = util.checkMarkImgAddress;
const errOnEmptyFields = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> تمامی فیلد ها باید پر شوند </span> </p>`;
const errOnInvalidEmail = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> ایمیل نا معتبر </span> </p>`;
const successMessage = `<p class="${classessOnSuccess}"> <span><img src=${checkMarkImgAddress} class="icon"> </img></span> <span> پیام شما با موفقیت ارسال شد </span> </p>`;

//////////////////
//eventlisteners//
//////////////////

eventListener();
function eventListener() {
  submitBtn.addEventListener("click", sendMessage);
}

/////////////
//functions//
/////////////

function sendMessage(e) {
  e.preventDefault();

  //check empty fileds
  if (util.checkEmptyField([senderName, senderEmail, senderMessage])) {
    util.showErrMessage(errOnEmptyFields, invalidDiv);
    return;
  }

  //check email is valid
  if (util.isInvalidEmail(senderEmail)) {
    util.showErrMessage(errOnInvalidEmail, invalidDiv);
    return;
  }

  //empty the invalid div if have content and show success message
  util.showErrMessage("", invalidDiv);
  util.showErrMessage(successMessage, successDiv);

  //////////////////////////// backend ////////////////////////////

  //object for save in DB
  const message = {
    senderName: senderName.value,
    senderEmail: senderEmail.value,
    senderMessage: senderMessage.value,
    date: new Date(),
  };

  //json format
  //jsonFile=JSON.stringify(message);

  /*
      send message to DB and save
      properties:
      sender name , sender email , sender message , time and date the message sended
  */

  //////////////////////////// backend ////////////////////////////

  //wait 1.5sec and reload the page
  setTimeout(() => {
    location.reload();
  }, 1500);
}
