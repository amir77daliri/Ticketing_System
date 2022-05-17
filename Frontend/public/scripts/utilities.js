/////////////
//variables//
/////////////

let exclamationImgAddress = "../assets/icons/exclamation-circle.svg";
let checkMarkImgAddress = "../assets/icons/check.svg";
let classessOnError = "alert alert-warning my-3 p-2";
let classessOnSuccess = "alert alert-primary my-3 p-2";

/////////////
//functions//
/////////////

//function for add a warning icon to a element
function addInvalidClass(element) {
  element.classList.add("is-invalid");
}

//function for remove the warning icon from a element
function removeInvalidClass(element) {
  element.classList.remove("is-invalid");
}

//function for show the user error message
function showErrMessage(message, element) {
  element.innerHTML = message;
}

//function to check if the email tag is valid or not(pass element contain email)
function isInvalidEmail(element) {
  let isInvalid = true;
  if (element.value.includes("@") && element.value.includes(".")) {
    isInvalid = false;
    removeInvalidClass(element);
  } else {
    addInvalidClass(element);
  }

  return isInvalid;
}

//function to check if the element or elements are empty or not(pass argumant as array)
function checkEmptyField(infos) {
  let isEmpty = false;
  infos.map((data) => {
    if (data.value == "") {
      isEmpty = true;
      addInvalidClass(data);
    } else {
      removeInvalidClass(data);
    }
  });

  return isEmpty;
}

//function for check the privacy is checked or not(pass element contain privacy checkbox)
function checkPrivacyChecked(element) {
  let notChecked = false;
  if (element.checked == false) {
    notChecked = true;
    addInvalidClass(element);
  } else {
    removeInvalidClass(element);
  }

  return notChecked;
}

//funtion to check if a string have a alphabetical letter or not
function haveLetter(str) {
  return /[a-zA-Z]/.test(str);
}

//function to check if the phonenumber is valid or not(pass the element contain phonenumber)
function isInvalidPhone(element) {
  let isInvalid = true;
  if (
    element.value.startsWith("09") &&
    !haveLetter(element.value) &&
    element.value.length == 11
  ) {
    isInvalid = false;
    removeInvalidClass(element);
  } else {
    addInvalidClass(element);
  }

  return isInvalid;
}

//function to check if the password have the requirment or not(pass element contain password)
function isInvalidPassword(element) {
  let pattern = new RegExp("(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})");
  if (pattern.test(element.value)) {
    removeInvalidClass(element);
    return false;
  } else {
    addInvalidClass(element);
    return true;
  }
}

//password for check the password and confirm password is equal or not
//first element contain password and second one contain veryfied pass
function isDifferentPassword(password, verifyPass) {
  if (password.value != verifyPass.value) {
    addInvalidClass(verifyPass);
    return true;
  } else {
    removeInvalidClass(verifyPass);
    return false;
  }
}

export {
  checkMarkImgAddress,
  exclamationImgAddress,
  classessOnError,
  classessOnSuccess,
  addInvalidClass,
  removeInvalidClass,
  showErrMessage,
  isInvalidEmail,
  checkEmptyField,
  checkPrivacyChecked,
  haveLetter,
  isInvalidPhone,
  isInvalidPassword,
  isDifferentPassword,
};
