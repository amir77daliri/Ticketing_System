import * as util from "./utilities.js";

/////////////
//variables//
/////////////

const messageTitle = document.querySelector("#title");
const messageContent = document.querySelector("#message");
const submitBtn = document.querySelector("#submit-btn");
const invalidDiv = document.querySelector("#invalid-field");
const successDiv = document.querySelector("#success-field");

const errOnEmptyFields = `<p class="${util.classessOnError}"> <span><img src=${util.exclamationImgAddress} class="icon"> </img></span> <span> تمامی فیلد ها باید پر شوند </span> </p>`;

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
  if (util.checkEmptyField([messageTitle, messageContent])) {
    util.showErrMessage(errOnEmptyFields, invalidDiv);
    return;
  }

  //////////////////////////// backend ////////////////////////////

  //object for save in DB
  const ticket = {
    status: 1, // 1-> in queue , 2-> in progress , 3-> finished
    trackId: 123, //must be random and unique
    title: messageTitle.value,
    content: messageContent.value,
    date: new Date(),
  };

  //json format
  //jsonFile=JSON.stringify(ticket);

  /*
      send ticket to DB and save
      properties:
      status , trackId , title , content , date
  */

  //////////////////////////// backend ////////////////////////////

  //empty the invalid div if have content and show success message
  util.showErrMessage("", invalidDiv);
  const successMessage = `<p class="${util.classessOnSuccess}"> <span><img src=${util.checkMarkImgAddress} class="icon"> </img></span> <span> تیکت با کد رهگیری ${ticket.trackId} با موفقیت ثبت شد </span> </p>`;
  util.showErrMessage(successMessage, successDiv);

  //wait 1.5sec and reload the page
  setTimeout(() => {
    console.log(ticket);
    window.alert(
      "میتوانید کد پیگیری را یادداشت کنید یا در بخش پروفایل مشاهده کنید"
    );
    location.reload();
  }, 1500);
}
