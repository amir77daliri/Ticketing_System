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

let responseModalSubmitBtn = document.querySelector(
  "#modal-response-submit-btn"
);

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

  //click event for submit button in responsing a ticket
  responseModalSubmitBtn.addEventListener("click", findTrackingId);
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
  let modalSelectOptionDiv = document.querySelector("#ticket-status");

  fillResponseModal(modalTitleDiv, modalTextDiv, modalSelectOptionDiv, row);
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
function fillResponseModal(
  modalTitleDiv,
  modalTextDiv,
  modalSelectOptionDiv,
  row
) {
  //////////////////////////// backend ////////////////////////////
  /*
      get the message that exist in {row}th in DB
      extract the following data from it:
      the message tracking id and message response text and status
    */
  //////////////////////////// backend ////////////////////////////

  const message = {
    messageTrackingId: ` ویرایش تیکت با کد رهگیری : کد رهگیری پیامی که در سطر ${row} دیتابیس است`,
    messageResponseText: `جواب پیام که در سطر ${row} دیتابیس هستش`,
    messageStatus: 2, //(1 -> in queue , 2 -> in progress , 3 -> finished)
  };

  modalTitleDiv.innerHTML = message.messageTrackingId;
  modalTextDiv.innerHTML = message.messageResponseText;
  modalSelectOptionDiv.value = message.messageStatus;
}

//function for find the ticket tracking id
function findTrackingId(e) {
  e.preventDefault();
  //find the ticket tracking id
  let modalTitle =
    responseModalSubmitBtn.parentNode.parentNode.parentNode.querySelector(
      "#modal-response-title"
    ).innerHTML;

  /*
        the title is :
            "edit ticket with id : {id}"
        
        so if we split the title with below pattern , second element in ouput array
        will be the tracking id
    */

  modalTitle = modalTitle.split(" : ");
  let trackingId = modalTitle[1];

  updateTicket(trackingId);
}

//functino for update the ticket state
function updateTicket(trackingId) {
  let modalTextDiv = document.querySelector("#modal-response-answer");
  let modalSelectOptionDiv = document.querySelector("#ticket-status");

  const ticketNewState = {
    ticketAnswer: modalTextDiv.value,
    ticketStatus: modalSelectOptionDiv.value,
  };

  //////////////////////////// backend ////////////////////////////
  /*
    find the message with id {trackingId} pass as a argumant in DB
    update the following data of it:
    the ticket answer and ticket status
  */
  //////////////////////////// backend ////////////////////////////
}
