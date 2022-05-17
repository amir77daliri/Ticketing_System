import * as util from "./utilities.js";

/////////////
//variables//
/////////////

const emailInput = document.querySelector("#email");
const passwordInput = document.querySelector("#password");
const invalidMessageDiv = document.querySelector("#invalid-field");
const successDiv = document.querySelector("#success-field");

let errorMessageClassList = util.classessOnError;
let successMessageClassList = util.classessOnSuccess;
let exclamationImgAddress = util.exclamationImgAddress;
let checkMarkImgAddress = util.checkMarkImgAddress;
const errorMessageOnEmpty = `<p class="${errorMessageClassList}"> <span> <img src=${exclamationImgAddress} class="icon"></img> </span> <span>فیلد ایمیل یا رمز عبور نمیتوانند خالی باشند</span>  </p>`;
const errorMessageOnWrongInfo = `<p class="${errorMessageClassList}"> <span> <img src=${exclamationImgAddress} class="icon"></img> </span> <span>ایمیل یا رمز عبور اشتباه</span>  </p>`;
const successMessage = `<p class="${successMessageClassList}"> <span> <img src=${checkMarkImgAddress} class="icon"></img> </span> <span>با موفقیت وارد شدید</span>  </p>`;

//////////////////
//eventlisteners//
//////////////////

eventListener();
function eventListener() {
  document.querySelector("#submit-btn").addEventListener("click", checkField);
}

/////////////
//functions//
/////////////

function checkField(e) {
  e.preventDefault();

  //check empty fileds
  if (util.checkEmptyField([emailInput, passwordInput])) {
    util.showErrMessage(errorMessageOnEmpty, invalidMessageDiv);
    return;
  }

  //////////////////////////// backend ////////////////////////////

  /*
      check if the email and password are match
      if match -> 
        continue and redirect to index page
      
      else -> 
        call ' showErrMessage(errorMessageOnWrongInfo) ' and then return
    */

  //////////////////////////// backend ////////////////////////////

  //empty the invalid div if have content and show success message
  util.showErrMessage("", invalidMessageDiv);
  util.showErrMessage(successMessage, successDiv);

  //wait 1.5sec and reload the page
  setTimeout(() => {
    location.reload();
  }, 1500);
}
