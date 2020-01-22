function myFunction() {

        if(document.getElementById('keyaccount').checked) {
            document.getElementById('generateToken').href = "location.href='../keyAccount'";
        }
        else{
        	document.getElementById('generateToken').href = "location.href='../sohom'";
        }
    }