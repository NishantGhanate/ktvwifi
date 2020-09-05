function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }
  

  function updatePlan(n){
    var internetSpeed = document.getElementsByClassName('internetSpeed')[n];
    var internetPrice = document.getElementsByClassName('internetPrice')[n];
    var internetValidity = document.getElementsByClassName('internetValidity')[n];
    var internetImage = document.getElementsByClassName('internetImage')[n];
    var internetMessage = document.getElementsByClassName('internetMessage')[n];
    var internetId = document.getElementsByClassName('internetId')[n];

    var smodal = document.getElementById('speedModal');
    var pmodal = document.getElementById('priceModal');
    var vmodal = document.getElementById('validityModal');
    var mmodal = document.getElementById('messageModal');
    var imodal = document.getElementById('imageModal');
    var idModal = document.getElementById('idModal');
    
    idModal.value = internetId.value;
    smodal.value = internetSpeed.innerHTML;
    pmodal.value = internetPrice.innerHTML;
    vmodal.value = internetValidity.innerHTML;
    mmodal.value = internetMessage.innerHTML;
  }

  function deletePlan(id){
    var planIdModal = document.getElementById('planIdModal');
    planIdModal.value = id;

  }

  function updateFaq(n){
    var title = document.getElementsByClassName('title')[n].innerHTML;
    var solution = document.getElementsByClassName('solution')[n].innerHTML;
    var id = document.getElementsByClassName('faqid')[n].value;
  
    var tmodal = document.getElementById('titleModal');
    var smodal = document.getElementById('solutionModal');
    var idModal = document.getElementById('idModal');
    tmodal.value = title;
    smodal.innerHTML = solution;
    idModal.value = id;
  }

  function deleteFaq(id){
    var idModal = document.getElementById('idModalDelete');
    idModal.value = id;
  }