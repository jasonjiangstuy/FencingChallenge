$( document ).ready(function(){
    $("submit").on( "click", sendForm );
})

function sendForm(){
    var fd = new FormData();
    const videoInput = $('#videoInput').prop('files')[0];
    var sendRequest = false;
    if (videoInput != undefined){
        sendRequest = true;
        console.log('form includes videoInput');
        fd.append('videoInput', videoInput);
    }
    if (sendRequest){
        $.ajax({
            type : 'POST',
            url : '/go',
            data: fd,
            processData: false,  // tell jQuery not to process the data
            contentType: false,   // tell jQuery not to set contentType
            success: sentSuccess,
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