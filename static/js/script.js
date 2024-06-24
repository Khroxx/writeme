function enableButton(){
    if(regPassword.value === regPasswordAgain.value){
        regButton.disabled = false;
    }
    else{
        regButton.disabled = true;
    }
}
