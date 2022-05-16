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

export {
  checkMarkImgAddress,
  exclamationImgAddress,
  classessOnError,
  classessOnSuccess,
  addInvalidClass,
  removeInvalidClass,
  showErrMessage,
  checkEmptyField,
};
