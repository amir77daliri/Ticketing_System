/////////////
//variables//
/////////////

let showMessageButtons = document.querySelectorAll(".show-message-btn");
showMessageButtons = Array.from(showMessageButtons);

//////////////////
//eventlisteners//
//////////////////

eventListener();

function eventListener() {
  showMessageButtons.map((data, row) => {
    data.addEventListener("click", () => {
      showModalMessage(row);
    });
  });
}

/////////////
//functions//
/////////////

//function for show the message text in modal
function showModalMessage(row) {
  let modalTextDiv = document.querySelector("#modal-message-text");

  fillMessageModal(modalTextDiv, row);
}

//function for fill the message modal
function fillMessageModal(modalTextDiv, row) {
  //////////////////////////// backend ////////////////////////////
  /*
      get the message that exist in {row}th in DB
      extract the following data from it:
      the message title and message text
    */
  //////////////////////////// backend ////////////////////////////

  modalTextDiv.innerHTML = `پیامی که در سطر ${row} دیتابیس وجود داره`;
}
