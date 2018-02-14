
/// Uso la libreria jquery per trattare il form

$("form").submit(function(e){
    e.preventDefault();  /// Non ricarica la pagina

    /// La cosa più semplice è questa...:
    //
    // var dati_serializzati = JSON.stringify(
    //   $("form").serializeArray()
    //	);
    //
    /// ...e viene fuori una cosa così:
    /// [{"name":"num1","value":"1"},{"name":"num2","value":"1.2"},{"name":"txt","value":"asd"}]
    
    /// ... ma io compatto per evitare ogni volta name e value: {"num1":"1","num2":"1.2","txt":"asd"}
    var dati_grezzi = {};
    $.each($('form').serializeArray(), function() {
	    dati_grezzi[this.name] = this.value;	    
    });

    dati_serializzati = JSON.stringify(dati_grezzi);

    /// Che cosa sto inviando al PHP?
    $("output").html("hai inviato al php questi dati: <br>"+dati_serializzati)

    /// Mando tutto al PHP
    $.ajax({
	type: 'GET',                      /// Che metodo uso?
	url: './roba-server.php',         /// A che file lo mando?
	data: {mydata:dati_serializzati}, /// Che cosa mando?
	dataType: 'json',                 /// Che tipo di dati?
    })
	.done( function( data ) {         /// Che cosa dico se tutto va bene?
	    console.log('Fatto!');        /// Guarda nella console del browser (F12)!
	    console.log(data);
	    $("article").text(JSON.stringify(data)); /// Dove li metto?
	})
	.fail( function( data ) {         /// Che cosa dico se qualcosa va storto?
	    console.log('Oh, no!');       /// Guarda nella console del browser (F12)!
	    console.log(data);
	});        
     
})
