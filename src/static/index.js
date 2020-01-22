function myFunction() {

        if(document.getElementById('keyaccount').checked) {
//            document.getElementById('submit').href = "location.href='../keyAccount'";
              location.replace("http://127.0.0.1:8000/keyAccount")

        }
        else{
//        	document.getElementById('submit').href = "location.href='../sohom'";
              location.replace("http://127.0.0.1:8000/sohom")

        }

   }

 function myFunction1(){

      if(document.getElementById('resdential').checked) {
//            document.getElementById('submit').href = "location.href='../keyAccount'";
              location.replace("http://127.0.0.1:8000/residential")

        }
        else{
//        	document.getElementById('submit').href = "location.href='../sohom'";
              location.replace("http://127.0.0.1:8000/Enterprise")

 }
 }

 var attending = "bussiness mobile";


 function residential(){
         if(document.getElementById('Business').checked) {
              attending = "bussiness mobile";
               location.replace("http://127.0.0.1:8000/generatenumber")

        }
        else{
              attending = "broad band";
               location.replace("http://127.0.0.1:8000/generatenumber")
        }

 }

document.getElementById("attending").innerHTML = "Bussiness Mobile";
