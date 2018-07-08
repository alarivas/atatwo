$(document).ready(function(){    
    $('#cerrar-resultados').click(function(){
        if ($('#cont-map').hasClass("map_abierto")) {
            $('#cont-map').removeClass('map_abierto');
            $( this ).removeClass('map_abierto');
        } else {
            $('#cont-map').addClass('map_abierto');
            $( this ).addClass('map_abierto');
        }
    });


});