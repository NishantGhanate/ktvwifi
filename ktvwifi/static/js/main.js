var readComplaintModal = document.getElementsByClassName("modal")[0];
var span = document.getElementsByClassName("close")[0];
function show(n) {
  var username = document.getElementsByClassName("complaintUser")[n];
  var complaintId = document.getElementsByClassName("complaintId")[n];
  var date = document.getElementsByClassName("complaintDate")[n];
  var title = document.getElementsByClassName("complaintTitle")[n];
  var message = document.getElementsByClassName("complaintMessage")[n];
  var complaintSol = document.getElementsByClassName("complaintSol")[n];
  // console.log(date.value,title.value,message.value);
  var readComplaintUsername = document.getElementById("readComplaintUsername");
  var readComplaintDate = document.getElementById("readComplaintDate");
  var readComplaintTitle = document.getElementById("readComplaintTitle");
  var readComplaintTextArea = document.getElementById("readComplaintTextArea");
  var readComplaintId = document.getElementById("readComplaintId");
  var readComplaintTextAreaSol = document.getElementById("readComplaintTextAreaSol");
  if (username != null){
    readComplaintUsername.value = username.value;
    readComplaintId.value = complaintId.value;
    
  }
  
  readComplaintTextAreaSol.innerHTML = complaintSol.value;
  readComplaintTitle.value = title.value;
  readComplaintDate.innerHTML = date.value;
  readComplaintTextArea.innerHTML = message.value;
  readComplaintModal.style.display = "block";
}


if(span != null){
  span.onclick = function() {
    readComplaintModal.style.display = "none";
  }
}

var writeComplaintModal = document.getElementById("writeComplaint");
var closeWrite = document.getElementById("closeWrite");
function writeComplaint(){
  writeComplaintModal.style.display = "block";
}



function contact(n) {
  var contactId = document.getElementsByClassName("complaintId")[n];
  var contactName = document.getElementsByClassName("contactName")[n];
  var contactEmail = document.getElementsByClassName("contactEmail")[n];
  var contactTitle = document.getElementsByClassName("contactTitle")[n];
  var contactMessage = document.getElementsByClassName("contactMessage")[n];
  var contactsolution = document.getElementsByClassName("contactsolution")[n];

  var contact_id = document.getElementById("contact_id");
  var readContactName = document.getElementById("readContactName");
  var readContactTitle = document.getElementById("readContactTitle");
  var readContactTextArea = document.getElementById("readContactTextArea");
  var readContactTextAreaSol = document.getElementById("readContactTextAreaSol");

  contact_id.value = contactId.value;
  readContactName.value = contactName.value ;
  readContactTitle.innerHTML = contactTitle.value;
  readContactTextArea.innerHTML = contactMessage.value;
  readContactTextAreaSol.innerHTML = contactsolution.value

}