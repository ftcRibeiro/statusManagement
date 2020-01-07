$(document).read(function(){
    function createMaquinas(){
        $.ajax({
            type: "POST",
            url: "skd",
            data:{
                'nome': $("#formData.name")
            },
            success: function(result){
                atualizaTela()
            },
            error: function(result){

            }

        })

        
    }
})