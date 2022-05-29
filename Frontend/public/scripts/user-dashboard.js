/////////////
//variables//
/////////////

let fakeInfoForTest = [
  {
    messageTitle: "تایتل پیام سطر 0 دیتابیس",
    messageText: "محتویات پیام سطر 0 دیتابیس",
  },
  {
    messageTitle: "تایتل پیام سطر1 دیتابیس",
    messageText: "محتویات پیام سطر 1 دیتابیس",
  },
  {
    messageTitle: "تایتل پیام سطر 2 دیتابیس",
    messageText: "محتویات پیام سطر 2 دیتابیس",
  },
];

let showMessageButtons = document.querySelectorAll(".show-message-btn");
showMessageButtons = Array.from(showMessageButtons);

let showResponseButtons = document.querySelectorAll(".response-btn");
showResponseButtons = Array.from(showResponseButtons);

//////////////////
//eventlisteners//
//////////////////

eventListener();

function eventListener() {
  //click event for each of the show message button
  showMessageButtons.map((data, row) => {
    data.addEventListener("click", () => {
      showModalMessage(row);
    });
  });

  //click event for each of the show response message button
  showResponseButtons.map((data) => {
    data.addEventListener("click", () => {
      let row =
        data.parentNode.parentNode.parentNode.querySelector("th").innerHTML;

      row = row - 1;
      showResponseMessage(row);
    });
  });
}

/////////////
//functions//
/////////////

//function for show the message text in modal
function showModalMessage(row) {
  let modalTitleDiv = document.querySelector("#modal-message-title");
  let modalTextDiv = document.querySelector("#modal-message-text");

  fillMessageModal(modalTitleDiv, modalTextDiv, row);
}

//function for show the response message in modal
function showResponseMessage(row) {
  let modalTitleDiv = document.querySelector("#modal-response-title");
  let modalTextDiv = document.querySelector("#modal-response-answer");

  fillResponseModal(modalTitleDiv, modalTextDiv, row);
}

//function for fill the message modal
function fillMessageModal(modalTitleDiv, modalTextDiv, row) {
  //////////////////////////// backend ////////////////////////////
  /*
    get the message that exist in {row}th in DB
    extract the following data from it:
    the message title and message text
  */
  //////////////////////////// backend ////////////////////////////

  modalTitleDiv.innerHTML = `عنوان پیام : ${fakeInfoForTest[row].messageTitle}`;
  modalTextDiv.innerHTML = fakeInfoForTest[row].messageText;
}

//function for fill the response modal
function fillResponseModal(modalTitleDiv, modalTextDiv, row) {
  //////////////////////////// backend ////////////////////////////
  /*
    get the message that exist in {row}th in DB
    extract the following data from it:
    the message tracking id and message response text
  */
  //////////////////////////// backend ////////////////////////////

  const message = {
    messageTrackingId: ` جواب پیام با کد رهگیری : کد رهگیری پیامی که در سطر ${row} دیتابیس است`,
    messageResponseText: `جواب پیام که در سطر ${row} دیتابیس هستش`,
  };

  modalTitleDiv.innerHTML = message.messageTrackingId;
  modalTextDiv.innerHTML = message.messageResponseText;
}
