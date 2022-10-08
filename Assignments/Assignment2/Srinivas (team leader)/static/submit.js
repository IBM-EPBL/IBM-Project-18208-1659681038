function confirmForm(form){
    if(!(form.password.value == form.cpassword.value)){
        alert("Password must be the same");
        form.cpassword.focus();
        return false;
    }
    else {
        return true;
    }
}