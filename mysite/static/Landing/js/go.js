$( document ).ready(function(){
    console.log("Document Loaded");
    $("#submit").click(function(event){
        event.preventDefault();
    });
    $("#submit").on( "click", sendForm );
})

function sendForm(){
    var fd = new FormData();
    const videoInput = $('#videoInput').prop('files')[0];
    var sendRequest = false;
    if (videoInput != undefined){
        console.log(videoInput);
        sendRequest = true;
        console.log('form includes videoInput');
        fd.append('videoInput', videoInput);
    }
    
    if (sendRequest){
        console.log(fd);
        fd.forEach(function(key, value){
            console.log(key + " : " + value);
        })
        $.ajax({
            type : 'POST',
            url : '/go',
            data: fd,
            processData: false,  // tell jQuery not to process the data
            contentType: false,   // tell jQuery not to set contentType
            success: sendSuccess,
            error: function(e) {
                console.log(e);
            },
        });
    }  

}

function sendSuccess(data){
    if (data == "success"){
        alert("edits successful");
      }else {
        alert(data);
      }
}