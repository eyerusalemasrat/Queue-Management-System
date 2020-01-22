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

