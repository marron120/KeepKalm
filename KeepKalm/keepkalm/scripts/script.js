function Respond()
{
    text = document.forms['suggest']['text'];

    if(text.value != "Add Suggestion Here" && text.value != "")
    {
        element = document.querySelector('#response');
        element.innerHTML = "Your suggestion has been received. Thank you for your time."    
    }
}