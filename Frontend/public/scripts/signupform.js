import * as util from "./utilities.js";

/////////////
//variables//
/////////////

const email = document.querySelector("#email");
const phoneNumber = document.querySelector("#phoneNumber");
const password = document.querySelector("#password");
const passwordVerify = document.querySelector("#passwordVerify");
const privacyCheck = document.querySelector("#privacyCheck");
const submitBtn = document.querySelector("#submit-btn");
const invalidDiv = document.querySelector("#invalid-field");
const successDiv = document.querySelector("#success-field");

let classessOnError = util.classessOnError;
let classessOnSuccess = util.classessOnSuccess;
let exclamationImgAddress = util.exclamationImgAddress;
let checkMarkImgAddress = util.checkMarkImgAddress;

const errOnEmptyFields = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> تمامی فیلد ها باید پر شوند </span> </p>`;
const errOnPrivacyNotChecked = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> باید شرایط را قبول کنید </span> </p>`;
const errOnInvalidPhone = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> شماره تلفن نا معتبر </span> </p>`;
const errOnInvalidEmail = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> ایمیل نا معتبر </span> </p>`;
const errOnInvalidPassword = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> پسوورد نا معتبر </span> </p>`;
const errOnNotUniquePhoneEmail = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> این ایمیل یا شماره تلفن قبلا ثبت شده </span> </p>`;
const errOnNotEqualPass = `<p class="${classessOnError}"> <span><img src=${exclamationImgAddress} class="icon"> </img></span> <span> مغایرت پسورد ها </span> </p>`;
const successMessage = `<p class="${classessOnSuccess}"> <span><img src=${checkMarkImgAddress} class="icon"> </img></span> <span> ثبت نام با موفقیت انجام شد </span> </p>`;

//////////////////
//eventlisteners//
//////////////////

eventListener();
function eventListener() {
  submitBtn.addEventListener("click", signup);
}

/////////////
//functions//
/////////////

//function for signup the user with the givven info
function signup(e) {
  e.preventDefault();

  //check empty fileds
  if (util.checkEmptyField([email, phoneNumber, password, passwordVerify])) {
    util.showErrMessage(errOnEmptyFields, invalidDiv);
    return;
  }

  //check email is valid
  if (util.isInvalidEmail(email)) {
    util.showErrMessage(errOnInvalidEmail, invalidDiv);
    return;
  }

  //check phone number is valid
  if (util.isInvalidPhone(phoneNumber)) {
    util.showErrMessage(errOnInvalidPhone, invalidDiv);
    return;
  }

  //////////////////////////// backend ////////////////////////////

  /*
      check if the email and phone are unique
      if unique -> 
        continue
      
      else -> 
        call ' showErrMessage(errOnNotUniquePhoneEmail) ' and then return
    */

  //////////////////////////// backend ////////////////////////////

  //check the password verify length and requirment
  if (util.isInvalidPassword(password)) {
    util.showErrMessage(errOnInvalidPassword, invalidDiv);
    return;
  }

  //check the password and confirm field are equal
  if (util.isDifferentPassword(password, passwordVerify)) {
    util.showErrMessage(errOnNotEqualPass, invalidDiv);
    return;
  }

  //last checking for accepting the rules
  if (util.checkPrivacyChecked(privacyCheck)) {
    util.showErrMessage(errOnPrivacyNotChecked, invalidDiv);
    return;
  }

  //empty the invalid div if have content and show success message
  util.showErrMessage("", invalidDiv);
  util.showErrMessage(successMessage, successDiv);

  //////////////////////////// backend ////////////////////////////

  //object for save in DB
  const user = {
    userEmail: email.value,
    userPhone: phoneNumber.value,
    userPassword: password.value,
  };

  //json format
  //jsonFile=JSON.stringify(user);

  /*
      send user to DB and save (user also have 'ticketList')
      properties:
      user email , user phonenumber , user password , user tickets list
  */

  //////////////////////////// backend ////////////////////////////

  //wait 1.5sec and reload the page
  setTimeout(() => {
    location.reload();
  }, 1500);
}
