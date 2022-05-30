/////////////
//variables//
/////////////

const ticketInfoDiv = document.querySelector("#ticket-info-part");
const ticket = {
  status: 1, // 1-> in queue , 2-> in progress , 3-> finished
  trackId: 123, //must be random and unique
  title: "عنوان تیکت",
  content: "محتوای پیام",
  date: new Date(),
};

let foundMessagePattern = `
<div class="row rounded bg-light p-4">
    
    <h3 class="fw-bold text-center text-primary">تیکت با کد رهگیری ${
      ticket.trackId
    } پیدا شد</h3>
    
    <hr/>
    
    <p class="text-center"> <span class="fw-bold">وضعیت</span> : <br/><br/><span>${toStr(
      ticket.status
    )}</span></p>
    
    <hr/>
    
    <p class="text-center"> <span class="fw-bold">عنوان : </span> <br/><br/><span>${
      ticket.title
    }</span></p>
    
    <hr/>
    
    <p class="text-center"> <span class="fw-bold">محتوای پیام :</span> <br><br><span> ${
      ticket.content
    }</span></p>
    <hr/>

    <p class="text-center"> <span class="fw-bold">تاریخ :</span> <br><br><span> ${
      ticket.date
    } </span></p>

</div>
`;

let notFoundImagAddress = "../assets/images/not-found.png";
let notFoundMessagePattern = `
<div class="row rounded bg-light p-4 align-items-center">
    <div class="col">
        <h3 class="fw-bold text-center text-danger">تیکت با کد رهگیری ${ticket.trackId} پیدا نشد</h3>
    </div>
    <div class="col">
        <img src="${notFoundImagAddress}" class="img-fluid"></img>
    </div>
</div>
`;

//////////////////
//eventlisteners//
//////////////////

eventListener();
function eventListener() {
  // if found ->
 // ticketInfoDiv.innerHTML = foundMessagePattern;

  // else ->
  ticketInfoDiv.innerHTML = notFoundMessagePattern;
}

/////////////
//functions//
/////////////

//function for convert the status of ticket into string
function toStr(number) {
  switch (number) {
    case 1:
      return "در انتظار بررسی";
    case 2:
      return "در حال بررسی";
    case 3:
      return "خاتمه یافته";
  }
}
