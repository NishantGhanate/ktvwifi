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

    console.log(internetSpeed);
    var smodal = document.getElementById('speedModal');
    var pmodal = document.getElementById('priceModal');
    var vmodal = document.getElementById('validityModal');
    var mmodal = document.getElementById('messageModal');
    var imodal = document.getElementById('imageModal');
    smodal.value = internetSpeed.innerHTML;
    pmodal.value = internetPrice.innerHTML;
    vmodal.value = internetValidity.innerHTML;
    mmodal.value = internetMessage.innerHTML;
  }

  function deletePlan(id){
    var planIdModal = document.getElementById('planIdModal');
    planIdModal.value = id;

  }