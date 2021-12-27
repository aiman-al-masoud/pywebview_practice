function onColorSelect(){
    var c = document.getElementById("color_chooser").value
    pywebview.api.on_color_select(c)
}


//(NOTMAL HTML FILE CHOOSER DOES NOT PROVIDE PATH DUE TO HTML IMPLEMENTATION).
//You need to tell python to tell window to open the filechooser 
function onFileChooser(){
    pywebview.api.open_file_chooser()
}


function onRadioChanged(){
    var id = document.querySelector('input[name="feline"]:checked').id
    pywebview.api.on_radio_changed(id)
    
}

function playASound(){
    pywebview.api.play_a_sound()
}




function onDropDownChanged(){
    v = document.getElementById("drop_down").value
    pywebview.api.on_drop_down_changed(v)
}


function onMouseEnterImage(){
    alert(event.srcElement.src)
}


function onMouseEnterWord(){
    word =  event.srcElement.innerHTML
    alert(word)
    //showById("tooltip")
    //var tooltip = document.getElementById("tooltip")
    //tooltip.innerHTML = word
    //tooltip.style.position = "absolute";
    //tooltip.style.top = 0; 
    //tooltip.style.left = 0; 
    
}




function hideById(id){
    var element = document.getElementById(id)
    element.style.display="none"
    element.style.visibility="hidden"
}

function showById(id){
    var element = document.getElementById(id)
    element.style.visibility="visible"
    element.style.display="inline-block"
}