function onSubmit(){
    
    //console.log("sdm")
    //alert("hello!")
    //alert(document.getElementById("my_field").value)

    myInput = document.getElementById("my_field").value

    pywebview.api.test_print()

    // you can pass strings seamlessly to python!
    pywebview.api.print_obj(myInput)
}