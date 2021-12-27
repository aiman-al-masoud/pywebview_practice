var pattern_field = document.getElementById("pattern_field")
var string_field = document.getElementById("string_field")
var outcome_img = document.getElementById("outcome_image")
var title = document.getElementById("title")





function onChange(){
    var pattern = pattern_field.value
    var string = string_field.value

    if (pattern.length==0 && string.length==0){
        outcome_img.style.visibility = "hidden"
        outcome_img.style.display = "none"
        title.style.color="#fff"
        pattern_field.style.color = "#fff"
        string.style.color = "#fff"
        return 
    }

    pywebview.api.matches(pattern, string).then( function(response){showOutcome(response)} )


}

function showOutcome(matches){
    outcome_img.style.visibility = "visible"
    outcome_img.style.display = "inline-block"
    if(matches){
        outcome_img.src = "./match_yes.png" 
        title.style.color="green"
        pattern_field.style.color = "green"
string.style.color = "green"
    }else{
        outcome_img.src = "./match_no.png"
        title.style.color="red"
        pattern_field.style.color = "red"
        string.style.color = "red"
        
    }   
}



